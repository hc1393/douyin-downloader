import requests
import json
import execjs
def get_url(k):
  with open('加密.js', 'r', encoding='utf-8') as f:
    j = f.read()
    ctx = execjs.compile(j)
    result = ctx.call('loadPage', str(k))
  return result
def token1(i):
    a=get_url(i)
    return a
def qingqiu(token):
  url = "https://www.mashangpa.com/api/problem-detail/5/data/"
  headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "referer": "https://www.mashangpa.com/problem-detail/5/",
    "Cookie": 'sessionid=bv2oh8xoizs69iwxq8n3tdn8cr8oxu90; Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1757430160,1757483015,1758277021; HMACCOUNT=1846E94D0D2F249B; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1758278085'  }
  payload = {
    "xl": token
  }
  # 使用session自动处理cookies
  response = requests.post(url,json=payload,  headers=headers )
  return response.json()


def ss():
    total = 0
    for i in range(1, 21):
      token=token1(i)
      data=qingqiu(token)
      print(data)
      page_sum = sum(float(x) for x in data["current_array"])
      print(f"第 {i} 页数据: {data['current_array']} | 本页合计: {page_sum}")
      total += page_sum
      print(f"当前累计值: {total}")
    return total

print(ss())
