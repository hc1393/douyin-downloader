import requests
import json
import hashlib
from datetime import datetime
from urllib.parse import urlencode


def generate_taobao_sign(timestamp_ms):
    """
    生成淘宝API签名
    """
    sign_template = 'c69cd7472809a01d7bec4234a85a1fe3&{}&12574478&{"dfApp":"auctionwalle","dfApiName":"auctionwalle.datou.getPageModulesData","dfVariables":"{\\"pageId\\":1410667,\\"moduleIds\\":\\"5143927030,2196109990,9018433170,8322645760,5958049730,6773865840,9135868500,9418072790,9858993340,6965660040,9688087910,_g_3770826_7945012210,_g_3770831_4454173630,_g_3770831_3226630480,global\\",\\"context\\":{\\"scm\\":\\"20140647.julang.biying.zzyf\\",\\"msclkid\\":\\"fab717eba8a010cd4fea7e6176250895\\",\\"locationCodes\\":\\"[\\\\\\"500000\\\\\\"]\\",\\"page\\":\\"1\\",\\"userInfo\\":\\"{}\\",\\"sceneCode\\":\\"20200713C5R32B6N\\",\\"firstScreen\\":\\"true\\",\\"device\\":\\"pc\\"}}","dfUniqueId":"1410667.5143927030,2196109990,9018433170,8322645760,5958049730,6773865840,9135868500,9418072790,9858993340,6965660040,9688087910,_g_3770826_7945012210,_g_3770831_4454173630,_g_3770831_3226630480,global","dfVariablesRecover":"{}"}'
    
    sign_string = sign_template.format(timestamp_ms)
    sign_hash = hashlib.md5(sign_string.encode('utf-8')).hexdigest()
    return sign_hash

def taobao_auction_request():
    """
    发送淘宝拍卖API请求
    """
    # 生成时间戳
    now = datetime.now()
    timestamp_ms = int(datetime.timestamp(now) * 1000 + now.microsecond // 1000)
    print(f"时间戳: {timestamp_ms}")
    
    # 生成签名
    sign = generate_taobao_sign(timestamp_ms)
    print(f"生成的签名: {sign}")
    
    # 构建请求参数
    url = "https://h5api.m.taobao.com/h5/mtop.taobao.datafront.invoke.auctionwalle/1.0/"
    
    params = {
        "jsv": "2.6.1",
        "appKey": "12574478",
        "t": str(timestamp_ms),
        "sign": sign,
        "bxPageId": "1410667",
        "api": "mtop.taobao.datafront.invoke.auctionwalle",
        "v": "1.0",
        "type": "originaljson",
        "dataType": "json",
        "requiredParams": "dfApiName%2CdfUniqueId"
    }
    
    # 请求头
    headers = {
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
        "Referer": "https://zc-paimai.taobao.com/"
    }
    
    # 请求体数据
    body = "data=%7B%22dfApp%22%3A%22auctionwalle%22%2C%22dfApiName%22%3A%22auctionwalle.datou.getPageModulesData%22%2C%22dfVariables%22%3A%22%7B%5C%22pageId%5C%22%3A1410667%2C%5C%22moduleIds%5C%22%3A%5C%229018433170%3Aitems%5C%22%2C%5C%22context%5C%22%3A%7B%5C%22_b_9018433170%3Aitems%5C%22%3A%5C%22%7B%5C%5C%5C%22scm%5C%5C%5C%22%3A%5C%5C%5C%2220140647.julang.biying.zzyf%5C%5C%5C%22%2C%5C%5C%5C%22msclkid%5C%5C%5C%22%3A%5C%5C%5C%22fab717eba8a010cd4fea7e6176250895%5C%5C%5C%22%2C%5C%5C%5C%22locationCodes%5C%5C%5C%22%3A%5B%5C%5C%5C%22500000%5C%5C%5C%22%5D%2C%5C%5C%5C%22userInfo%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22appendMap%5C%5C%5C%22%3A%7B%5C%5C%5C%22sid%5C%5C%5C%22%3A%5C%5C%5C%226328104745_1770708707074%5C%5C%5C%22%7D%2C%5C%5C%5C%22page%5C%5C%5C%22%3A%5C%5C%5C%221%5C%5C%5C%22%7D%5C%22%2C%5C%22userInfo%5C%22%3A%5C%22%7B%7D%5C%22%2C%5C%22device%5C%22%3A%5C%22pc%5C%22%2C%5C%22sceneCode%5C%22%3A%5C%2220200713C5R32B6N%5C%22%7D%7D%22%2C%22dfUniqueId%22%3A%221410667.9018433170%3Aitems%22%2C%22dfVariablesRecover%22%3A%22%7B%7D%22%7D"
    
    try:
        print("正在发送淘宝拍卖请求...")
        print(f"请求URL: {url}")
        
        # 发送POST请求
        response = requests.post(
            url,
            params=params,
            headers=headers,
            data=body,
            timeout=30
        )
        
        print(f"响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            try:
                json_response = response.json()
                print("请求成功!")
                print("响应数据:")
                print(json.dumps(json_response, ensure_ascii=False, indent=2))
                return json_response
            except json.JSONDecodeError:
                print("响应不是有效的JSON格式")
                print("原始响应内容:")
                print(response.text[:1000])
                return {"raw_response": response.text}
        else:
            print(f"请求失败，状态码: {response.status_code}")
            print("响应内容:")
            print(response.text[:1000])
            return {"error": f"HTTP {response.status_code}", "content": response.text[:1000]}
            
    except requests.exceptions.Timeout:
        print("请求超时")
        return {"error": "请求超时"}
    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")
        return {"error": str(e)}
    except Exception as e:
        print(f"其他错误: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    print("=== 淘宝拍卖API请求示例 ===\n")
    result = taobao_auction_request()
    print("\n=== 请求完成 ===")