import requests
import json

def load_page(page_number):
    """
    获取第十七题指定页面的数据
    
    Args:
        page_number (int): 页码
        
    Returns:
        dict: 返回API响应数据
    """
    url = f"https://mashangpa.com/api/problem-detail/17/data/?page={page_number}"
    
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 如果状态码不是200会抛出异常
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f'Error fetching problem details: {e}')
        return None
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON response: {e}')
        return None

def update_counter(data):
    """
    处理从API获取的数据
    这是一个示例函数，你需要根据实际需求实现
    
    Args:
        data (dict): 从API获取的数据
    """
    # 示例处理逻辑
    if data:
        print("Received data:", data)
        # 在这里添加你实际需要处理数据的逻辑
    else:
        print("No data received")

if __name__ == "__main__":
    # 调用示例
    result = load_page(1)
    update_counter(result)
    print(result)