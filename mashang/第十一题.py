import requests
import hashlib
import execjs
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def get_url1(k):
    with open('第十一题加密.js', 'r', encoding='utf-8') as f:
        j = f.read()
        ctx = execjs.compile(j)
        result = ctx.call('get_time', k)
    return result
def get_url(page):
    # 生成t参数
    base_url = "https://www.mashangpa.com/api/problem-detail/11/data/?page=" + str(page)
    t_parameter = get_url1(page)  # 您需要根据实际逻辑调整
    url_with_params = f"{base_url}&m={t_parameter[0]}&_ts={t_parameter[1]}"
    print(f"Processing page {page}: {url_with_params}")
    # 其余代码保持不变
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "Referer": "https://www.mashangpa.com/problem-detail/11/",
        'cookie': "sessionid=cd7bpf1lcsory0s5xqlskkjamip1garj; Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1762677936,1763178489,1763181639,1763181899; HMACCOUNT=81475DFC18DA7E74; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1763184423"
    }
    try:
        response = requests.get(url_with_params, headers=headers, timeout=10)
        return page, response.json()
    except Exception as e:
        print(f"Error processing page {page}: {e}")
        return page, None


def submit_answer(answer):
    """
    提交答案到服务器
    """
    url = "https://www.mashangpa.com/problem/11/submit/"
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryBPLSPmif7przmXRE",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrftoken": "p84Z0i3BUPbEZPr3yFUeGmSOGmYDzLzBAIMRPRLYWcKfVA3dRzusZbmZ9zj5x37n",
        "Referer": "https://www.mashangpa.com/problem-detail/10/",
        'cookie': "sessionid=cd7bpf1lcsory0s5xqlskkjamip1garj; Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1762677936,1763178489,1763181639,1763181899; HMACCOUNT=81475DFC18DA7E74; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1763184423"

    }

    body = (
        "------WebKitFormBoundaryBPLSPmif7przmXRE\r\n"
        "Content-Disposition: form-data; name=\"csrfmiddlewaretoken\"\r\n\r\n"
        "p84Z0i3BUPbEZPr3yFUeGmSOGmYDzLzBAIMRPRLYWcKfVA3dRzusZbmZ9zj5x37n\r\n"
        "------WebKitFormBoundaryBPLSPmif7przmXRE\r\n"
        f"Content-Disposition: form-data; name=\"user_answer\"\r\n\r\n"
        f"{int(answer)}\r\n"
        "------WebKitFormBoundaryBPLSPmif7przmXRE--\r\n"
    )

    try:
        response = requests.post(url, headers=headers, data=body, timeout=10)
        return response.json()
    except Exception as e:
        print(f"提交答案时出错: {e}")
        return None


def ss():
    total = 0
    page_data = {}

    # Use ThreadPoolExecutor to fetch data concurrently
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Submit all tasks
        future_to_page = {executor.submit(get_url, i): i for i in range(1, 21)}

        # Process completed tasks
        for future in as_completed(future_to_page):
            page, data = future.result()
            if data and "current_array" in data:
                page_data[page] = data
                page_sum = sum(float(x) for x in data["current_array"])
                print(f"第 {page} 页数据: {data['current_array']} | 本页合计: {page_sum}")
            elif data:
                print(f"Page {page} returned unexpected data: {data}")
            else:
                print(f"Failed to get data for page {page}")

    # Calculate total in order
    for i in range(1, 21):
        if i in page_data:
            data = page_data[i]
            try:
                page_sum = sum(float(x) for x in data["current_array"])
                total += page_sum
                print(f"当前累计值: {total}")
            except (KeyError, ValueError, TypeError) as e:
                print(f"Error processing page {i} data: {e}")

    return total


if __name__ == "__main__":
    start_time = time.time()
    result = ss()
    end_time = time.time()
    print(f"最终结果: {result}")
    print(f"耗时: {end_time - start_time:.2f} 秒")

    # 提交答案
    print("正在提交答案...")
    submit_result = submit_answer(result)
    if submit_result:
        print(f"提交结果: {submit_result}")
    else:
        print("提交失败")