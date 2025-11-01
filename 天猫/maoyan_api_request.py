import requests
import json

def search_maoyan_movies(keyword, offset=0, limit=10):
    """
    搜索猫眼电影信息
    
    Args:
        keyword (str): 搜索关键词
        offset (int): 偏移量，默认为0
        limit (int): 返回结果数量，默认为10
    
    Returns:
        dict: API响应结果
    """
    
    # API URL和参数
    url = "https://api.maoyan.com/mmdb/search/integrated/keyword/v1/list.json"
    
    params = {
        "token": "MY_Vb1-yqe9tFrH_vis6inwq8hLbrEAAAAwxd8MD4JLmeGWHXZt-zchIqk4etm0oZSmmk9pEx7EXyhKqeYI0uBkPMGT4OyZ1AxiAAAAvwAAAAEB",
        "keyword": keyword,
        "offset": offset,
        "stype": '[{"type":6}]',
        "iscorrected": "false",
        "ci": 45,
        "gCi": 45,
        "lng": 106.55072784423828,
        "lat": 29.56471061706543,
        "channelId": 70001,
        "almtype": -1,
        "limit": limit,
        "sellChannel": 7,
        "yodaReady": "wx",
        "csecappid": "wxdbb4c5f1b8ee7da1",
        "csecplatform": 3,
        "csecversionname": "wallet-v6.11.11",
        "csecversion": "1.4.0"
    }
    
    # 请求头
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "multipart/form-data",
        "csecuuid": "2d0615bde920cdd3e4185844e85ffbc2",
        "mtgsig": "{\"a1\":\"1.2\",\"a2\":1761747228111,\"a3\":\"9132vwyz4wv958v3040x19wvwz459y9880z7486xzwx97978z1yww4yw\",\"a4\":\"67ec30de707e3470de30ec6770347e701165bd576151c327\",\"a5\":\"yr+anC08GYWILpgO1nt3HVxQ+bD1QfELlEYK+SaUb2q/QgkeyUYb6mdFKxA3e+MnWv/XxkDkoSrEAMozTViGkEJVIrmI0TsIzfkuSkmlMATva78Nr3Briu+5QFjc6cGm9SHaXqFpaWdowsY/nXcDTh7vo0/HXLhNMd+ygaaJdMGu1kaXkBnpN38FVCtJkSA0Txxo8Rq8P2/d16b98uVTuotwhomHL3utuuGC087Nt/6r38V/JCGQEK4tKSqMAfJ8p3vP8JzpVGoIIvml\",\"a6\":\"w1.31fTi61fwxUgCIg5sB2ZiwbSyuDGnWGffpWADVaHQxLGrkfAJPpycll1JXpCdb3lL7sKj2944xC7/6ST9eSzG9s+NMv74zEfZ19Lo9Lfn5gEXfEC8A+WdJ5VnV6x4i9ic50/JYizi14Ko1d91Sm05MZHaiL+J1EfoRSjiW3qkBp1btm4YvLvFswuqBRAchNjWaiy3VdZRz8GaQe05RvOXjqqLxwDlrAtfOFgdN8o6s7l7tmqybmz11Xk1CDPBkPNy+8dSoy0206+Fx/tm4dGxbihWAEQ/ehhbPv/Kayr97JKdAUf4BHH2ZVHKjZnuytitNsNslWil8ni/74zXKv/xB7ltNaiWQXGubXNuKWKlpU+lqP/CFUkXJGe8ESoq8pI8xU875uGTK5z/Pjg3rVp1yvS5snC4qH93q0Aq1otL3wfMVh7ZrBniaSDauD3+3xkwEr4dZl8sTlJutZM8P1W8YPLQ12xeCOXnxJyQ3lBMY6zxIuwDL4vw8gGDVvgJW4z1\",\"a7\":\"wxdbb4c5f1b8ee7da1\",\"x0\":3,\"d1\":\"7cab1f37d4b5671cdf3faf9286d7caa2\"}",
        "openid": "o31Py0Ip12yvw0x5P8iLwuLdhBfI",
        "openidcipher": "AwQAAABJAgAAAAEAAAAyAAAAPLgC95WH3MyqngAoyM/hf1hEoKrGdo0pJ5DI44e1wGF9AT3PH7Wes03actC2n/GVnwfURonD78PewMUppAAAADilSXi4ZWAnGp+4SDNlV5Wdt1nFy8HEXs4OP1Q3njlckuHZJgfY7GXdpvW8fCrS1DUhQf45Ouvyaw==",
        "openidsec": "GeYSTGhsJADI9yGFQa4Jhia3w+hrxtJ1O/5sq5wFa9U=",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "uuid": "2d0615bde920cdd3e4185844e85ffbc2",
        "x-channel-id": "70001",
        "x-requested-with": "wxapp",
        "x-wxa-page": "pages/show/search/index",
        "x-wxa-query": "{}",
        "x-wxa-referer": "pages/show/list/index",
        "xweb_xhr": "1"
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # 如果响应状态码不是200会抛出异常
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None

def extract_movie_info(data):
    """
    从API响应中提取电影信息
    
    Args:
        data (dict): API响应数据
    
    Returns:
        list: 电影信息列表
    """
    if not data or 'data' not in data:
        return []
    
    movies = []
    # 根据API响应结构调整解析方式
    if 'list' in data['data']:
        for item in data['data']['list']:
            movie_info = {
                'id': item.get('id', ''),
                'name': item.get('name', ''),
                'score': item.get('score', ''),
                'img': item.get('img', ''),
            }
            movies.append(movie_info)
    
    return movies

if __name__ == "__main__":
    # 搜索示例
    keyword = "邓紫棋"
    print(f"正在搜索: {keyword}")
    
    result = search_maoyan_movies(keyword)
    
    if result:
        print("搜索成功，结果如下:")
        movies = extract_movie_info(result)
        if movies:
            for movie in movies:
                print(f"- {movie['name']} (ID: {movie['id']}) 评分: {movie['score']}")
        else:
            print("未找到相关电影信息")
            # 打印原始响应以便调试
            print("原始响应:", json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("搜索失败")