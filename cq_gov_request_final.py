import requests

def get_cq_gov_page():
    """
    将JavaScript fetch请求转换为Python requests请求（最终版，解决编码问题）
    原始fetch请求: https://rlsbj.cq.gov.cn/ztzl/zqs2020ndkslygwyzl/gwyks2026/202601/t20260121_15341242.html
    """
    url = "https://rlsbj.cq.gov.cn/ztzl/zqs2020ndkslygwyzl/gwyks2026/202601/t20260121_15341242.html"
    
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
    }
    
    # 创建session对象
    session = requests.Session()
    
    # 设置referrer
    headers["Referer"] = "https://cn.bing.com/"
    
    try:
        # 发送GET请求
        response = session.get(
            url,
            headers=headers,
            timeout=30  # 添加超时设置
        )
        
        # 关键：强制指定响应内容的编码
        response.encoding = 'utf-8'
        
        # 检查响应状态
        if response.status_code == 200:
            print("请求成功!")
            print("响应状态码:", response.status_code)
            
            # 尝试用不同编码写入文件
            try:
                # 先尝试直接写入
                with open('cq_gov_page_correct.html', 'w', encoding='utf-8') as f:
                    f.write(response.text)
                print("内容已保存到 cq_gov_page_correct.html 文件中")
            except UnicodeEncodeError:
                # 如果仍有编码问题，使用errors='ignore'参数
                with open('cq_gov_page_correct.html', 'w', encoding='utf-8', errors='ignore') as f:
                    f.write(response.text)
                print("内容已保存到 cq_gov_page_correct.html 文件中（忽略编码错误）")
            
            # 查找并打印标题
            import re
            title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE | re.DOTALL)
            if title_match:
                title = title_match.group(1).strip()
                print(f"页面标题: {title}")
            else:
                print("未找到页面标题")
            
            # 找到meta标签中的关键信息
            site_name_match = re.search(r'<meta name="SiteName" content="(.*?)"', response.text)
            if site_name_match:
                site_name = site_name_match.group(1)
                print(f"站点名称: {site_name}")
            
            article_title_match = re.search(r'<meta name="ArticleTitle" content="(.*?)"', response.text)
            if article_title_match:
                article_title = article_title_match.group(1)
                print(f"文章标题: {article_title}")
                
            print(f"响应内容长度: {len(response.text)} 字符")
            print("响应内容前500字符预览:")
            print(response.text[:500])
            
            return response.text
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return None
            
    except UnicodeDecodeError as e:
        print(f"编码错误: {e}")
        # 尝试使用二进制方式获取并手动解码
        response = session.get(url, headers=headers, timeout=30)
        try:
            # 尝试用gbk解码
            content = response.content.decode('gbk')
            print("使用GBK编码成功解码")
            with open('cq_gov_page_gbk.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("内容已保存到 cq_gov_page_gbk.html 文件中")
            return content
        except UnicodeDecodeError:
            print("无法解码响应内容")
            return None
    except Exception as e:
        print(f"请求过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    result = get_cq_gov_page()