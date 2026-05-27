import requests
import chardet

def get_cq_gov_page():
    """
    将JavaScript fetch请求转换为Python requests请求
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
            # credentials: "include" 对应 requests 的默认行为，cookies会自动包含
        )
        
        # 手动检测内容编码
        detected_encoding = chardet.detect(response.content)
        print("检测到的内容编码:", detected_encoding)
        
        # 使用检测到的编码解码内容
        decoded_content = response.content.decode(detected_encoding['encoding'])
        
        # 检查响应状态
        if response.status_code == 200:
            print("请求成功!")
            print("响应状态码:", response.status_code)
            print("响应内容长度:", len(decoded_content))
            print("检测到的编码:", detected_encoding['encoding'])
            
            # 写入文件以便查看内容
            with open('cq_gov_page.html', 'w', encoding='utf-8') as f:
                f.write(decoded_content)
            print("内容已保存到 cq_gov_page.html 文件中")
            
            print("响应内容预览:", decoded_content[:500])
            return decoded_content
        else:
            print(f"请求失败，状态码: {response.status_code}")
            print("响应内容:", decoded_content)
            return None
            
    except Exception as e:
        print(f"请求过程中发生错误: {e}")
        return None

if __name__ == "__main__":
    result = get_cq_gov_page()