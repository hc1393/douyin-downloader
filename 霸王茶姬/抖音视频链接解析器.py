import requests
import json
import base64
import random
import string
import re
import time
import argparse
import sys
from urllib.parse import urlparse


class DouyinVideoLinkParser:
    def __init__(self):
        self.session = requests.Session()
        self.global_session_token = None
        self.api_key = "dd87bbb8-6306-467e-8711-ff771a281020"
        self.base_url = "https://www.douyintool.com"
        
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
        生成会话令牌
        """
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        token_data = {
            "randomString": random_string
        }
        token_json = json.dumps(token_data, separators=(',', ':'))
        token = base64.b64encode(token_json.encode('utf-8')).decode('utf-8')
        return token

    def set_session_token(self):
        """
        设置会话令牌
        """
        if not self.global_session_token:
            self.global_session_token = self.generate_session_token()

    def get_session_token(self):
        """
        获取会话令牌
        """
        return self.global_session_token

    def extract_url(self, input_text):
        """
        从输入文本中提取URL
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
            general_match = re.search(general_pattern, input_text)
            if general_match:
                return general_match.group(0)
        
        return None

    def parse_video(self, url, retry_count=3, delay=5):
        """
        解析视频获取下载链接
        """
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
                            "data": result
                        }
                    except json.JSONDecodeError as e:
                        return {
                            "success": False,
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
                            "error": "访问过于频繁，请稍后再试！"
                        }
                elif response.status_code == 400:
                    return {
                        "success": False,
                        "error": "请求参数错误，视频不存在或者链接不正确"
                    }
                else:
                    return {
                        "success": False,
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
                        "error": "请求超时，请检查网络连接！"
                    }
            except requests.exceptions.RequestException as e:
                return {
                    "success": False,
                    "error": f"网络请求错误: {str(e)}"
                }
        
        return {
            "success": False,
            "error": "解析失败，请稍后再试！"
        }

    def extract_download_links(self, result):
        """
        从解析结果中提取下载链接
        """
        if not result["success"]:
            return {
                "success": False,
                "error": result.get("error", "解析失败")
            }
        
        data = result["data"]
        if data.get("code") == 200:
            video_data = data.get("data", {})
            title = video_data.get("title", "无标题")
            video_url = video_data.get("video_url", "")
            cover_url = video_data.get("cover_url", "")
            images = video_data.get("images", [])
            
            links = {
                "title": title,
                "video_download_link": video_url,
                "cover_download_link": cover_url,
                "image_links": images
            }
            
            return {
                "success": True,
                "links": links
            }
        else:
            return {
                "success": False,
                "error": data.get("msg", "解析失败")
            }

    def process_single_text(self, text):
        """
        处理单个文本
        """
        # 提取URL
        url = self.extract_url(text)
        if not url:
            return {
                "success": False,
                "error": "未检测到有效链接"
            }
        
        # 解析视频
        parse_result = self.parse_video(url)
        if not parse_result["success"]:
            return parse_result
        
        # 提取下载链接
        links_result = self.extract_download_links(parse_result)
        return links_result

    def process_multiple_texts(self, text_list):
        """
        处理多个文本
        """
        results = []
        for i, text in enumerate(text_list):
            print(f"处理第 {i+1}/{len(text_list)} 个链接...")
            result = self.process_single_text(text)
            result["index"] = i
            result["text"] = text
            results.append(result)
            # 添加延迟避免请求过于频繁
            time.sleep(1)
        return results

    def print_result(self, result):
        """
        打印结果
        """
        if result["success"]:
            links = result["links"]
            print(f"标题: {links['title']}")
            if links['video_download_link']:
                print(f"视频下载链接: {links['video_download_link']}")
            if links['cover_download_link']:
                print(f"封面下载链接: {links['cover_download_link']}")
            if links['image_links']:
                print(f"图片数量: {len(links['image_links'])}")
                for i, img_link in enumerate(links['image_links']):
                    print(f"  图片{i+1}: {img_link}")
        else:
            print(f"解析失败: {result['error']}")

    def save_results(self, results, filename):
        """
        保存结果到文件
        """
        with open(filename, 'w', encoding='utf-8') as f:
            for result in results:
                if result["success"]:
                    links = result["links"]
                    f.write(f"原文本: {result.get('text', '')}\n")
                    f.write(f"标题: {links['title']}\n")
                    if links['video_download_link']:
                        f.write(f"视频下载链接: {links['video_download_link']}\n")
                    if links['cover_download_link']:
                        f.write(f"封面下载链接: {links['cover_download_link']}\n")
                    if links['image_links']:
                        f.write(f"图片链接:\n")
                        for img_link in links['image_links']:
                            f.write(f"  {img_link}\n")
                    f.write("\n")
                else:
                    f.write(f"原文本: {result.get('text', '')}\n")
                    f.write(f"解析失败: {result['error']}\n\n")
        print(f"结果已保存到: {filename}")


def main():
    parser = argparse.ArgumentParser(description='抖音视频链接解析器')
    parser.add_argument('-t', '--text', help='包含抖音链接的文本')
    parser.add_argument('-f', '--file', help='包含多个抖音链接文本的文件路径')
    parser.add_argument('-o', '--output', help='输出文件路径')
    
    args = parser.parse_args()
    
    # 创建解析器实例
    link_parser = DouyinVideoLinkParser()
    
    if args.text:
        # 处理单个文本
        print("处理单个文本...")
        result = link_parser.process_single_text(args.text)
        link_parser.print_result(result)
        
        # 如果指定了输出文件，则保存结果
        if args.output:
            link_parser.save_results([result], args.output)
            
    elif args.file:
        # 处理文件中的多个文本
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
            
            print(f"从文件中读取到 {len(lines)} 个文本，开始处理...")
            results = link_parser.process_multiple_texts(lines)
            
            # 打印结果
            for i, result in enumerate(results):
                print(f"\n{i+1}.")
                link_parser.print_result(result)
            
            # 如果指定了输出文件，则保存结果
            if args.output:
                link_parser.save_results(results, args.output)
                
        except FileNotFoundError:
            print(f"错误: 找不到文件 {args.file}")
        except Exception as e:
            print(f"处理文件时出错: {e}")
    else:
        # 交互式模式
        print("抖音视频链接解析器")
        print("=" * 50)
        print("请输入包含抖音链接的文本 (输入 'quit' 退出):")
        
        texts = []
        while True:
            text = input("> ")
            if text.lower() == 'quit':
                break
            if text.strip():
                texts.append(text.strip())
                if len(texts) >= 10:  # 限制最多处理10个
                    print("已达到最大处理数量 (10)")
                    break
        
        if texts:
            print(f"\n开始处理 {len(texts)} 个文本...")
            results = link_parser.process_multiple_texts(texts)
            
            # 打印结果
            for i, result in enumerate(results):
                print(f"\n{i+1}.")
                link_parser.print_result(result)
            
            # 询问是否保存结果
            save_choice = input("\n是否保存结果到文件? (y/n): ")
            if save_choice.lower() == 'y':
                filename = input("请输入文件名 (默认: douyin_links.txt): ").strip()
                if not filename:
                    filename = "douyin_links.txt"
                link_parser.save_results(results, filename)


if __name__ == "__main__":
    main()