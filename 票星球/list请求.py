import requests
import json
import time
import execjs
from datetime import datetime
import csv
# 将JavaScript的fetch请求转换为Python requests

def get_url(time):
  with open('加密参数.js', 'r', encoding='utf-8') as f:
    j = f.read()
    ctx = execjs.compile(j)
    result = ctx.call('JO',time)
  return result
def get_cookie(time):
  with open('加密参数.js', 'r', encoding='utf-8') as f:
    j = f.read()
    ctx = execjs.compile(j)
    result = ctx.call('get_cookie_tex',time)
  return result


def fetch_request(cityid):
    time = int(datetime.now().timestamp()*1000)
    fronttraceid=get_url(time)
    cookie=get_cookie(time)
    url = "https://m.piaoxingqiu.com/cyy_gatewayapi/home/pub/v3/show_list/search_by_front"

    # params = {
    #     "cityId": "BL1034",
    #     "ifComponent": "0",
    #     "lang": "zh",
    #     "length": "10",
    #     "offset": "0",
    #     "pageType": "ALL_PAGE",
    #     "sortType": "RECOMMEND",
    #     "terminalSrc": "WEB",
    #     "utcOffset": "480",
    #     "ver": "4.45.1",
    #     "src": "WEB"
    # }
    params = {
        "cityId":cityid,
        "lang": "zh",
        "length": "10",
        "offset": "0",
        "pageIndex": "0",
        "pageLength": "10",
        "pageType": "ALL_PAGE",
        "terminalSrc": "WEB",
        "utcOffset": "480",
        "ver": "4.45.3",
        "src": "WEB"
    }

    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "access-token": "",
        "cache-control": "no-cache",
        "front-trace-id": fronttraceid,
        'cookie':cookie,
        "pragma": "no-cache",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "src": "WEB",
        "terminal-src": "WEB",
        "utc-offset": "480",
        "ver": "4.45.1"
    }

    # 发送GET请求
    response = requests.get(url, params=params, headers=headers)
    return response.json()

def extract_show_data(response_data):
    """
    从响应数据中提取指定字段：
    showName, showId, stdShowId, showDate, cityName, venueId, 
    firstShowTime, lastShowTime, latestShowTime
    """
    extracted_data = []
    
    # 获取搜索数据列表
    search_data = response_data.get('data', {}).get('searchData', [])
    print(search_data)
    # 遍历每个演出项目并提取所需字段
    for item in search_data:
        show_info = {
            'showName': item.get('showName'),
            'showId': item.get('showId'),
            'stdShowId': item.get('stdShowId'),
            'showDate': item.get('showDate'),
            'cityName': item.get('cityName'),
            'venueId': item.get('venueId'),
            'firstShowTime': item.get('firstShowTime'),
            'lastShowTime': item.get('lastShowTime'),
            'latestShowTime': item.get('latestShowTime')
        }
        extracted_data.append(show_info)
    return extracted_data

def save_to_csv(data, filename='演出数据.csv'):
    """
    将数据保存到CSV文件中
    """
    if not data:
        print("没有数据可保存")
        return
    
    # 定义表头
    fieldnames = ['showName', 'showId', 'stdShowId', 'showDate', 'cityName', 
                  'venueId', 'firstShowTime', 'lastShowTime', 'latestShowTime']
    
    # 写入CSV文件
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"数据已保存到 {filename}")


def fetch_show_detail(cityid,showid,siteid):
    url = 'https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v5/show/'+showid+'/static'

    params = {
        "lang": "zh",
        "terminalSrc": "WEB",
        "utcOffset": "480",
        "ver": "4.45.3",
        "src": "WEB",
        "cityId": cityid,
        "source": "FROM_QUICK_ORDER",
        "siteId": siteid
    }

    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "access-token": "eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkE1LxDAURf_LW3fxkr58dJYjIwqKIMosJUlTKHaakqbgOMx_NzEwS92-e-658C6wnte70HvYcWxgW318nIcAuwvY8bsGcP_w9PEMDayb3d-OkktlNHrfc6YFcaXlwKijzOXmexH1BSNFLXbWWcEZR0SmnRa_2Cm5_zBeba9hypPzNk3XBhYT05jGMJdazlP49HOV6MHyjhCHVmFfJMxxoUyVvCw-mhT-3Gsz6qI3yb-NpzzJlGRtR5yQCZYfEF3uHg_7MnteCtCA_1oqSBol4fUHAAD__w.B0kt3RKBDSLKG_b1jfVTXrwh4Nw4i3Pi1JkHBE8VO_mmN7epR8p_3RzFOaSBv-ZcssNrhcQlgfExiWbTx1HD-MCpCNxOyDd1DiDhDkiOG1Il9ZfoGipRWr6j0GMGXnhAOuJPHBindVg9wHa68Cw_biPD3U2kgMuafiR1vLHD_TM",
        "angry-dog": "XfMaanV2lDr07s5j_tlWOLxe8XBTuuav_aAja31PVpXbLegQfjjjys0Xi8KEd_1pAMX1ERmkvlv8cw2uK2FzlAw5BnlfXKiAc0leclVVKNDQ4L19U1pAgf10UiHML9ahc25ZOWhVNU9iUGVWd2dVYg.WyIxLjAuMCIsIldFQiJd",
        "cache-control": "no-cache",
        "front-trace-id": "mh6eee1g0pvsdggsfax",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "src": "WEB",
        "terminal-src": "WEB",
        "utc-offset": "480",
        "ver": "4.45.3"
    }

    # 发送GET请求
    response = requests.get(url, params=params, headers=headers)

    # 返回JSON响应
    return response.json()

def load_cities_from_csv(filename='城市数据.csv'):
    """
    从CSV文件中加载城市数据
    """
    cities = []
    try:
        with open(filename, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cities.append({
                    'cityId': row['cityId'],
                    'siteId': row['siteId']
                })
    except FileNotFoundError:
        print(f"未找到文件 {filename}，请先运行城市列表请求.py 生成城市数据")
    return cities

def load_shows_from_csv(filename='演出数据.csv'):
    """
    从CSV文件中加载演出数据
    """
    shows = []
    try:
        with open(filename, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                shows.append({
                    'showId': row['showId'],
                    'showName': row['showName']
                })
    except FileNotFoundError:
        print(f"未找到文件 {filename}，请先获取演出数据")
    return shows

if __name__ == "__main__":
    # 从城市数据CSV文件中读取城市信息
    cities = load_cities_from_csv()
    if not cities:
        print("请先运行城市列表请求.py生成城市数据文件")
        exit()
    
    # 使用第一个城市进行演示
    city = cities[0]
    cityid = city['cityId']
    siteid = city['siteId']
    
    print(f"使用城市ID: {cityid}, 站点ID: {siteid}")
    
    # 获取原始响应数据
    response_data = fetch_request(cityid)
    # 提取指定字段
    extracted_data = extract_show_data(response_data)
    print("\n提取后的数据:")
    print(json.dumps(extracted_data, ensure_ascii=False, indent=2))

    # 保存到CSV文件
    save_to_csv(extracted_data)
    
    # 如果有演出数据，则获取第一个演出的详细信息
    if extracted_data:
        show = extracted_data[0]
        showid = show['showId']
        show_name = show['showName']
        print(f"\n获取演出 '{show_name}' 的详细信息...")
        
        # 获取演出详细信息
        detail_data = fetch_show_detail(cityid, showid, siteid)
        print("演出详细信息:")
        print(json.dumps(detail_data, ensure_ascii=False, indent=2))