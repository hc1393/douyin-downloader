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
from astrbot.core.message.components import Video, Image

logger = logging.getLogger(__name__)

# 抖音链接正则（合并为一个模式用于自动检测）
DOUYIN_REGEX = r'(?:https?://v\.douyin\.com/\S+|https?://www\.douyin\.com/(?:video|note)/\d+\S*|https?://www\.iesdouyin\.com/share/video/\d+\S*)'

# 用于提取 URL 的模式列表
DOUYIN_PATTERNS = [
    r'https?://v\.douyin\.com/\S+',
    r'https?://www\.douyin\.com/video/\d+',
    r'https?://www\.douyin\.com/note/\d+',
    r'https?://www\.iesdouyin\.com/share/video/\d+',
]


class DouyinDownloader(Star):
    def __init__(self, context: Context, config: dict = None):
        super().__init__(context, config)
        logger.info("DouyinDownloader 插件已加载")

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

    async def _extract_url(self, text: str) -> str | None:
        """从消息文本中提取抖音链接"""
        for pattern in DOUYIN_PATTERNS:
            match = re.search(pattern, text)
            if match:
                return match.group(0)
        return None

    async def _resolve_short_url(self, session: requests.Session, url: str) -> str:
        """解析短链接，获取真实 URL"""
        if "v.douyin.com" in url:
            try:
                resp = session.head(url, allow_redirects=True, timeout=10)
                return resp.url
            except Exception as e:
                logger.warning(f"解析短链接失败: {e}，使用原始链接")
        return url

    async def _extract_aweme_id(self, url: str) -> str | None:
        """从 URL 中提取 aweme_id"""
        match = re.search(r'/video/(\d+)', url)
        if match:
            return match.group(1)

        match = re.search(r'/note/(\d+)', url)
        if match:
            return match.group(1)

        match = re.search(r'/share/video/(\d+)', url)
        if match:
            return match.group(1)

        match = re.search(r'aweme_id=(\d+)', url)
        if match:
            return match.group(1)

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

    async def _get_content_info(self, session: requests.Session, url: str) -> dict | None:
        """从页面提取内容信息（视频或图文）"""
        try:
            resp = session.get(url, timeout=15)
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
            # 使用递归括号匹配找到完整的 images JSON 数组
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
                # 提取每个图片对象中的 url_list
                url_pattern = r'"url_list"\s*:\s*\[\s*"(https?://[^"]*)"'
                for match in re.finditer(url_pattern, images_json):
                    try:
                        decoded_url = json.loads('"' + match.group(1) + '"')
                        decoded_url = self._clean_image_url(decoded_url)
                        if decoded_url not in images and len(decoded_url) > 30:
                            images.append(decoded_url)
                    except json.JSONDecodeError:
                        pass

            # 方法2: 从 video.images 中提取（图文视频的备用来源）
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

            # 方法3: 从 cover 和 origin_cover 中提取封面图
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

            # 方法4: 搜索所有抖音CDN图片URL（更宽松的兜底方案）
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

            # 方法5: 从 aweme/detail API 响应格式中提取
            if len(images) < 2:
                # 尝试匹配 JSON 嵌套的 images 数组
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
            logger.info(f"提取到 {len(images)} 张图片，aweme_type={aweme_type}，is_image_post={is_image_post}")
            for i, img_url in enumerate(images[:5]):
                logger.debug(f"图片{i+1}: {img_url[:100]}...")

            # 如果是图文作品且有图片，返回图片类型
            if images and (is_image_post or not re.search(r'"play_addr"\s*:\s*\{', resp.text)):
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

                # 即使是视频，也检查是否有单张图片（可能是封面）
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

            return None
        except Exception as e:
            logger.error(f"获取内容信息失败: {e}")
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
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Pixel 4 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://www.douyin.com/',
        })

        # 解析短链接
        real_url = await self._resolve_short_url(session, url)
        logger.info(f"解析后URL: {real_url}")

        # 提取 aweme_id
        aweme_id = await self._extract_aweme_id(real_url)
        if not aweme_id:
            yield self._text_result(event, "无法解析作品ID，请检查链接是否正确。")
            return

        logger.info(f"aweme_id: {aweme_id}")

        # 获取内容信息
        content_info = await self._get_content_info(session, real_url)
        if not content_info:
            yield self._text_result(event, "获取作品信息失败，请稍后重试。")
            return

        title = content_info.get('title', '抖音作品')
        author = content_info.get('author', '未知作者')

        # 根据类型处理
        if content_info['type'] == 'image':
            # 图文作品
            yield self._text_result(event, f"正在下载 {len(content_info['images'])} 张图片...")

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
            yield self._text_result(event, caption)
            yield self._images_result(event, image_paths)

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

            caption = (
                f"下载完成！\n"
                f"类型: 视频作品\n"
                f"标题: {title[:50]}\n"
                f"作者: {author}\n"
                f"分辨率: {resolution}\n"
                f"时长: {duration_str}\n"
                f"大小: {file_size_mb:.1f}MB"
            )
            yield self._text_result(event, caption)
            yield self._video_result(event, file_path)

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
