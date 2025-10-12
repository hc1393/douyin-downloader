import time
import datetime
import execjs
import requests

import re
from datetime import datetime


def detect_timestamps(html_content):
    """检测HTML中可能的时间戳值"""
    results = []
    # 检测10位数字（经典Unix时间戳）
    ten_digits = re.findall(r'\b\d{10}\b', html_content)
    for ts in set(ten_digits):  # 去重
        try:
            ts_int = int(ts)
            year = datetime.fromtimestamp(ts_int).year
            if 1970 <= year <= 2100:  # 合理范围
                results.append({
                    'value': ts_int,
                    'type': 'unix_seconds',
                    'position': '10位数字'
                })
        except:
            pass

    # 检测13位数字（JavaScript时间戳-毫秒）
    thirteen_digits = re.findall(r'\b\d{13}\b', html_content)
    for ts in set(thirteen_digits):
        try:
            ts_int = int(ts) // 1000  # 转换为秒
            year = datetime.fromtimestamp(ts_int).year
            if 1970 <= year <= 2100:
                results.append({
                    'value': ts_int,
                    'type': 'js_milliseconds',
                    'position': '13位数字'
                })
        except:
            pass

    # 检测常见变量名
    var_names = ['time_unix', 'TimeUnix', 'timeStamp', 'timestamp', 'exp', 'iat']
    for var in var_names:
        pattern = re.compile(f'var\\s+{var}\\s*=\\s*(\\d+)\\s*;')
        match = pattern.search(html_content)
        if match:
            ts = match.group(1)
            try:
                ts_int = int(ts)
                year = datetime.fromtimestamp(ts_int).year
                if 1970 <= year <= 2100:
                    results.append({
                        'value': ts_int,
                        'type': f'var_{var}',
                        'position': '变量定义'
                    })
            except:
                pass

    # 排序并去重
    unique_results = {result['value']: result for result in results}.values()
    return sorted(unique_results, key=lambda x: x['value'], reverse=True)


def get_calibrated_time(time_unix_server):
    """模拟JavaScript的校准时间逻辑"""
    # 模拟JavaScript中的TimeUnixBD
    time_unix_bd = int(round(time.time()))  # 当前客户端时间(秒级)

    # 计算时间差（客户端与服务器时间差）
    time_unix_diff = time_unix_bd - time_unix_server
    print('时间差：'+ str(time_unix_diff))
    current_unix = int(round(time.time()))  # 当前时间
    return current_unix - time_unix_diff  # 校准后的服务器时间

def diaoyong():
    url='https://www.acgice.com/sjz/v/keys?t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTI5NjEsIm5hbWUiOiI1MDkwMzFBMzZDQUExRkY1MUU1QUUzNzdGODg4QTA5OCIsImdyb3VwX2lkIjoxLCJwYXJlbnRfaWQiOjAsInR5cGUiOiIiLCJjcmVhdGVfdGltZSI6IjIwMjUtMDktMTRUMTM6MTM6MjguNTIyNjAxNjE5KzA4OjAwIiwiZXhwIjoxNzU3ODYyODA4fQ.nyECeZydboLUccDj1QuIU7um6Zxb-DIwht1JGvuw3so'
    # 使用示例
    html_content = requests.get(url).text
    timestamps = detect_timestamps(html_content)
    for ts in timestamps:
        # 提取服务器TimeUnix值
        time_unix_server = ts['value']

        if not time_unix_server:
            print("未能从HTML中提取TimeUnix值")
            return
        # 创建校准时间函数
        get_calibrated_time_func = get_calibrated_time(time_unix_server)
        return get_calibrated_time_func



def get_url(k):
    with open('crypto-js.min.js','r',encoding='utf-8') as f:
        j = f.read()
        ctx=execjs.compile(j)
        result = ctx.call('diao1',str(k-3))
        return result

def qing():
    k = diaoyong()
    print(k,type(k))
    url = get_url(k)
    print(url)
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "referer": "https://www.acgice.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
    }

    # 发送请求
    response = requests.get(
        url,
        headers=headers,
        timeout=10  # 设置10秒超时
    )

    # 处理响应
    if response.status_code == 200:
        try:
            data = response.json()
            print("请求成功，返回数据:")
            print(data)
        except Exception as e:
            print("JSON解析失败:", e)
            print("原始响应:", response.text)
    else:
        print(f"请求失败，状态码: {response.status_code}")
        print("错误详情:", response.text)

print(qing())

# https://api.acgice.com/api/sjz/item_list?a=&top=1-2&p=1&mid=0&n=&token=e5613dd40cfe69294755b89d63660a62&timestamp=1757589028
# https://api.acgice.com/api/sjz/item_list?a=&top=1-2&p=1&mid=0&n=&token=9ced1bccb379cf4925f081c83cd49e6e&timestamp=1757590101