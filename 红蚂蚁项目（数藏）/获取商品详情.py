import requests
import json

def get_market_goods_detail(token, goods_id, goods_type):
    """
    获取市场商品详情
    
    Args:
        token (str): 用户身份验证令牌
        goods_id (str): 商品ID
        goods_type (str): 商品类型
    
    Returns:
        dict: 商品详情数据
    """
    url = "https://api.hyart.art/api/market/market/marketGoodsDetail"
    
    payload = {
        "id": goods_id,
        "type": goods_type
    }
    headers = {
        'accept': "*/*",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        'cache-control': "no-cache",
        'content-type': "application/json",
        'pragma': "no-cache",
        'sec-ch-ua': '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-site",
        'token': token,
        'referrer': "https://hyart.art/"
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"获取商品详情失败: {e}")
        return None

def main():
    # 示例用法
    # 注意：这里需要替换为有效的token
    token = "b6bd8053-0ad4-4114-be17-4c96474811d9"
    goods_id = "2"
    goods_type = "2"
    
    result = get_market_goods_detail(token, goods_id, goods_type)
    if result:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("获取商品详情失败")

if __name__ == "__main__":
    main()