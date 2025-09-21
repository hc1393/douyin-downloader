import requests
import time
import random


def fetch_page_data(session, page):
    url = f"https://www.mashangpa.com/api/problem-detail/3/data/?page={page}"
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "referer": "https://www.mashangpa.com/problem-detail/3/",
        "Cookie":'sessionid=bv2oh8xoizs69iwxq8n3tdn8cr8oxu90; Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1757430160,1757483015,1758277021; HMACCOUNT=1846E94D0D2F249B; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1758278085'
    }

    try:
        # 增加请求头真实性
        headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br",
        })

        response = session.get(url, headers=headers)
        response.raise_for_status()  # 检查HTTP错误

        # 检查是否是JSON响应
        if 'application/json' not in response.headers.get('Content-Type', ''):
            print(f"第 {page} 页返回非JSON内容: {response.text[:100]}...")
            return 0

        data = response.json()

        # 调试输出：打印API响应结构
        if page == 1:  # 仅在第一页时打印调试信息
            print("API响应结构示例:")
            print(data)

        # 确保数据结构正确
        if "current_array" not in data:
            print(f"第 {page} 页响应缺少current_array字段")
            return 0

        # 确保所有元素都是数字
        try:
            # 尝试转换为浮点数再求和
            page_sum = sum(float(x) for x in data["current_array"])
            print(f"第 {page} 页数据: {data['current_array']} | 本页合计: {page_sum}")
            return page_sum
        except ValueError:
            # 如果无法转换为数字，打印错误
            print(f"第 {page} 页数据包含非数字值: {data['current_array']}")
            print("尝试仅处理数字元素...")

            # 安全处理：过滤掉非数字元素
            numbers = []
            for x in data["current_array"]:
                try:
                    numbers.append(float(x))
                except (TypeError, ValueError):
                    pass

            if not numbers:
                print(f"第 {page} 页无有效数字数据")
                return 0

            page_sum = sum(numbers)
            print(f"有效数据: {numbers} | 本页合计: {page_sum}")
            return page_sum

    except requests.exceptions.RequestException as e:
        print(f"请求第 {page} 页失败: {str(e)}")
        return 0
    except (KeyError, TypeError) as e:
        print(f"JSON解析错误: {str(e)}")
        print(f"响应内容: {response.text[:200]}...")
        return 0


def main():
    print("开始获取数据...")

    # 创建共享会话
    session = requests.Session()

    # 预请求获取必要cookies
    print("预请求获取cookies...")
    try:
        homepage = "https://www.mashangpa.com/problem-detail/3/"
        session.get(homepage, timeout=10, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        })
    except Exception as e:
        print(f"预请求失败: {e}，继续执行")

    total = 0
    for page in range(1, 21):
        print(f"\n正在获取第 {page} 页数据...")
        page_sum = fetch_page_data(session, page)
        total += page_sum
        print(f"当前累计值: {total}")

        # 随机延时避免请求频率过高 (2-5秒)
        if page < 10:
            delay = random.uniform(2.0, 5.0)
            print(f"等待 {delay:.2f} 秒后继续...")
            time.sleep(delay)

    print(f"\n所有页面数据合计总和: {total}")


if __name__ == "__main__":
    main()
