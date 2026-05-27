import requests

def get_cq_gov_page():
    """
    将JavaScript fetch请求转换为Python requests请求（简化版）
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
        "upgrade-insecure-requests": "1"
    }
    
    # 设置referrer
    referrer = "https://cn.bing.com/"
    headers["Referer"] = referrer
    
    try:
        # 发送GET请求
        response = requests.get(
            url,
            headers=headers,
        )
        
        # 尝试使用不同的编码方式
        try:
            # 首先尝试直接使用content进行解码
            content = response.content.decode('utf-8')
        except UnicodeDecodeError:
            try:
                # 如果utf-8失败，则尝试gbk编码
                content = response.content.decode('gbk')
            except UnicodeDecodeError:
                # 最后尝试gb2312编码
                content = response.content.decode('gb2312')
        
        # 检查响应状态
        if response.status_code == 200:
            print("请求成功!")
            print("响应状态码:", response.status_code)
            
            # 写入文件以便查看内容
            with open('cq_gov_page.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("内容已保存到 cq_gov_page.html 文件中")
            
            # 输出部分内容进行预览
            lines = content.split('\n')
            print("HTML标题行:")
            for line in lines[:50]:  # 检查前50行寻找标题
                if '<title>' in line:
                    print(line.strip())
                    break
            
            print("\nHTML内容前几行预览:")
            for i, line in enumerate(lines[:20]):
                if line.strip():  # 只打印非空行
                    print(f"{i+1:2d}: {line.strip()}")
            
            return content
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"请求过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    result = get_cq_gov_page()