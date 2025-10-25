import requests
import json
import csv

def fetch_cities():
    url = "https://m.piaoxingqiu.com/cyy_gatewayapi/home/pub/v3/citys"
    
    params = {
        "lang": "zh",
        "terminalSrc": "WEB",
        "utcOffset": "480",
        "ver": "4.45.3",
        "src": "WEB"
    }
    
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "access-token": "eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkE1LxDAURf_LW3fxkr58dJYjIwqKIMosJUlTKHaakqbgOMx_NzEwS92-e-658C6wnte70HvYcWxgW318nIcAuwvY8bsGcP_w9PEMDayb3d-OkktlNHrfc6YFcaXlwKijzOXmexH1BSNFLXbWWcEZR0SmnRa_2Cm5_zBeba9hypPzNk3XBhYT05jGMJdazlP49HOV6MHyjhCHVmFfJMxxoUyVvCw-mhT-3Gsz6qI3yb-NpzzJlGRtR5yQCZYfEF3uHg_7MnteCtCA_1oqSBol4fUHAAD__w.B0kt3RKBDSLKG_b1jfVTXrwh4Nw4i3Pi1JkHBE8VO_mmN7epR8p_3RzFOaSBv-ZcssNrhcQlgfExiWbTx1HD-MCpCNxOyDd1DiDhDkiOG1Il9ZfoGipRWr6j0GMGXnhAOuJPHBindVg9wHa68Cw_biPD3U2kgMuafiR1vLHD_TM",
        "angry-dog": "41gkqjPgPBO9eDrvV4Cl3-7UNwP6er0fTzjnNjBBQJhczlFMZXBgbk1GF9Xzsf-FUxePhwxI9FgyfY-i1d9e4QYJ3ul61j3y_h8jnffXVlvQVcFWIH4vFgYSVIWldeJbYUZUMW1aQXlnUWROYWNOOQ.WyIxLjAuMCIsIldFQiJd",
        "cache-control": "no-cache",
        "front-trace-id": "mh6fpp3rgos9biahfe",
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

def extract_city_data(response_data):
    """
    从响应数据中提取城市信息：
    cityId, bsCityId, cityName, provinceId, provinceName, 
    spelling, status, siteId, countryId, countryName
    """
    extracted_data = []
    
    # 获取城市数据列表
    if isinstance(response_data, dict):
        data_section = response_data.get('data', {})
        all_cities = data_section.get('allCities', [])
        
        # 遍历所有城市分组
        for city_group in all_cities:
            if isinstance(city_group, dict):
                cities = city_group.get('cities', [])
                # 遍历每个城市并提取所需字段
                for city in cities:
                    if isinstance(city, dict):
                        city_info = {
                            'cityId': city.get('cityId'),
                            'bsCityId': city.get('bsCityId'),
                            'cityName': city.get('cityName'),
                            'provinceId': city.get('provinceId'),
                            'provinceName': city.get('provinceName'),
                            'spelling': city.get('spelling'),
                            'status': city.get('status'),
                            'siteId': city.get('siteId'),
                            'countryId': city.get('countryId'),
                            'countryName': city.get('countryName')
                        }
                        extracted_data.append(city_info)
    
    return extracted_data

def save_to_csv(data, filename='城市数据.csv'):
    """
    将城市数据保存到CSV文件中
    """
    if not data:
        print("没有数据可保存")
        return
    
    # 定义表头
    fieldnames = ['cityId', 'bsCityId', 'cityName', 'provinceId', 'provinceName', 
                  'spelling', 'status', 'siteId', 'countryId', 'countryName']
    
    # 写入CSV文件
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"数据已保存到 {filename}")

# 执行请求并处理结果
if __name__ == "__main__":
    result = fetch_cities()
    print("原始响应数据:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 提取指定字段
    extracted_data = extract_city_data(result)
    print("\n提取后的数据:")
    print(json.dumps(extracted_data, ensure_ascii=False, indent=2))
    
    # 保存到CSV文件
    save_to_csv(extracted_data)