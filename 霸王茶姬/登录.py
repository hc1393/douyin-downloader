import requests
import json

url = "https://miniapp.qmai.cn/web/account-center/oauth/bind-mobile?type__1475=n4%2BxuDyGitYxRjQD%2FD0QoYG%3Dai%3DdD8SlniD0xTD"

payload = {
  "code": "48105a158733dedb8054ae3779afda272e006d5ca53b2463dbd6ab0a0df6c997",
  "reg_activity_source": 0,
  "is_update_mobile": 0,
  "channel_code": "",
  "flowScene": 1089,
  "eVersion": "1.0",
  "appid": "wxafec6f8422cb357b"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 9; OPPO R11 Plus Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 MMWEBID/5512 MicroMessenger/8.0.64.2940(0x28004035) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
  'Accept': "v=1.0",
  'Content-Type': "application/json",
  'store-id': "49006",
  'qm-from': "wechat",
  'qm-from-type': "catering",
  'qm-user-token': "bFb5kybCjdmMZgHiHy6iQPbc26upb_aeyhEf8R7MwhmVXkk84PkivtYp0TJWf5oZCufU4x4ud4t3GM8jKzsrDA",
  'accept-language': "zh-CN",
  'multi-store-id': "245305",
  'charset': "utf-8",
  'referer': "https://servicewechat.com/wxafec6f8422cb357b/268/page-frame.html",
  'Cookie': "acw_tc=ac11000117605942705732546e591661b90d946a2ed5b47bd4e9a6df7065ca; ssxmod_itna3=C50qzxuDRD0D2DRhxjxx0xiqYjYeWKG7iFFQDwhOBDCueqi=i73TuUKQDUAmMG7AxGCD8LKGFD7vP=DBwGpoD/fKuKQxleDARzPM9LDDxGWtCDtdD9DW5Gg74YYDUxGjGDzqi8uxqhEKSyE5TDD5887+5DGI1A=v5x2e4RBi4ZAw4Q2eDSp7WDQeDt2mPgAqaKGoKX00AQ0ffjF4L3GxTtQxh9PeDnPmKB6LxQxkIRtlf6RG09IOutnj64D; "
}

response = requests.post(url, data=json.dumps(payload), headers=headers)


import requests
import json
def  get_goods_detail():
    url = "https://miniapp.qmai.cn/web/catering2-apiserver/goods/detail?type__1475=QqhQ0IqdGNDKKYK0%3D55AKitvgcPwDArbD"

    payload = {
      "goodsId": "625339451983278080",
      "orderType": 1,
      "storeId": "335185",
      "buyTime": "",
      "combinedPractice": 1,
      "version": 2,
      "appid": "wxafec6f8422cb357b"
    }
    
    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 9; OPPO R11 Plus Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 MMWEBID/5512 MicroMessenger/8.0.64.2940(0x28004035) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
      'Accept': "v=1.0",
      'Content-Type': "application/json",
      'store-id': "49006",
      'qm-from-type': "catering",
      'qm-from': "wechat",
      'qm-user-token': "rHqdv6gThex12Aqxakb8OyZtYJn4qf1nj4z2YstNHPTBqFyE_RNpjwdbP1G1CtE2NxDqBakLwQhHGr397IbU4g",
      'accept-language': "zh-CN",
      'work-staff-id': "",
      'work-staff-name': "",
      'work-wechat-userid': "",
      'multi-store-id': "335185",
      'scene': "1089",
      'channelcode': "",
      'promotion-code': "",
      'gdt-vid': "",
      'qz-gtd': "",
      'charset': "utf-8",
      'referer': "https://servicewechat.com/wxafec6f8422cb357b/268/page-frame.html",
      'Cookie': "acw_tc=ac11000117605965604427815e502590e1ee51757e3427904c56be9a0d7a2b; ssxmod_itna3=C50qzxRD0DuD2D0rxRxCqe7qYQyC43qij23P6oqv3QPG8I08kOGjQWDCxxyh2iqGCD8qqD8Dn4DMGAxDseRDBdw=Hne0TDG3MajkX4DeDbg0xBjD7qi1DILoGGDBKDRD4B=DE=5lmI8Asvz=xDCAExDwZxDAO58uZxi=20ePgGxQ0TtYnWTDAv+rx0iDBWTiGTtWpiTPc+4If0L6/feX+ir=gDKe85iDi5i8GvXK0fLCFL2nKk2gREuiuEq4D; "
    }
    
    response1 = requests.post(url, data=json.dumps(payload), headers=headers)


import requests
import json

url = "https://miniapp.qmai.cn/web/catering2-apiserver/goods/list/category-item?type__1475=iqUhDKYvqjoxODl1%2BG7YjqAIeDv30Qoo88F4D"

payload = {
  "orderType": 1,
  "storeId": "335185",
  "buyTime": "",
  "version": 3,
  "appid": "wxafec6f8422cb357b"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 9; OPPO R11 Plus Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 MMWEBID/5512 MicroMessenger/8.0.64.2940(0x28004035) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
  'Accept': "v=1.0",
  'Content-Type': "application/json",
  'store-id': "49006",
  'qm-from-type': "catering",
  'qm-from': "wechat",
  'qm-user-token': "rHqdv6gThex12Aqxakb8OyZtYJn4qf1nj4z2YstNHPTBqFyE_RNpjwdbP1G1CtE2NxDqBakLwQhHGr397IbU4g",
  'accept-language': "zh-CN",
  'work-staff-id': "",
  'work-staff-name': "",
  'work-wechat-userid': "",
  'multi-store-id': "335185",
  'scene': "1089",
  'channelcode': "",
  'promotion-code': "",
  'gdt-vid': "",
  'qz-gtd': "",
  'charset': "utf-8",
  'referer': "https://servicewechat.com/wxafec6f8422cb357b/268/page-frame.html",
  'Cookie': "acw_tc=ac11000117605979948665190e5454722e089343357e19d32a95b844a62daf; "
            "ssxmod_itna3=C50qzxRDnDcDgD0hxx207G0At5AQG7DmOxK8ixCqG=D0lGRrr2bO04B4R=P0QK7DmqikfWDAPD9xxqD/YDrPGX3RexdIDz4DW82IpdFDGDi3Ohc4G=Dcx7tID44GkhD4B=DEP3jqI7IkNNIDDtn0DG2SDDnfq6iSDYIB2xPfhv10xxI74DZbQ3DK4Dv74+k0hfe7fhLGGpLFpWHLbxIAipxLqYDAqYQUTHqWphL+ZchdtB8cWOIcm4xD; "
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
wxafec6f8422cb357b
C:\Users\ThinkPad\AppData\Roaming\Tencent\xwechat\radium\Applet\packages
print(response.text)