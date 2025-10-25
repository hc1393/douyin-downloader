import requests
import json

def fetch_seat_plans():
    url = "https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v3/show/68d12cfd9dd9b800014fe03d/show_session/68d12cfd9dd9b800014fe049/seat_plans_from_marketing_countdown"
    
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
        "angry-dog": "Sj6Cv3CgmXYZ4fq3VviJUgZg_SbRZYhgFGSMq_lbURt8zw8_9qhF8q9Od_9VVcJm4f-1AB5smmjmh6-JT-DEqRLZuBDERV_E0sx3ckrZmy3NTbchQh6H7X8DNj7A3CcgZkpPUThTNHZsUUwwVXhzeA.WyIxLjAuMCIsIldFQiJd",
        "cache-control": "no-cache",
        "front-trace-id": "mh6f17cn0ge28mvnzrvj",
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
    result = fetch_seat_plans()
    print(json.dumps(result, ensure_ascii=False, indent=2))