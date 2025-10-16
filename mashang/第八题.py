import requests
import json
import execjs
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import time


def get_url(k):
    with open('第八题.js', 'r', encoding='utf-8') as f:
        j = f.read()
        ctx = execjs.compile(j)
        result = ctx.call('get_m_t', k)
    return result


def get_content(token, page):
    url = "https://www.mashangpa.com/api/problem-detail/8/data/"

    payload = {
        "page": page
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/json",
        'pragma': "no-cache",
        'cache-control': "no-cache",
        'sec-ch-ua-platform': "\"Windows\"",
        'sec-ch-ua': "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
        'sec-ch-ua-mobile': "?0",
        'm': token[0],
        'x-requested-with': "XMLHttpRequest",
        't': token[1],
        'origin': "https://www.mashangpa.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.mashangpa.com/problem-detail/8/",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        'priority': "u=1, i",
        'Cookie': "sessionid=3aqg7x6jxhww1c9z8lkqz071glt3iodr; Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1760452447,1760530880,1760576639,1760610634; HMACCOUNT=81475DFC18DA7E74; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1760612672; s=51b351b351b351b370b0905090703050d0f0b0907"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # 确保返回JSON数据
    try:
        data = response.json()
        print(f"第 {page} 页响应: {data}")
        return data, page
    except json.JSONDecodeError:
        print(f"第 {page} 页响应不是有效的JSON: {response.text}")
        return None, page


def process_page(page):
    """处理单个页面的函数，供多线程调用"""
    token = get_url(page)
    data, page_num = get_content(token, page)
    return data, page_num


def ss():
    total = 0
    page_data = {}  # 用于存储每页数据
    lock = Lock()  # 用于保护共享资源

    # 使用线程池，限制并发数为2避免触发反爬机制
    with ThreadPoolExecutor(max_workers=2) as executor:
        # 提交所有任务
        future_to_page = {executor.submit(process_page, i): i for i in range(1, 21)}

        # 获取结果
        for future in as_completed(future_to_page):
            data, page = future.result()

            # 线程安全地更新总值和页面数据
            with lock:
                # 检查数据是否有效
                if data is not None and "current_array" in data:
                    page_sum = sum(float(x) for x in data["current_array"])
                    page_data[page] = page_sum
                    print(f"第 {page} 页数据: {data['current_array']} | 本页合计: {page_sum}")
                else:
                    page_data[page] = 0
                    print(f"第 {page} 页数据获取失败或格式不正确")

    # 按页码顺序计算总和
    for page in sorted(page_data.keys()):
        total += page_data[page]
        print(f"第 {page} 页合计: {page_data[page]} | 当前累计值: {total}")

    return total


if __name__ == "__main__":
    result = ss()
    print(f"最终结果: {result}")