import requests
import json
import urllib3
import time
import hashlib
# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getsign(timestamp):
    cmd='QueryRoleSummary'
    cookieMap={'device': 'unknown',
               'openid': 'o3wdptyOmvHJ3iQlV2MRrhjmmqrw',
               'acct_type': 'wx',
               'appid': 'wx5a3bbeac0d87c75a',
               'access_token': '101_sCEJmxcHg4IkqJfc9SopFvzx-Fh8ETUzbVz5UoWakZIw_ZDrVQ9htrs1E4EdTNbHAhDbvZng2S5sxuuaflxOzyvebuX9D9JXtuRdab0Dju8'
               }
    params={"gameID":"1396","pageSize":15,"sSort":"sort_rank=desc"}
    plainText2 = cmd + cookieMap['openid'] + cookieMap['access_token'] + cookieMap['appid'] + str(timestamp) + str(params)
    print(timestamp)

    md5_hash = hashlib.md5(plainText2.encode('utf-8'))
    sign = md5_hash.hexdigest()
    print(sign)
    return sign
print(getsign('1772109564'))

def fetch_game_data(token):
    """完全匹配JavaScript fetch请求的Python实现"""
    timestamp2 = int(time.time())

    timestamp =int(time.time() * 1000)
    print(timestamp,timestamp2)
    # 完全匹配的URL和参数
    url = "https://capiv2.xinyue.qq.com/cgi-bin/vip_qzproxy.fcgi?cmd=jjsonrouter&_t="+str(timestamp)
    print(url)

    
    # 完全匹配的请求头
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "text/plain",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "referrer": "https://xinyue.qq.com/"
    }
    
    # 完全匹配的请求体
    body = {
        "request": {
            "device": "unknown",
            "openid": "o3wdptyOmvHJ3iQlV2MRrhjmmqrw",
            "acct_type": "wx",
            "appid": "wx5a3bbeac0d87c75a",
            "access_token": token,
            "timestamp": timestamp2,
            "cmd": "QueryRoleSummary",
            "business": "o3wdptyOmvHJ3iQlV2MRrhjmmqrw_"+str(timestamp),
            "sign": getsign(timestamp2),
            "req": "{\"gameID\":\"1396\",\"pageSize\":15,\"sSort\":\"sort_rank=desc\",\"context\":[123,34,83,107,105,112,34,58,52,53,44,34,84,115,34,58,49,55,55,50,49,48,55,57,57,57,125]}"
        }
    }
    # 发送请求（模拟fetch的cors模式，omit凭证）
    session = requests.Session()
    session.verify = False  # 对应credentials: "omit"
    try:
        response = session.post(
            url=url,
            headers=headers,
            json=body,  # 自动处理JSON序列化
            timeout=30
        )
        
        # 返回原始响应
        return response.json()
        
    except Exception as e:
        return {"error": str(e)}

# 直接调用函数获取数据
if __name__ == "__main__":
    token='101_sCEJmxcHg4IkqJfc9SopFvzx-Fh8ETUzbVz5UoWakZIw_ZDrVQ9htrs1E4EdTNbHAhDbvZng2S5sxuuaflxOzyvebuX9D9JXtuRdab0Dju8'
    result = fetch_game_data(token)
    print(json.dumps(result, indent=2, ensure_ascii=False))



# fetch("https://capiv2.xinyue.qq.com/cgi-bin/vip_qzproxy.fcgi?cmd=jjsonrouter&_t=1772108524238", {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "cache-control": "no-cache",
#     "content-type": "text/plain",
#     "pragma": "no-cache",
#     "priority": "u=1, i",
#     "sec-ch-ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site"
#   },
#   "referrer": "https://xinyue.qq.com/",
#   "body": "{\"request\":{\"device\":\"unknown\",\"openid\":\"o3wdptyOmvHJ3iQlV2MRrhjmmqrw\",\"acct_type\":\"wx\",\"appid\":\"wx5a3bbeac0d87c75a\",\"access_token\":\"101_sCEJmxcHg4IkqJfc9SopFvzx-Fh8ETUzbVz5UoWakZIw_ZDrVQ9htrs1E4EdTNbHAhDbvZng2S5sxuuaflxOzyvebuX9D9JXtuRdab0Dju8\",\"timestamp\":1772108522,\"cmd\":\"QueryRoleSummary\",\"business\":\"o3wdptyOmvHJ3iQlV2MRrhjmmqrw_1772108524238\",\"sign\":\"06f1b86d4ea9e2496a80f28bcdcf2b67\",\"req\":\"{\\\"gameID\\\":\\\"1396\\\",\\\"pageSize\\\":15,\\\"sSort\\\":\\\"sort_rank=desc\\\",\\\"context\\\":[123,34,83,107,105,112,34,58,52,53,44,34,84,115,34,58,49,55,55,50,49,48,55,57,57,57,125]}\"}}",
#   "method": "POST",
#   "mode": "cors",
#   "credentials": "omit"
# });