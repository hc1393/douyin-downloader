import requests
import json
import execjs
import base64
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_url():
    with open('第九题加密.js', 'r', encoding='utf-8') as f:
        j = f.read()
        ctx = execjs.compile(j)
        result = ctx.call('get_m')
    return result

def send_request(page=3):
    # 获取加密参数
    m, tt = get_url()
    
    # 请求体
    body = {
        "page": page,
        "m": m,
        "tt": tt
    }
    
    # 请求头
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "cookie": "sessionid=cd7bpf1lcsory0s5xqlskkjamip1garj; Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1760610634,1760617987,1762526975,1762677936; HMACCOUNT=81475DFC18DA7E74; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1762678017"
    }
    
    # 发送POST请求
    response = requests.post(
        url="https://www.mashangpa.com/api/problem-detail/9/data/",
        headers=headers,
        json=body
    )
    
    return response

def get_current_array_sum(page=3):
    try:
        # 获取响应数据
        response = send_request(page)
        
        # 检查响应状态
        if response.status_code != 200:
            print(f"页面 {page} 请求失败，状态码: {response.status_code}")
            return [], 0, page
            
        # 解析JSON
        data = response.json()
        
        # 检查响应是否包含错误信息
        if "current_array" not in data:
            print(f"页面 {page} 响应不包含 current_array: {data}")
            return [], 0, page
            
        # 提取current_array并计算总和（转换为int）
        current_array = data['current_array']
        
        # 检查数组元素是否为数字
        try:
            # 确保所有元素都是整数
            current_array = [int(x) for x in current_array]
            total = sum(current_array)
        except ValueError as e:
            print(f"页面 {page} 数据转换错误: {e}, 原始数据: {current_array}")
            return [], 0, page
        
        return current_array, total, page
    except Exception as e:
        print(f"页面 {page} 处理异常: {e}")
        return [], 0, page

# 遍历所有页面（1-20页）使用多线程
def get_all_page_sum_multithreaded(max_workers=5):
    total = 0
    page_results = {}
    
    # 创建线程池
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        future_to_page = {executor.submit(get_current_array_sum, i): i for i in range(1, 21)}
        
        # 获取结果
        for future in as_completed(future_to_page):
            try:
                current_array, page_sum, page_num = future.result()
                page_results[page_num] = (current_array, page_sum)
            except Exception as exc:
                page_num = future_to_page[future]
                print(f'页面 {page_num} 产生异常: {exc}')
                # 出错时使用默认值
                page_results[page_num] = ([], 0)
    
    # 按页码顺序输出结果并计算总和
    for i in range(1, 21):
        current_array, page_sum = page_results[i]
        print(f"第 {i} 页数据: {current_array} | 本页合计: {page_sum}")
        total += page_sum
        print(f"当前累计值: {total}")
        
    return total

# 测试单个页面
def test_single_page(page=1):
    current_array, total, page_num = get_current_array_sum(page)
    print(f"第 {page_num} 页数据: {current_array} | 本页合计: {total}")

# 示例调用
if __name__ == "__main__":
    # 测试单个页面
    # test_single_page(1)
    
    total_sum = get_all_page_sum_multithreaded()
    print(f"所有页面总和: {total_sum}")