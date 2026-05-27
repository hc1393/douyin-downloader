import requests
import json
import time
from urllib.parse import urlencode

def debug_fetch_request():
    """调试版本的请求发送器"""
    
    # 原始的JavaScript fetch配置
    url = "https://capiv2.xinyue.qq.com/cgi-bin/vip_qzproxy.fcgi"
    
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
        "sec-fetch-site": "same-site"
    }
    
    params = {
        "cmd": "jjsonrouter",
        "_t": "1772101608451"  # 使用原始时间戳进行对比
    }
    
    # 原始的请求体
    body = {
        "request": {
            "device": "unknown",
            "openid": "o3wdptyOmvHJ3iQlV2MRrhjmmqrw",
            "acct_type": "wx",
            "appid": "wx5a3bbeac0d87c75a",
            "access_token": "101_K1f_cKRAbVAZ8ey4iUP3Y-7tspqCWZ4gsbtdy4nxEWj3Gp4GE4oKmiwG4AGMCLkJzAbrVD4WYEHZUZ307O5F5xX_IsVu59TSviAlcWGAVII",
            "timestamp": 1772101608,
            "cmd": "QueryRoleSummary",
            "business": "o3wdptyOmvHJ3iQlV2MRrhjmmqrw_1772101608451",
            "sign": "84f0293e09aab79beef73b154acef65d",
            "req": "{\"gameID\":\"1396\",\"pageSize\":15,\"sSort\":\"combatPower=desc\"}"
        }
    }
    
    print("🔍 调试信息:")
    print(f"URL: {url}")
    print(f"参数: {params}")
    print(f"Headers keys: {list(headers.keys())}")
    print(f"Body keys: {list(body.keys())}")
    
    # 尝试发送请求
    try:
        print("\n🚀 发送调试请求...")
        
        # 方法1: 使用json参数
        print("\n方法1: 使用requests.json参数")
        response1 = requests.post(
            url=url,
            params=params,
            headers=headers,
            json=body,
            timeout=30
        )
        print(f"状态码: {response1.status_code}")
        print(f"响应头Content-Type: {response1.headers.get('content-type', 'N/A')}")
        print(f"响应内容: {response1.text[:200]}")
        
        # 方法2: 使用data参数手动序列化
        print("\n方法2: 使用requests.data参数")
        response2 = requests.post(
            url=url,
            params=params,
            headers=headers,
            data=json.dumps(body, separators=(',', ':')),
            timeout=30
        )
        print(f"状态码: {response2.status_code}")
        print(f"响应内容: {response2.text[:200]}")
        
        # 方法3: 模拟浏览器请求
        print("\n方法3: 模拟浏览器完整请求")
        enhanced_headers = headers.copy()
        enhanced_headers.update({
            "origin": "https://xinyue.qq.com",
            "referer": "https://xinyue.qq.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        
        response3 = requests.post(
            url=url,
            params=params,
            headers=enhanced_headers,
            json=body,
            timeout=30
        )
        print(f"状态码: {response3.status_code}")
        print(f"响应内容: {response3.text[:200]}")
        
        # 尝试解析响应
        for i, response in enumerate([response1, response2, response3], 1):
            try:
                result = response.json()
                print(f"\n✅ 方法{i} JSON解析成功:")
                print(json.dumps(result, indent=2, ensure_ascii=False))
            except:
                print(f"\n❌ 方法{i} JSON解析失败")
                
    except Exception as e:
        print(f"❌ 请求异常: {e}")

def compare_with_original():
    """与原始JavaScript请求对比"""
    print("\n" + "="*60)
    print("📋 与原始JavaScript请求对比")
    print("="*60)
    
    # 原始JavaScript代码的关键部分
    js_code_analysis = {
        "method": "POST",
        "mode": "cors",
        "credentials": "omit",
        "content-type": "text/plain",
        "referrer": "https://xinyue.qq.com/"
    }
    
    print("JavaScript fetch配置:")
    for key, value in js_code_analysis.items():
        print(f"  {key}: {value}")
    
    print("\nPython requests对应:")
    python_equivalent = {
        "method": "POST (requests.post)",
        "mode": "cors (自动处理)",
        "credentials": "omit (默认行为)",
        "content-type": "text/plain (在headers中设置)",
        "referrer": "referer (在headers中设置)"
    }
    
    for key, value in python_equivalent.items():
        print(f"  {key}: {value}")

def test_different_approaches():
    """测试不同的请求方法"""
    url = "https://capiv2.xinyue.qq.com/cgi-bin/vip_qzproxy.fcgi"
    
    # 测试不同的参数组合
    test_cases = [
        {
            "name": "基础请求",
            "params": {"cmd": "jjsonrouter"},
            "headers": {"content-type": "text/plain"}
        },
        {
            "name": "带时间戳",
            "params": {"cmd": "jjsonrouter", "_t": str(int(time.time() * 1000))},
            "headers": {"content-type": "text/plain"}
        },
        {
            "name": "完整头部",
            "params": {"cmd": "jjsonrouter", "_t": str(int(time.time() * 1000))},
            "headers": {
                "content-type": "text/plain",
                "accept": "*/*",
                "referer": "https://xinyue.qq.com/"
            }
        }
    ]
    
    body = {
        "request": {
            "device": "unknown",
            "openid": "test_openid",
            "acct_type": "wx",
            "appid": "test_appid",
            "access_token": "test_token",
            "timestamp": int(time.time()),
            "cmd": "QueryRoleSummary",
            "business": f"test_{int(time.time())}",
            "sign": "test_sign",
            "req": "{\"gameID\":\"1396\",\"pageSize\":15}"
        }
    }
    
    print("\n🧪 测试不同请求配置:")
    
    for case in test_cases:
        print(f"\n测试: {case['name']}")
        try:
            response = requests.post(
                url=url,
                params=case['params'],
                headers=case['headers'],
                json=body,
                timeout=10
            )
            print(f"  状态码: {response.status_code}")
            print(f"  响应: {response.text[:100]}")
        except Exception as e:
            print(f"  错误: {e}")

if __name__ == "__main__":
    print("🎮 JavaScript to Python 请求转换调试工具")
    print("=" * 60)
    
    # 执行调试
    debug_fetch_request()
    
    # 对比分析
    compare_with_original()
    
    # 测试不同方法
    test_different_approaches()
    
    print(f"\n✨ 调试完成!")