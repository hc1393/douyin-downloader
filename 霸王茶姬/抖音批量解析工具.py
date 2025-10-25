import requests
import json
import base64
import random
import string
import re
import time
import csv
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


class BatchDouyinParser:
    def __init__(self, max_workers=3):
        self.session = requests.Session()
        self.global_session_token = None
        self.api_key = "dd87bbb8-6306-467e-8711-ff771a281020"
        self.base_url = "https://www.douyintool.com"
        self.max_workers = max_workers  # 最大并发数
        
        # 设置默认请求头
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-Ch-Ua": '"Chromium";v="141", "Microsoft Edge";v="141", "Not?A_Brand";v="8"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        })

    def generate_session_token(self):
        """
        生成会话令牌，对应JavaScript中的generateSessionToken函数
        """
        # 生成随机字符串，模拟 Math.random().toString(36).substring(2)
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        
        # 创建token数据
        token_data = {
            "randomString": random_string
        }
        
        # 转换为JSON并进行base64编码，对应 btoa(JSON.stringify(...))
        token_json = json.dumps(token_data, separators=(',', ':'))
        token = base64.b64encode(token_json.encode('utf-8')).decode('utf-8')
        
        return token

    def set_session_token(self):
        """
        设置会话令牌，对应JavaScript中的setSessionToken函数
        """
        if not self.global_session_token:
            self.global_session_token = self.generate_session_token()

    def get_session_token(self):
        """
        获取会话令牌，对应JavaScript中的getSessionToken函数
        """
        return self.global_session_token

    def extract_url(self, input_text):
        """
        从输入文本中提取URL，对应JavaScript中的URL提取逻辑
        """
        # 抖音和TikTok的URL正则表达式
        tiktok_pattern = r"https?:\/\/(?:www|m|vt|vm)?\.tiktok\.com\/(?:@[\w.-]+\/video\/\d+|[\w.-]+)"
        douyin_pattern = r"https?:\/\/(?:www\.)?douyin\.com\/(?:v|video)\/[\w.-]+"
        short_douyin_pattern = r"https?:\/\/v\.douyin\.com\/[\w.-]+"
        general_pattern = r"http[s]?:\/\/[\w.-]+[\w\/-]*[\w.-]*\??[\w=&:\-\+\%]*[/]*"
        
        # 综合正则表达式
        combined_pattern = f"({tiktok_pattern})|({douyin_pattern})|({short_douyin_pattern})"
        
        match = re.search(combined_pattern, input_text)
        if match:
            return match.group(0)
        else:
            # 尝试匹配一般的URL格式
            general_match = re.search(general_pattern, input_text)
            if general_match:
                return general_match.group(0)
        
        return None

    def parse_single_video(self, url, retry_count=3, delay=5):
        """
        解析单个视频，对应JavaScript中的setValue函数
        """
        print(f"开始解析URL: {url}")
        
        # 确保session token已设置
        self.set_session_token()
        session_token = self.get_session_token()
        
        # API端点
        api_url = f"{self.base_url}/api/video/share/url/parse"
        
        # 设置请求头
        headers = {
            "Content-Type": "application/json",
            "Origin": self.base_url,
            "X-Requested-By": "web",
            "Session-Token": session_token
        }
        
        # 请求数据
        payload = {
            "url": url,
            "key": self.api_key
        }
        
        # 重试机制
        for attempt in range(retry_count):
            try:
                response = self.session.post(api_url, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 200:
                    try:
                        result = response.json()
                        return {
                            "success": True,
                            "url": url,
                            "data": result
                        }
                    except json.JSONDecodeError as e:
                        return {
                            "success": False,
                            "url": url,
                            "error": f"JSON解析错误: {str(e)}",
                            "response_text": response.text
                        }
                elif response.status_code == 500:
                    if attempt < retry_count - 1:
                        time.sleep(delay)
                        delay *= 2  # 指数退避
                        continue
                    else:
                        return {
                            "success": False,
                            "url": url,
                            "error": "访问过于频繁，请稍后再试！"
                        }
                elif response.status_code == 400:
                    return {
                        "success": False,
                        "url": url,
                        "error": "请求参数错误，视频不存在或者链接不正确"
                    }
                else:
                    return {
                        "success": False,
                        "url": url,
                        "error": f"请求失败，状态码: {response.status_code}"
                    }
                    
            except requests.exceptions.Timeout:
                if attempt < retry_count - 1:
                    time.sleep(delay)
                    delay *= 2
                    continue
                else:
                    return {
                        "success": False,
                        "url": url,
                        "error": "请求超时，请检查网络连接！"
                    }
            except requests.exceptions.RequestException as e:
                return {
                    "success": False,
                    "url": url,
                    "error": f"网络请求错误: {str(e)}"
                }
        
        return {
            "success": False,
            "url": url,
            "error": "解析失败，请稍后再试！"
        }

    def parse_batch_videos(self, text_list, delay=2):
        """
        批量解析多个视频链接
        
        Args:
            text_list (list): 包含抖音链接的文本列表
            delay (int): 批量处理时的延迟时间（秒）
            
        Returns:
            list: 解析结果列表
        """
        results = []
        url_mapping = {}  # 文本到URL的映射
        
        # 第一步：提取所有URL
        print("正在提取URL...")
        for i, text in enumerate(text_list):
            url = self.extract_url(text)
            if url:
                url_mapping[text] = url
                print(f"文本 {i+1}: {url}")
            else:
                results.append({
                    "index": i,
                    "text": text,
                    "success": False,
                    "error": "未检测到有效链接"
                })
        
        # 第二步：并发解析URL
        print(f"\n开始批量解析 {len(url_mapping)} 个链接...")
        parsed_results = []
        
        # 使用线程池进行并发处理
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交任务
            future_to_text = {
                executor.submit(self.parse_single_video, url): (text, i) 
                for i, (text, url) in enumerate(url_mapping.items())
            }
            
            # 收集结果
            for future in as_completed(future_to_text):
                text, index = future_to_text[future]
                try:
                    result = future.result()
                    result["index"] = index
                    result["text"] = text
                    parsed_results.append(result)
                    
                    # 显示进度
                    status = "成功" if result["success"] else "失败"
                    print(f"解析进度: {len(parsed_results)}/{len(url_mapping)} - {status}")
                    
                    # 添加延迟避免请求过于频繁
                    time.sleep(delay)
                except Exception as e:
                    parsed_results.append({
                        "index": index,
                        "text": text,
                        "success": False,
                        "error": f"处理异常: {str(e)}"
                    })
        
        # 按原始顺序合并结果
        results.extend(parsed_results)
        results.sort(key=lambda x: x["index"])
        
        return results

    def format_single_result(self, result):
        """
        格式化单个结果
        """
        if not result["success"]:
            return f"解析失败: {result['error']}"
        
        data = result["data"]
        if data.get("code") == 200:
            video_data = data.get("data", {})
            title = video_data.get("title", "无标题")
            video_url = video_data.get("video_url", "")
            cover_url = video_data.get("cover_url", "")
            images = video_data.get("images", [])
            
            output = f"标题: {title}\n"
            if video_url:
                output += f"视频链接: {video_url}\n"
            if cover_url:
                output += f"封面链接: {cover_url}\n"
            if images:
                output += f"图片数量: {len(images)}\n"
                for i, img in enumerate(images[:5]):  # 只显示前5张
                    output += f"  图片{i+1}: {img}\n"
                if len(images) > 5:
                    output += f"  ...还有{len(images) - 5}张图片\n"
            
            return output
        else:
            return f"解析失败: {data.get('msg', '未知错误')}"

    def save_results_to_csv(self, results, filename=None):
        """
        将结果保存到CSV文件
        
        Args:
            results (list): 解析结果列表
            filename (str): 文件名，如果未提供则自动生成
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"douyin_parse_results_{timestamp}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['序号', '原始文本', '链接', '状态', '标题', '视频链接', '封面链接', '图片数量', '错误信息']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for i, result in enumerate(results):
                row = {
                    '序号': i + 1,
                    '原始文本': result.get('text', '')[:50] + '...' if len(result.get('text', '')) > 50 else result.get('text', ''),
                    '链接': result.get('url', ''),
                    '状态': '成功' if result.get('success', False) else '失败',
                    '标题': '',
                    '视频链接': '',
                    '封面链接': '',
                    '图片数量': 0,
                    '错误信息': result.get('error', '') if not result.get('success', False) else ''
                }
                
                if result.get('success', False) and 'data' in result:
                    data = result['data']
                    if data.get('code') == 200:
                        video_data = data.get('data', {})
                        row['标题'] = video_data.get('title', '')
                        row['视频链接'] = video_data.get('video_url', '')
                        row['封面链接'] = video_data.get('cover_url', '')
                        row['图片数量'] = len(video_data.get('images', []))
                
                writer.writerow(row)
        
        print(f"结果已保存到: {filename}")
        return filename

    def print_summary(self, results):
        """
        打印解析结果摘要
        
        Args:
            results (list): 解析结果列表
        """
        total = len(results)
        success_count = sum(1 for r in results if r.get('success', False))
        fail_count = total - success_count
        
        print("\n" + "="*50)
        print("解析结果摘要")
        print("="*50)
        print(f"总计: {total}")
        print(f"成功: {success_count}")
        print(f"失败: {fail_count}")
        print(f"成功率: {success_count/total*100:.2f}%" if total > 0 else "成功率: 0%")
        
        if fail_count > 0:
            print("\n失败详情:")
            for result in results:
                if not result.get('success', False):
                    print(f"  - {result.get('text', '')[:50]}...: {result.get('error', '未知错误')}")


def main():
    # 创建解析器实例
    parser = BatchDouyinParser(max_workers=2)  # 限制并发数避免被封
    
    # 测试用的输入文本列表
    test_inputs = [
        "9.97 12/09 reO:/ B@T.LJ 前方核能！这才是这个世界的巅峰战斗！！！ # MAD # AMV # 动漫 # 动漫混剪 # 超燃混剪  https://v.douyin.com/9_IYxChPu_c/ 复制此链接，打开Dou音搜索，直接观看视频！",
        "复制打开抖音，看看【动画锦集的作品】超燃混剪，这才是男人该看的动漫！  https://v.douyin.com/iJFmSeUr/ 复制此链接，打开Dou音搜索，直接观看视频！",
        "这个动漫太燃了！# 动漫推荐 # 超燃 # 二次元  https://v.douyin.com/abcdefg/ 复制此链接，打开Dou音搜索，直接观看视频！",
        "没有链接的文本内容，应该会解析失败"
    ]
    
    print("抖音批量视频解析工具")
    print("=" * 50)
    print(f"待处理文本数量: {len(test_inputs)}")
    for i, text in enumerate(test_inputs):
        print(f"{i+1}. {text[:100]}{'...' if len(text) > 100 else ''}")
    
    # 批量解析
    print("\n开始批量解析...")
    results = parser.parse_batch_videos(test_inputs, delay=1)
    
    # 显示详细结果
    print("\n详细解析结果:")
    print("=" * 50)
    for i, result in enumerate(results):
        print(f"\n{i+1}. 原始文本: {result.get('text', '')[:100]}{'...' if len(result.get('text', '')) > 100 else ''}")
        formatted_result = parser.format_single_result(result)
        print(formatted_result)
    
    # 打印摘要
    parser.print_summary(results)
    
    # 保存结果到CSV
    csv_file = parser.save_results_to_csv(results)
    print(f"\n详细结果已保存到CSV文件: {csv_file}")


if __name__ == "__main__":
    main()