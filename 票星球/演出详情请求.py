import requests
import json

def fetch_show_detail():
    url = "https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v5/show/68d20e539dd9b800014fed0a/static"
    
    params = {
        "lang": "zh",
        "terminalSrc": "WEB",
        "utcOffset": "480",
        "ver": "4.45.3",
        "src": "WEB",
        "cityId": "BL1034",
        "source": "FROM_QUICK_ORDER",
        "siteId": "6268b17853245f055f21d677"
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

# 执行请求并打印结果
if __name__ == "__main__":
    result = fetch_show_detail()
    print(json.dumps(result, ensure_ascii=False, indent=2))