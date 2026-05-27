import os
import re
import json
import tempfile
import logging
import time
import struct

import requests

from astrbot.api.star import Context, Star
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.core.message.components import Video, Image, Record

logger = logging.getLogger(__name__)

# 抖音链接正则（合并为一个模式用于自动检测）
DOUYIN_REGEX = r'(?:https?://v\.douyin\.com/\S+|https?://(?:www|m)\.douyin\.com/(?:video|note)/\d+\S*|https?://(?:www|m)\.iesdouyin\.com/share/(?:video|slides)/\d+\S*)'

# 用于提取 URL 的模式列表
DOUYIN_PATTERNS = [
    r'https?://v\.douyin\.com/\S+',
    r'https?://(?:www|m)\.douyin\.com/video/\d+',
    r'https?://(?:www|m)\.douyin\.com/note/\d+',
    r'https?://(?:www|m)\.iesdouyin\.com/share/(?:video|slides)/\d+',
]


class DouyinDownloader(Star):
    def __init__(self, context: Context, config: dict = None):
        super().__init__(context, config)
        self.proxy = (config or {}).get('proxy', '')
        logger.info(f"DouyinDownloader 插件已加载, proxy={self.proxy or '无'}")

    def _text_result(self, event: AstrMessageEvent, text: str):
        """创建纯文字结果（禁用文字转图片）"""
        result = event.plain_result(text)
        result.use_t2i_ = False
        return result

    def _video_result(self, event: AstrMessageEvent, file_path: str):
        """创建视频结果"""
        video = Video.fromFileSystem(file_path)
        return event.chain_result([video])

    def _image_result(self, event: AstrMessageEvent, file_path: str):
        """创建图片结果"""
        img = Image.fromFileSystem(file_path)
        return event.chain_result([img])

    def _images_result(self, event: AstrMessageEvent, file_paths: list):
        """创建多图片结果"""
        images = [Image.fromFileSystem(p) for p in file_paths]
        return event.chain_result(images)

    def _audio_result(self, event: AstrMessageEvent, file_path: str):
        """创建音频结果"""
        record = Record.fromFileSystem(file_path)
        return event.chain_result([record])

    async def _extract_url(self, text: str) -> str | None:
        """从消息文本中提取抖音链接"""
        for pattern in DOUYIN_PATTERNS:
            match = re.search(pattern, text)
            if match:
                return match.group(0)
        return None

    async def _resolve_short_url(self, session: requests.Session, url: str) -> str:
        """解析短链接，获取真实 URL"""
        if "v.douyin.com" not in url:
            return url

        # 方法1: GET 请求跟踪重定向（用移动UA，避免被封）
        mobile_ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
        try:
            resp = session.get(url, allow_redirects=True, timeout=15,
                               headers={'User-Agent': mobile_ua})
            resolved = resp.url
            logger.info(f"GET 解析: {url} -> {resolved} (status={resp.status_code})")

            if "v.douyin.com" not in resolved and "douyin.com" in resolved:
                return resolved
        except Exception as e:
            logger.warning(f"GET 请求失败: {e}")

        # 方法1b: 不跟踪重定向，从 Location 头提取
        try:
            resp = session.get(url, allow_redirects=False, timeout=10,
                               headers={'User-Agent': mobile_ua})
            location = resp.headers.get('Location', '')
            if location and 'douyin.com' in location:
                logger.info(f"从 Location 提取: {location[:100]}")
                return location
        except Exception as e:
            logger.warning(f"GET(no-redirect) 请求失败: {e}")

        # 方法2: 从响应体中提取 aweme_id
        try:
            aweme_patterns = [
                r'aweme_id=(\d+)',
                r'"awemeId"\s*:\s*"(\d+)"',
                r'/video/(\d{15,25})',
                r'/note/(\d{15,25})',
                r'itemId=(\d+)',
            ]
            for pattern in aweme_patterns:
                match = re.search(pattern, resp.text)
                if match:
                    aweme_id = match.group(1)
                    logger.info(f"从响应体提取到 aweme_id: {aweme_id}")
                    return f"https://www.douyin.com/video/{aweme_id}"
        except Exception:
            pass

        # 方法3: 从响应体中提取重定向URL
        try:
            href_patterns = [
                r'href="(https?://www\.douyin\.com/video/[^"]+)"',
                r'href="(https?://www\.douyin\.com/note/[^"]+)"',
                r'href="(https?://www\.iesdouyin\.com/[^"]+)"',
                r'window\.location\.href\s*=\s*["\']([^"\']+)["\']',
            ]
            for pattern in href_patterns:
                match = re.search(pattern, resp.text)
                if match:
                    logger.info(f"从响应体提取URL: {match.group(1)}")
                    return match.group(1)
        except Exception:
            pass

        logger.warning(f"短链接解析失败，使用原始URL: {url}")
        return url

    async def _extract_aweme_id(self, url: str) -> str | None:
        """从 URL 中提取 aweme_id"""
        if not url:
            return None

        patterns = [
            r'/video/(\d+)',
            r'/note/(\d+)',
            r'/share/video/(\d+)',
            r'/share/slides/(\d+)',
            r'aweme_id=(\d+)',
            r'itemId=(\d+)',
            r'awemeId=(\d+)',
            r'/(\d{15,25})(?:/|$|\?)',  # 兜底：URL路径中的15-25位数字
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                aweme_id = match.group(1)
                logger.info(f"提取到 aweme_id: {aweme_id} (pattern: {pattern})")
                return aweme_id

        logger.warning(f"无法从URL提取 aweme_id: {url}")
        return None

    def _pick_best_image_url(self, url_list: list) -> str:
        """从 url_list 中选择最佳图片URL（优先 jpeg 格式）"""
        if not url_list:
            return ''
        # 优先选 jpeg 格式（兼容性最好）
        for u in url_list:
            if '.jpeg' in u or '.jpg' in u:
                return self._clean_image_url(u)
        # 其次选非 webp
        for u in url_list:
            if '.webp' not in u:
                return self._clean_image_url(u)
        # 最后用第一个
        return self._clean_image_url(url_list[0])

    def _extract_music_info(self, aweme: dict) -> dict | None:
        """从 aweme 数据中提取音乐信息"""
        music = aweme.get('music', {})
        if not music:
            return None

        music_title = music.get('title', '')
        music_author = music.get('author', '')
        music_mid = music.get('mid', '')
        music_duration = music.get('duration', 0)

        # 方法1: 从 video.play_addr 中提取音频URL（图文作品的音乐在这里）
        video = aweme.get('video', {})
        play_addr = video.get('play_addr', {})
        url_list = play_addr.get('url_list', [])
        if url_list:
            raw_url = url_list[0]
            # 提取 video_id 参数中的真实音频URL
            vid_match = re.search(r'video_id=(https?://[^&]+\.mp3)', raw_url)
            if vid_match:
                music_url = vid_match.group(1)
                logger.info(f"从 video_id 提取音乐URL: {music_url[:80]}")
                return {
                    'url': music_url,
                    'title': music_title or '未知音乐',
                    'author': music_author or '未知作者',
                    'mid': music_mid,
                    'duration': music_duration,
                }
            # 如果没有 mp3，尝试用 play 替换 playwm
            if '/playwm/' in raw_url:
                music_url = raw_url.replace('/playwm/', '/play/')
                return {
                    'url': music_url,
                    'title': music_title or '未知音乐',
                    'author': music_author or '未知作者',
                    'mid': music_mid,
                    'duration': music_duration,
                }

        # 方法2: 从 music.play_url 获取
        play_url = music.get('play_url', {})
        if isinstance(play_url, dict):
            uri = play_url.get('uri', '')
            url_list = play_url.get('url_list', [])
            if url_list:
                return {
                    'url': url_list[0],
                    'title': music_title or '未知音乐',
                    'author': music_author or '未知作者',
                    'mid': music_mid,
                    'duration': music_duration,
                }
            if uri:
                return {
                    'url': f'https://aweme.snssdk.com/aweme/v1/play/?{uri}',
                    'title': music_title or '未知音乐',
                    'author': music_author or '未知作者',
                    'mid': music_mid,
                    'duration': music_duration,
                }
        elif isinstance(play_url, str) and play_url.startswith('http'):
            return {
                'url': play_url,
                'title': music_title or '未知音乐',
                'author': music_author or '未知作者',
                'mid': music_mid,
                'duration': music_duration,
            }

        logger.warning(f"无法提取音乐URL, mid={music_mid}")
        return None

    async def _extract_audio_from_video(self, video_path: str) -> str | None:
        """从视频文件中提取音频"""
        try:
            import subprocess
            audio_path = video_path.rsplit('.', 1)[0] + '.mp3'
            cmd = [
                'ffmpeg', '-y', '-i', video_path,
                '-vn', '-acodec', 'libmp3lame', '-q:a', '2',
                audio_path
            ]
            result = subprocess.run(cmd, capture_output=True, timeout=60)
            if result.returncode == 0 and os.path.exists(audio_path):
                logger.info(f"音频提取成功: {audio_path}")
                return audio_path
            else:
                logger.warning(f"音频提取失败: {result.stderr.decode()[:200]}")
                return None
        except FileNotFoundError:
            logger.warning("ffmpeg 未安装，无法提取音频")
            return None
        except Exception as e:
            logger.error(f"音频提取异常: {e}")
            return None

    def _clean_image_url(self, url: str) -> str:
        """清理图片URL，获取最高画质"""
        # 替换缩略图为原图
        for size in ['100x100', '200x200', '300x300', '400x400', '500x500',
                     '600x600', '700x700', '800x800', '900x900', '1000x1000',
                     '1200x1200', '1500x1500', '1800x1800', '2000x2000']:
            url = url.replace(f'/aweme/{size}/', '/aweme/')
        # 移除水印参数
        url = re.sub(r'&watermark=\d+', '', url)
        # 移除 noop image 后缀（保留原始图片）
        url = url.replace('~noop.image', '')
        # 移除裁剪参数
        url = re.sub(r'&crop=.*?(?=&|$)', '', url)
        return url

    def _parse_iesdouyin_page(self, html: str) -> dict | None:
        """解析 iesdouyin 分享页面，提取视频/图文信息"""
        try:
            # 提取 _ROUTER_DATA（使用括号计数法提取完整JSON）
            router_match = re.search(r'window\._ROUTER_DATA\s*=\s*\{', html)
            if not router_match:
                logger.warning("未找到 _ROUTER_DATA")
                return None

            start = router_match.end() - 1  # 指向 '{'
            bracket_count = 0
            end = start
            for i in range(start, min(start + 1000000, len(html))):
                if html[i] == '{':
                    bracket_count += 1
                elif html[i] == '}':
                    bracket_count -= 1
                    if bracket_count == 0:
                        end = i + 1
                        break
            raw = html[start:end]
            logger.info(f"_ROUTER_DATA 长度: {len(raw)}")
            raw = raw.encode('raw_unicode_escape').decode('unicode_escape')
            data = json.loads(raw)

            # 方法1: 直接从 item_list 提取（最可靠）
            aweme = None
            try:
                loader = data.get('loaderData', {})
                for key, val in loader.items():
                    if isinstance(val, dict) and 'videoInfoRes' in val:
                        item_list = val.get('videoInfoRes', {}).get('item_list', [])
                        if item_list:
                            aweme = item_list[0]
                            logger.info(f"从 item_list 提取到 aweme: {aweme.get('desc', '')[:30]}")
                            break
            except Exception as e:
                logger.warning(f"item_list 提取失败: {e}")

            # 方法2: 递归查找（备用）
            if not aweme:
                def find_aweme(obj, depth=0):
                    if depth > 6:
                        return None
                    if isinstance(obj, dict):
                        if 'aweme_type' in obj and ('desc' in obj or 'video' in obj):
                            return obj
                        for v in obj.values():
                            r = find_aweme(v, depth + 1)
                            if r:
                                return r
                    elif isinstance(obj, list):
                        for item in obj:
                            r = find_aweme(item, depth + 1)
                            if r:
                                return r
                    return None

                aweme = find_aweme(data)

            if not aweme:
                # 检查是否被过滤
                try:
                    for key, val in loader.items():
                        if isinstance(val, dict) and 'videoInfoRes' in val:
                            filter_list = val.get('videoInfoRes', {}).get('filter_list', [])
                            if filter_list:
                                reason = filter_list[0].get('filter_reason', 'unknown')
                                logger.warning(f"视频被过滤: {reason}")
                except Exception:
                    pass
                logger.warning("在 _ROUTER_DATA 中未找到 aweme 数据")
                return None

            desc = aweme.get('desc', '抖音作品')
            nickname = aweme.get('author', {}).get('nickname', '未知作者')
            aweme_type = aweme.get('aweme_type', 0)

            # 提取图片
            images = []
            for img in aweme.get('images', []):
                url_list = img.get('url_list', [])
                if url_list:
                    img_url = self._pick_best_image_url(url_list)
                    if img_url and len(img_url) > 30:
                        images.append(img_url)

            # 提取音乐信息
            music_info = self._extract_music_info(aweme)
            if music_info:
                logger.info(f"提取到音乐: {music_info['title'][:30]} - {music_info['author'][:20]}")

            logger.info(f"iesdouyin 解析: desc={desc[:30]}, aweme_type={aweme_type}, images={len(images)}, music={bool(music_info)}")

            # 判断类型：aweme_type 68=图文, 2=图集, 0=视频
            if images and (aweme_type in (68, 2, 101, 102, 103) or len(images) >= 2):
                result = {
                    'type': 'image',
                    'title': desc,
                    'author': nickname,
                    'images': images,
                }
                if music_info:
                    result['music'] = music_info
                return result

            # 提取视频
            video = aweme.get('video', {})
            play_addr = video.get('play_addr', {})
            url_list = play_addr.get('url_list', [])
            if url_list:
                video_url = url_list[0].replace('/playwm/', '/play/')
                # 检查是否是真正的视频（不是音频文件）
                if '.mp3' not in video_url and 'music' not in video_url:
                    result = {
                        'type': 'video',
                        'video_url': video_url,
                        'title': desc,
                        'author': nickname,
                        'width': video.get('width', 0),
                        'height': video.get('height', 0),
                        'duration': video.get('duration', 0) // 1000,
                    }
                    if music_info:
                        result['music'] = music_info
                    return result

            # 兜底：有图片就返回图片
            if images:
                result = {
                    'type': 'image',
                    'title': desc,
                    'author': nickname,
                    'images': images,
                }
                if music_info:
                    result['music'] = music_info
                return result

            return None
        except Exception as e:
            logger.error(f"解析 iesdouyin 页面失败: {e}", exc_info=True)
            return None

    async def _get_content_info(self, session: requests.Session, url: str, aweme_id: str = None, debug_info: list = None) -> dict | None:
        """从页面提取内容信息（视频或图文）"""
        def debug(msg):
            if debug_info is not None:
                debug_info.append(msg)
            logger.info(msg)

        try:
            # 使用分享页面提取数据（数据直接嵌入HTML，无需JS渲染）
            # m.douyin.com 对服务器IP不封禁，优先使用
            mobile_ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
            if aweme_id:
                debug(f"aweme_id={aweme_id}, len={len(aweme_id)}")
                share_urls = [
                    (f"https://m.douyin.com/share/video/{aweme_id}", mobile_ua),
                    (f"https://www.iesdouyin.com/share/video/{aweme_id}/", None),
                    (f"https://www.douyin.com/share/video/{aweme_id}", None),
                ]
                for share_url, ua in share_urls:
                    debug(f"请求: {share_url[:50]}")
                    try:
                        headers = {'User-Agent': ua} if ua else None
                        resp = session.get(share_url, timeout=15, headers=headers)
                        debug(f"响应: status={resp.status_code}, len={len(resp.text)}")
                    except Exception as e:
                        debug(f"请求异常: {type(e).__name__}")
                        continue

                    if resp.status_code == 200 and len(resp.text) > 10000:
                        result = self._parse_iesdouyin_page(resp.text)
                        if result:
                            return result
                        debug(f"解析返回None")
                    else:
                        debug(f"页面过短({len(resp.text)}B)，跳过")

            # 备用：请求原始页面
            debug(f"备用请求: {url[:60]}")
            resp = session.get(url, timeout=15)
            logger.info(f"原始页面响应: status={resp.status_code}, length={len(resp.text)}")
            resp.raise_for_status()

            # 提取标题
            title_match = re.search(r'"desc"\s*:\s*"([^"]{1,200})"', resp.text)
            title = title_match.group(1) if title_match else '抖音作品'

            # 提取作者
            author_match = re.search(r'"nickname"\s*:\s*"([^"]{1,50})"', resp.text)
            author = author_match.group(1) if author_match else '未知作者'

            # 提取 aweme_type
            type_match = re.search(r'"aweme_type"\s*:\s*(\d+)', resp.text)
            aweme_type = int(type_match.group(1)) if type_match else 0

            # 提取图片（优先级：图文视频 > 纯视频）
            images = []

            # 方法1: 从顶级 images 数组中提取（图文作品的主要来源）
            for images_match in re.finditer(r'"images"\s*:\s*\[', resp.text):
                start = images_match.end() - 1
                bracket_count = 0
                end = start
                for i in range(start, min(start + 500000, len(resp.text))):
                    if resp.text[i] == '[':
                        bracket_count += 1
                    elif resp.text[i] == ']':
                        bracket_count -= 1
                        if bracket_count == 0:
                            end = i + 1
                            break
                images_json = resp.text[start:end]
                url_pattern = r'"url_list"\s*:\s*\[\s*"(https?://[^"]*)"'
                for match in re.finditer(url_pattern, images_json):
                    try:
                        decoded_url = json.loads('"' + match.group(1) + '"')
                        decoded_url = self._clean_image_url(decoded_url)
                        if decoded_url not in images and len(decoded_url) > 30:
                            images.append(decoded_url)
                    except json.JSONDecodeError:
                        pass

            # 方法2: 从 image_list 数组中提取
            if len(images) < 2:
                for img_list_match in re.finditer(r'"image_list"\s*:\s*\[', resp.text):
                    start = img_list_match.end() - 1
                    bracket_count = 0
                    end = start
                    for i in range(start, min(start + 500000, len(resp.text))):
                        if resp.text[i] == '[':
                            bracket_count += 1
                        elif resp.text[i] == ']':
                            bracket_count -= 1
                            if bracket_count == 0:
                                end = i + 1
                                break
                    img_list_json = resp.text[start:end]
                    url_pattern = r'"url_list"\s*:\s*\[\s*"(https?://[^"]*)"'
                    for match in re.finditer(url_pattern, img_list_json):
                        try:
                            decoded_url = json.loads('"' + match.group(1) + '"')
                            decoded_url = self._clean_image_url(decoded_url)
                            if decoded_url not in images and len(decoded_url) > 30:
                                images.append(decoded_url)
                        except json.JSONDecodeError:
                            pass

            # 方法3: 从 video.images 中提取
            if len(images) < 2:
                video_images_pattern = r'"video"\s*:\s*\{[^}]*?"images"\s*:\s*\[(.*?)\]'
                video_images_match = re.search(video_images_pattern, resp.text, re.DOTALL)
                if video_images_match:
                    url_pattern = r'"url_list"\s*:\s*\[\s*"(https?://[^"]*)"'
                    for match in re.finditer(url_pattern, video_images_match.group(1)):
                        try:
                            decoded_url = json.loads('"' + match.group(1) + '"')
                            decoded_url = self._clean_image_url(decoded_url)
                            if decoded_url not in images and len(decoded_url) > 30:
                                images.append(decoded_url)
                        except json.JSONDecodeError:
                            pass

            # 方法4: 从 cover 和 origin_cover 中提取封面图
            cover_patterns = [
                r'"cover"\s*:\s*\{[^}]*?"url_list"\s*:\s*\[\s*"(https?://[^"]*)"',
                r'"origin_cover"\s*:\s*\{[^}]*?"url_list"\s*:\s*\[\s*"(https?://[^"]*)"',
                r'"dynamic_cover"\s*:\s*\{[^}]*?"url_list"\s*:\s*\[\s*"(https?://[^"]*)"',
            ]
            for pattern in cover_patterns:
                match = re.search(pattern, resp.text)
                if match:
                    try:
                        decoded_url = json.loads('"' + match.group(1) + '"')
                        decoded_url = self._clean_image_url(decoded_url)
                        if decoded_url not in images and len(decoded_url) > 30:
                            images.append(decoded_url)
                    except json.JSONDecodeError:
                        pass

            # 方法5: 搜索所有抖音CDN图片URL（兜底方案）
            if len(images) < 2:
                all_img_pattern = r'"(https?://[^"]*(?:douyinpic|byteimg)[^"]*(?:\.jpeg|\.jpg|\.png|\.webp|/obj/)[^"]*)"'
                all_img_urls = re.findall(all_img_pattern, resp.text, re.IGNORECASE)
                for img_url in all_img_urls:
                    try:
                        decoded_url = json.loads(img_url)
                        decoded_url = self._clean_image_url(decoded_url)
                        if decoded_url not in images and len(decoded_url) > 50:
                            images.append(decoded_url)
                    except json.JSONDecodeError:
                        pass

            # 方法6: 从 aweme/detail API 响应格式中提取
            if len(images) < 2:
                detail_pattern = r'"images"\s*:\s*\[\s*\{[^]]*?"url_list"\s*:\s*\[\s*"(https?://[^"]*)"'
                for match in re.finditer(detail_pattern, resp.text, re.DOTALL):
                    try:
                        decoded_url = json.loads('"' + match.group(1) + '"')
                        decoded_url = self._clean_image_url(decoded_url)
                        if decoded_url not in images and len(decoded_url) > 30:
                            images.append(decoded_url)
                    except json.JSONDecodeError:
                        pass

            # 去重
            seen = set()
            unique_images = []
            for img in images:
                if img not in seen:
                    seen.add(img)
                    unique_images.append(img)
            images = unique_images

            # aweme_type: 0=普通视频, 68=图文作品, 其他值也可能表示图文
            is_image_post = aweme_type in (68, 101, 102, 103) or len(images) >= 2
            has_play_addr = bool(re.search(r'"play_addr"\s*:\s*\{', resp.text))
            logger.info(f"提取到 {len(images)} 张图片，aweme_type={aweme_type}，is_image_post={is_image_post}，has_play_addr={has_play_addr}")
            for i, img_url in enumerate(images[:5]):
                logger.info(f"图片{i+1}: {img_url[:100]}...")

            # 调试：如果提取到的图片不足2张，保存页面快照用于分析
            if len(images) < 2:
                try:
                    debug_path = os.path.join(tempfile.gettempdir(), 'douyin_debug.html')
                    with open(debug_path, 'w', encoding='utf-8') as f:
                        f.write(resp.text)
                    logger.info(f"调试：页面已保存到 {debug_path}，长度 {len(resp.text)}")

                    # 打印页面中关键字段的存在情况
                    for field in ['images', 'image_list', 'image_post_info', 'slide_images', 'play_addr', 'aweme_type']:
                        count = resp.text.count(f'"{field}"')
                        logger.info(f"调试：字段 \"{field}\" 出现 {count} 次")
                except Exception as e:
                    logger.error(f"保存调试页面失败: {e}")

            # 判断逻辑：
            # 1. aweme_type 为图文类型 → 图文
            # 2. 提取到 >=2 张图片 → 图文（即使有 play_addr）
            # 3. 有图片但无 play_addr → 图文
            # 4. 否则 → 视频
            if images and (is_image_post or not has_play_addr):
                return {
                    'type': 'image',
                    'title': title,
                    'author': author,
                    'images': images,
                }

            # 尝试提取视频 URL
            video_pattern = r'"play_addr"\s*:\s*\{[^}]*"url_list"\s*:\s*\["([^"]+)"'
            video_matches = re.findall(video_pattern, resp.text)

            if video_matches:
                video_url = json.loads('"' + video_matches[0] + '"')
                video_url = video_url.replace('/playwm/', '/play/')

                width_match = re.search(r'"width"\s*:\s*(\d+)', resp.text)
                height_match = re.search(r'"height"\s*:\s*(\d+)', resp.text)
                width = int(width_match.group(1)) if width_match else 0
                height = int(height_match.group(1)) if height_match else 0

                duration_match = re.search(r'"duration"\s*:\s*(\d+)', resp.text)
                duration = int(duration_match.group(1)) // 1000 if duration_match else 0

                cover_url = images[0] if images else None

                return {
                    'type': 'video',
                    'video_url': video_url,
                    'title': title,
                    'author': author,
                    'width': width,
                    'height': height,
                    'duration': duration,
                    'cover': cover_url,
                }

            # 最后兜底：如果有图片就返回图片类型
            if images:
                return {
                    'type': 'image',
                    'title': title,
                    'author': author,
                    'images': images,
                }

            # 如果页面提取失败但有 aweme_id，尝试 API 接口
            if aweme_id:
                logger.info(f"页面提取失败，尝试 API 接口: aweme_id={aweme_id}")
                try:
                    api_url = f"https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id={aweme_id}&aid=1128&version_name=23.5.0"
                    api_resp = session.get(api_url, timeout=15)
                    if api_resp.status_code == 200:
                        data = api_resp.json()
                        aweme_detail = data.get('aweme_detail', {})
                        if aweme_detail:
                            # 从 API 响应中提取信息
                            desc = aweme_detail.get('desc', '抖音作品')
                            author_info = aweme_detail.get('author', {})
                            nickname = author_info.get('nickname', '未知作者')
                            aweme_type = aweme_detail.get('aweme_type', 0)

                            # 提取图片
                            images = []
                            for img in aweme_detail.get('images', []):
                                url_list = img.get('url_list', [])
                                if url_list:
                                    img_url = self._clean_image_url(url_list[0])
                                    if img_url and len(img_url) > 30:
                                        images.append(img_url)

                            if images:
                                logger.info(f"API 提取到 {len(images)} 张图片")
                                return {
                                    'type': 'image',
                                    'title': desc,
                                    'author': nickname,
                                    'images': images,
                                }

                            # 提取视频
                            video = aweme_detail.get('video', {})
                            play_addr = video.get('play_addr', {})
                            url_list = play_addr.get('url_list', [])
                            if url_list:
                                video_url = url_list[0].replace('/playwm/', '/play/')
                                return {
                                    'type': 'video',
                                    'video_url': video_url,
                                    'title': desc,
                                    'author': nickname,
                                    'width': video.get('width', 0),
                                    'height': video.get('height', 0),
                                    'duration': video.get('duration', 0) // 1000,
                                }
                except Exception as e:
                    logger.error(f"API 接口请求失败: {e}")

            debug(f"备用方法均失败: images={len(images)}")
            return None
        except Exception as e:
            debug(f"异常: {type(e).__name__}: {str(e)[:80]}")
            logger.error(f"获取内容信息失败: {e}", exc_info=True)
            return None

    def _safe_filename(self, title: str, max_len: int = 30) -> str:
        """生成安全的文件名（纯ASCII，避免CDN上传失败）"""
        timestamp = str(int(time.time() * 1000))[-8:]
        # 从标题中提取英文和数字作为前缀
        safe = re.sub(r'[^a-zA-Z0-9]', '', title)
        if safe:
            return f'{safe[:10]}_{timestamp}'
        return f'dy_{timestamp}'

    def _validate_video(self, file_path: str) -> bool:
        """验证视频文件是否有效"""
        try:
            with open(file_path, 'rb') as f:
                header = f.read(12)
                if len(header) < 12:
                    return False
                # MP4 文件在第4-8字节有 'ftyp' 标记
                if header[4:8] == b'ftyp':
                    return True
                # 也检查是否是 RIFF (WebM/MKV 等)
                if header[:4] == b'RIFF':
                    return True
                # 检查是否是 FLV
                if header[:3] == b'FLV':
                    return True
                logger.warning(f"视频文件头不符合预期: {header[:8].hex()}")
                return False
        except Exception as e:
            logger.error(f"验证视频文件失败: {e}")
            return False

    def _transcode_video(self, input_path: str) -> str | None:
        """转码视频为微信兼容格式 (H.264+AAC)"""
        try:
            import subprocess
            output_path = input_path.replace('.mp4', '_h264.mp4')
            cmd = [
                'ffmpeg', '-y', '-i', input_path,
                '-c:v', 'libx264', '-preset', 'fast',
                '-crf', '23', '-c:a', 'aac',
                '-movflags', '+faststart',
                output_path
            ]
            result = subprocess.run(cmd, capture_output=True, timeout=120)
            if result.returncode == 0 and os.path.exists(output_path):
                logger.info(f"视频转码成功: {output_path}")
                os.remove(input_path)
                return output_path
            else:
                logger.error(f"视频转码失败: {result.stderr.decode()[:200]}")
                return None
        except FileNotFoundError:
            logger.warning("ffmpeg 未安装，跳过视频转码")
            return None
        except Exception as e:
            logger.error(f"视频转码异常: {e}")
            return None

    async def _download_file(self, session: requests.Session, url: str, filename: str) -> str | None:
        """下载文件到临时目录"""
        try:
            tmp_dir = tempfile.mkdtemp()
            file_path = os.path.join(tmp_dir, filename)

            resp = session.get(url, timeout=60, stream=True)
            resp.raise_for_status()

            # 检查 Content-Type，确保是视频/图片
            content_type = resp.headers.get('Content-Type', '')
            logger.info(f"下载文件 Content-Type: {content_type}, URL: {url[:80]}...")

            file_size = 0
            with open(file_path, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
                    file_size += len(chunk)

            logger.info(f"文件下载完成: {file_path}, 大小: {file_size} bytes")

            if file_size < 1000:
                logger.error(f"文件过小 ({file_size} bytes)，可能下载失败")
                os.remove(file_path)
                os.rmdir(tmp_dir)
                return None

            return file_path
        except Exception as e:
            logger.error(f"下载文件失败: {e}")
            return None

    async def _download_images(self, session: requests.Session, image_urls: list, title: str) -> list:
        """下载多张图片"""
        safe_title = self._safe_filename(title, 20)
        if not safe_title:
            safe_title = 'douyin_image'

        downloaded = []
        for i, url in enumerate(image_urls):
            filename = f'{safe_title}_{i+1}.jpeg'
            file_path = await self._download_file(session, url, filename)
            if file_path and os.path.exists(file_path):
                downloaded.append(file_path)
        return downloaded

    async def _process_douyin_link(self, event: AstrMessageEvent):
        """处理抖音链接的核心逻辑"""
        message_text = event.message_str

        # 提取链接
        url = await self._extract_url(message_text)
        if not url:
            return

        yield self._text_result(event, "检测到抖音链接，正在解析...")

        # 创建 session
        session = requests.Session()
        if self.proxy:
            session.proxies = {'http': self.proxy, 'https': self.proxy}
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer': 'https://m.douyin.com/',
        })

        # 解析短链接
        real_url = await self._resolve_short_url(session, url)
        logger.info(f"解析后URL: {real_url}")

        # 提取 aweme_id
        aweme_id = await self._extract_aweme_id(real_url)
        if not aweme_id:
            yield self._text_result(event, "无法解析作品ID，请检查链接是否正确。")
            return

        logger.info(f"aweme_id: {aweme_id} (len={len(aweme_id)})")

        # 获取内容信息
        debug_info = [f"aweme_id={aweme_id}(len={len(aweme_id)})"]
        try:
            content_info = await self._get_content_info(session, real_url, aweme_id, debug_info)
        except Exception as e:
            logger.error(f"获取内容信息异常: {e}", exc_info=True)
            yield self._text_result(event, f"获取信息异常: {type(e).__name__}: {str(e)[:100]}")
            return

        if not content_info:
            debug_msg = " | ".join(debug_info) if debug_info else "无调试信息"
            yield self._text_result(event, f"获取作品信息失败。\n调试: {debug_msg}")
            return

        title = content_info.get('title', '抖音作品')
        author = content_info.get('author', '未知作者')

        # 根据类型处理
        music_info = content_info.get('music')
        if content_info['type'] == 'image':
            # 图文作品
            img_count = len(content_info['images'])
            has_music = bool(music_info)
            status_msg = f"正在下载 {img_count} 张图片"
            if has_music:
                status_msg += " + 背景音乐"
            status_msg += "..."
            yield self._text_result(event, status_msg)

            image_paths = await self._download_images(session, content_info['images'], title)

            if not image_paths:
                yield self._text_result(event, "图片下载失败，请稍后重试。")
                return

            caption = (
                f"下载完成！\n"
                f"类型: 图文作品\n"
                f"标题: {title[:50]}\n"
                f"作者: {author}\n"
                f"图片数量: {len(image_paths)}张"
            )
            if has_music:
                caption += f"\n音乐: {music_info['title'][:30]} - {music_info['author'][:20]}"
            yield self._text_result(event, caption)
            yield self._images_result(event, image_paths)

            # 下载并发送音乐
            if has_music:
                safe_title = self._safe_filename(title, 20)
                audio_path = await self._download_file(session, music_info['url'], f'{safe_title}.mp3')
                if audio_path and os.path.exists(audio_path):
                    audio_size = os.path.getsize(audio_path) / (1024 * 1024)
                    if audio_size < 50:
                        yield self._audio_result(event, audio_path)
                    else:
                        logger.warning(f"音频文件过大 ({audio_size:.1f}MB)，跳过发送")
                    try:
                        os.remove(audio_path)
                        os.rmdir(os.path.dirname(audio_path))
                    except OSError:
                        pass
                else:
                    logger.warning("音乐下载失败")

            # 清理临时文件
            for path in image_paths:
                try:
                    os.remove(path)
                    os.rmdir(os.path.dirname(path))
                except OSError:
                    pass

        else:
            # 视频作品
            yield self._text_result(event, "正在下载高清无水印视频...")

            safe_title = self._safe_filename(title, 20)
            video_url = content_info['video_url']

            # 尝试下载视频，先用无水印URL，失败则用带水印URL
            file_path = await self._download_file(session, video_url, f'{safe_title}.mp4')

            # 验证视频文件
            if file_path and os.path.exists(file_path):
                if not self._validate_video(file_path):
                    logger.warning(f"视频文件验证失败，尝试备用URL")
                    os.remove(file_path)
                    os.rmdir(os.path.dirname(file_path))
                    # 尝试带水印的URL
                    backup_url = video_url.replace('/play/', '/playwm/')
                    if backup_url != video_url:
                        file_path = await self._download_file(session, backup_url, f'{safe_title}.mp4')

            if not file_path or not os.path.exists(file_path):
                yield self._text_result(event, "视频下载失败，请稍后重试。")
                return

            # 尝试转码为微信兼容格式 (H.264+AAC)
            original_path = file_path
            transcoded_path = self._transcode_video(file_path)
            if transcoded_path:
                file_path = transcoded_path
            else:
                logger.info("转码跳过，使用原始视频文件")

            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            if file_size_mb > 100:
                yield self._text_result(event, f"视频文件过大 ({file_size_mb:.1f}MB)，超过发送限制。")
                os.remove(file_path)
                os.rmdir(os.path.dirname(file_path))
                return

            width = content_info.get('width', 0)
            height = content_info.get('height', 0)
            duration = content_info.get('duration', 0)
            resolution = f"{width}x{height}" if width else "未知"
            duration_str = f"{duration // 60}:{duration % 60:02d}" if duration else "未知"

            # 提取视频中的音频
            audio_path = await self._extract_audio_from_video(file_path)

            caption = (
                f"下载完成！\n"
                f"类型: 视频作品\n"
                f"标题: {title[:50]}\n"
                f"作者: {author}\n"
                f"分辨率: {resolution}\n"
                f"时长: {duration_str}\n"
                f"大小: {file_size_mb:.1f}MB"
            )
            if audio_path:
                caption += f"\n已提取背景音乐"
            yield self._text_result(event, caption)
            yield self._video_result(event, file_path)

            # 发送提取的音频
            if audio_path and os.path.exists(audio_path):
                audio_size = os.path.getsize(audio_path) / (1024 * 1024)
                if audio_size < 50:
                    yield self._audio_result(event, audio_path)
                try:
                    os.remove(audio_path)
                except OSError:
                    pass

            try:
                os.remove(file_path)
                os.rmdir(os.path.dirname(file_path))
            except OSError:
                pass

    @filter.command("douyin")
    async def handle_douyin(self, event: AstrMessageEvent):
        """命令模式：/douyin <链接>"""
        async for result in self._process_douyin_link(event):
            yield result

    @filter.regex(DOUYIN_REGEX)
    async def auto_detect(self, event: AstrMessageEvent):
        """自动检测模式：消息中包含抖音链接时自动处理"""
        async for result in self._process_douyin_link(event):
            yield result

    async def terminate(self):
        """插件卸载时的清理逻辑"""
        logger.info("DouyinDownloader 插件已卸载")
