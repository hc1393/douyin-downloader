import requests
import json

url = "https://gator.volces.com/list/"

params = {
    "sdk_version": "2.14.6",
    "sdk_name": "sdk-mp"
}

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "xweb_xhr": "1"
}

# 请求体数据
body_data = [
    {
        "events": [
            {
                "event": "predefine_pageview_hide",
                "params": "{\"scene\":1256,\"query_showId\":\"68da2233bf661a00018048f4\",\"path\":\"package-show/pages/show-detail/show-detail\",\"title\":\"\",\"session_id\":\"6d042675-9048-4b73-82bb-e5d26e6dd738\",\"refer_path\":\"pages/list/list\",\"refer_query\":\"{}\",\"refer_title\":\"\",\"duration\":666008,\"$current_path\":\"package-show/pages/show-detail/show-detail\",\"$current_query\":\"{\\\"showId\\\":\\\"68da2233bf661a00018048f4\\\"}\"}",
                "local_time_ms": 1760797444322,
                "session_id": "6d042675-9048-4b73-82bb-e5d26e6dd738"
            }
        ],
        "user": {
            "web_id": "7562563227792609541",
            "user_unique_id": "6474309bcb521200018c8594"
        },
        "header": {
            "app_id": 20009669,
            "app_version": "4.44.7",
            "os_name": "windows",
            "os_version": "Windows 11 x64",
            "device_model": "microsoft",
            "device_brand": "microsoft",
            "access": "wifi",
            "language": "zh_CN",
            "platform": "mp",
            "sdk_version": "2.14.6",
            "sdk_lib": "mp_common",
            "timezone": 8,
            "tz_offset": -28800,
            "resolution": "414x676",
            "screen_width": 414,
            "screen_height": 676,
            "custom": {
                "custom_platform": "miniProduct",
                "mp_platform": "0",
                "mp_platform_app_version": "3.9.10",
                "mp_platform_basic_version": "3.3.5",
                "miniprogram_appid": "wxad60dd8123a62329",
                "miniprogram_version": "4.44.7",
                "miniprogram_env_version": "release",
                "terminalSrc": "weixin_mini",
                "version": "4.44.7",
                "product": "PIAOXINGQIU",
                "merchantId": "6267a80eed218542786f1494",
                "channel": "",
                "planDistributorId": "",
                "distributorUserId": "",
                "hostSDKVersion": "3.3.5",
                "hostVersion": "3.9.10",
                "cellphone": "173****5160",
                "userId": "6474309bcb521200018c8594"
            },
            "_sdk_version": "2.14.6",
            "_sdk_name": "@datarangers/sdk-mp",
            "is_connected": True
        }
    },
    {
        "events": [
            {
                "event": "leave_page",
                "params": "{\"fromPage\":\"package-show/pages/show-detail/show-detail\",\"pageQuery\":\"showId=68da2233bf661a00018048f4\",\"loadDuration\":666056,\"displayDuration\":666056,\"referrerPage\":\"pages/list/list\",\"trackSessionId\":\"030614070586056807041b0c09835dfa\",\"cityId\":\"BL1266\",\"siteID\":\"6268b2ed53245f055f21d865\",\"$current_path\":\"package-show/pages/show-detail/show-detail\",\"$current_query\":\"{\\\"showId\\\":\\\"68da2233bf661a00018048f4\\\"}\"}",
                "local_time_ms": 1760797444325,
                "session_id": "6d042675-9048-4b73-82bb-e5d26e6dd738"
            }
        ],
        "user": {
            "web_id": "7562563227792609541",
            "user_unique_id": "6474309bcb521200018c8594"
        },
        "header": {
            "app_id": 20009669,
            "app_version": "4.44.7",
            "os_name": "windows",
            "os_version": "Windows 11 x64",
            "device_model": "microsoft",
            "device_brand": "microsoft",
            "access": "wifi",
            "language": "zh_CN",
            "platform": "mp",
            "sdk_version": "2.14.6",
            "sdk_lib": "mp_common",
            "timezone": 8,
            "tz_offset": -28800,
            "resolution": "414x676",
            "screen_width": 414,
            "screen_height": 676,
            "custom": {
                "custom_platform": "miniProduct",
                "mp_platform": "0",
                "mp_platform_app_version": "3.9.10",
                "mp_platform_basic_version": "3.3.5",
                "miniprogram_appid": "wxad60dd8123a62329",
                "miniprogram_version": "4.44.7",
                "miniprogram_env_version": "release",
                "terminalSrc": "weixin_mini",
                "version": "4.44.7",
                "product": "PIAOXINGQIU",
                "merchantId": "6267a80eed218542786f1494",
                "channel": "",
                "planDistributorId": "",
                "distributorUserId": "",
                "hostSDKVersion": "3.3.5",
                "hostVersion": "3.9.10",
                "cellphone": "173****5160",
                "userId": "6474309bcb521200018c8594"
            },
            "_sdk_version": "2.14.6",
            "_sdk_name": "@datarangers/sdk-mp",
            "is_connected": True
        }
    },
    {
        "events": [
            {
                "event": "predefine_pageview",
                "params": "{\"scene\":1256,\"path\":\"pages/list/list\",\"title\":\"\",\"session_id\":\"6d042675-9048-4b73-82bb-e5d26e6dd738\",\"refer_path\":\"package-show/pages/show-detail/show-detail\",\"refer_query\":\"{\\\"showId\\\":\\\"68da2233bf661a00018048f4\\\"}\",\"refer_title\":\"\",\"$current_path\":\"pages/list/list\",\"$current_query\":\"{}\"}",
                "local_time_ms": 1760797444330,
                "session_id": "6d042675-9048-4b73-82bb-e5d26e6dd738"
            }
        ],
        "user": {
            "web_id": "7562563227792609541",
            "user_unique_id": "6474309bcb521200018c8594"
        },
        "header": {
            "app_id": 20009669,
            "app_version": "4.44.7",
            "os_name": "windows",
            "os_version": "Windows 11 x64",
            "device_model": "microsoft",
            "device_brand": "microsoft",
            "access": "wifi",
            "language": "zh_CN",
            "platform": "mp",
            "sdk_version": "2.14.6",
            "sdk_lib": "mp_common",
            "timezone": 8,
            "tz_offset": -28800,
            "resolution": "414x676",
            "screen_width": 414,
            "screen_height": 676,
            "custom": {
                "custom_platform": "miniProduct",
                "mp_platform": "0",
                "mp_platform_app_version": "3.9.10",
                "mp_platform_basic_version": "3.3.5",
                "miniprogram_appid": "wxad60dd8123a62329",
                "miniprogram_version": "4.44.7",
                "miniprogram_env_version": "release",
                "terminalSrc": "weixin_mini",
                "version": "4.44.7",
                "product": "PIAOXINGQIU",
                "merchantId": "6267a80eed218542786f1494",
                "channel": "",
                "planDistributorId": "",
                "distributorUserId": "",
                "hostSDKVersion": "3.3.5",
                "hostVersion": "3.9.10",
                "cellphone": "173****5160",
                "userId": "6474309bcb521200018c8594"
            },
            "_sdk_version": "2.14.6",
            "_sdk_name": "@datarangers/sdk-mp",
            "is_connected": True
        }
    },
    {
        "events": [
            {
                "event": "load_page",
                "params": "{\"loadDuration\":0,\"fromPage\":\"pages/list/list\",\"referrerPage\":\"package-show/pages/show-detail/show-detail\",\"trackSessionId\":\"030614070586056807041b0c09835dfa\",\"cityId\":\"BL1266\",\"siteID\":\"6268b2ed53245f055f21d865\",\"$current_path\":\"pages/list/list\",\"$current_query\":\"{}\"}",
                "local_time_ms": 1760797444334,
                "session_id": "6d042675-9048-4b73-82bb-e5d26e6dd738"
            }
        ],
        "user": {
            "web_id": "7562563227792609541",
            "user_unique_id": "6474309bcb521200018c8594"
        },
        "header": {
            "app_id": 20009669,
            "app_version": "4.44.7",
            "os_name": "windows",
            "os_version": "Windows 11 x64",
            "device_model": "microsoft",
            "device_brand": "microsoft",
            "access": "wifi",
            "language": "zh_CN",
            "platform": "mp",
            "sdk_version": "2.14.6",
            "sdk_lib": "mp_common",
            "timezone": 8,
            "tz_offset": -28800,
            "resolution": "414x676",
            "screen_width": 414,
            "screen_height": 676,
            "custom": {
                "custom_platform": "miniProduct",
                "mp_platform": "0",
                "mp_platform_app_version": "3.9.10",
                "mp_platform_basic_version": "3.3.5",
                "miniprogram_appid": "wxad60dd8123a62329",
                "miniprogram_version": "4.44.7",
                "miniprogram_env_version": "release",
                "terminalSrc": "weixin_mini",
                "version": "4.44.7",
                "product": "PIAOXINGQIU",
                "merchantId": "6267a80eed218542786f1494",
                "channel": "",
                "planDistributorId": "",
                "distributorUserId": "",
                "hostSDKVersion": "3.3.5",
                "hostVersion": "3.9.10",
                "cellphone": "173****5160",
                "userId": "6474309bcb521200018c8594"
            },
            "_sdk_version": "2.14.6",
            "_sdk_name": "@datarangers/sdk-mp",
            "is_connected": True
        }
    },
    {
        "events": [
            {
                "event": "display_page",
                "params": "{\"fromPage\":\"pages/list/list\",\"referrerPage\":\"package-show/pages/show-detail/show-detail\",\"loadDuration\":0,\"displayDuration\":0,\"trackSessionId\":\"030614070586056807041b0c09835dfa\",\"cityId\":\"BL1266\",\"siteID\":\"6268b2ed53245f055f21d865\",\"$current_path\":\"pages/list/list\",\"$current_query\":\"{}\"}",
                "local_time_ms": 1760797444335,
                "session_id": "6d042675-9048-4b73-82bb-e5d26e6dd738"
            }
        ],
        "user": {
            "web_id": "7562563227792609541",
            "user_unique_id": "6474309bcb521200018c8594"
        },
        "header": {
            "app_id": 20009669,
            "app_version": "4.44.7",
            "os_name": "windows",
            "os_version": "Windows 11 x64",
            "device_model": "microsoft",
            "device_brand": "microsoft",
            "access": "wifi",
            "language": "zh_CN",
            "platform": "mp",
            "sdk_version": "2.14.6",
            "sdk_lib": "mp_common",
            "timezone": 8,
            "tz_offset": -28800,
            "resolution": "414x676",
            "screen_width": 414,
            "screen_height": 676,
            "custom": {
                "custom_platform": "miniProduct",
                "mp_platform": "0",
                "mp_platform_app_version": "3.9.10",
                "mp_platform_basic_version": "3.3.5",
                "miniprogram_appid": "wxad60dd8123a62329",
                "miniprogram_version": "4.44.7",
                "miniprogram_env_version": "release",
                "terminalSrc": "weixin_mini",
                "version": "4.44.7",
                "product": "PIAOXINGQIU",
                "merchantId": "6267a80eed218542786f1494",
                "channel": "",
                "planDistributorId": "",
                "distributorUserId": "",
                "hostSDKVersion": "3.3.5",
                "hostVersion": "3.9.10",
                "cellphone": "173****5160",
                "userId": "6474309bcb521200018c8594"
            },
            "_sdk_version": "2.14.6",
            "_sdk_name": "@datarangers/sdk-mp",
            "is_connected": True
        }
    }
]

# 发送POST请求
response = requests.post(url, params=params, headers=headers, json=body_data)

# 输出响应状态码和内容
print("Status Code:", response.status_code)
print("Response Text:", response.text)


