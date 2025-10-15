import requests
import json
import execjs

def get_url():
  with open('ssss.js', 'r', encoding='utf-8') as f:
    j = f.read()
    ctx = execjs.compile(j)
    result = ctx.call('hh')
  return result

def fetch_page_data(page, token, proxy=None):
    """获取单页数据"""
    # 修复URL构造
    url = f"https://www.mashangpa.com/api/problem-detail/7/data/?page={page}&x={token[0]}"
    
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        # 使用从token中获取的m值
        "m": token[1],
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        # 使用从token中获取的时间戳
        "ts": str(token[2]),
        "x-requested-with": "XMLHttpRequest",
        "Referer": "https://www.mashangpa.com/problem-detail/7/",
        # 添加User-Agent
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    }
    
    # 使用session保持cookies
    session = requests.Session()
    
    # 如果提供了代理，则设置代理
    if proxy:
        session.proxies = {
            "http": proxy,
            "https": proxy,
        }
        print(f"使用代理: {proxy}")
    
    # 先访问主页获取必要的cookies
    session.get("https://www.mashangpa.com/problem-detail/7/", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    })
    
    # 发送API请求
    response = session.get(url, headers=headers)
    return response.json()

# 新增函数：直接使用fetch代码中的参数发送请求
def fetch_with_static_params(proxy=None):
    """
    根据fetch代码直接发送请求
    """
    url = "https://www.mashangpa.com/api/problem-detail/7/data/?page=1&x=08e678a0c9a3bf98411c24128d8b49a7ccfd6c1b93088bacbb57f8d3ad31cb20"
    
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "m": "eff63b4fad7ec7b2949bbea1028bce36",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "ts": "1760536220314",
        "x-requested-with": "XMLHttpRequest",
        "Referer": "https://www.mashangpa.com/problem-detail/7/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    }
    
    # 使用session保持cookies
    session = requests.Session()
    
    # 如果提供了代理，则设置代理
    if proxy:
        session.proxies = {
            "http": proxy,
            "https": proxy,
        }
        print(f"使用代理: {proxy}")
    
    # 先访问主页获取必要的cookies
    session.get("https://www.mashangpa.com/problem-detail/7/", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    })
    
    # 发送API请求
    response = session.get(url, headers=headers)
    return response.json()

def ss(proxy=None):
    total = 0
    for i in range(1, 2):
      token=get_url()
      print(token)
      data=fetch_page_data(i, token, proxy)
      return data

# 代理配置函数
def setup_proxy(proxy_type="http", host="127.0.0.1", port=8080, username=None, password=None):
    """
    配置代理服务器
    
    参数:
    proxy_type: 代理类型 ("http", "https", "socks5")
    host: 代理服务器地址
    port: 代理服务器端口
    username: 代理用户名（如果需要认证）
    password: 代理密码（如果需要认证）
    
    返回:
    格式化后的代理URL
    """
    if username and password:
        proxy_url = f"{proxy_type}://{username}:{password}@{host}:{port}"
    else:
        proxy_url = f"{proxy_type}://{host}:{port}"
    
    return proxy_url

# 测试代理连接
def test_proxy_connection(proxy):
    """
    测试代理连接是否正常
    """
    try:
        session = requests.Session()
        if proxy:
            session.proxies = {
                "http": proxy,
                "https": proxy,
            }
        
        response = session.get("http://httpbin.org/ip", timeout=10)
        if response.status_code == 200:
            print("代理连接成功!")
            print("当前IP地址:", response.json())
            return True
        else:
            print(f"代理连接失败，状态码: {response.status_code}")
            return False
    except Exception as e:
        print(f"代理连接测试失败: {e}")
        return False

if __name__ == "__main__":
    # 代理配置 - 请根据你的实际情况修改这里
    # 以下是几种常见的代理配置方式:
    
    # 1. 不使用代理（直接连接）
    # proxy = None
    
    # 2. HTTP代理
    # proxy = setup_proxy("http", "127.0.0.1", 8080)
    
    # 3. HTTPS代理
    # proxy = setup_proxy("https", "127.0.0.1", 8443)
    
    # 4. SOCKS5代理（需要安装: pip install requests[socks]）
    # proxy = setup_proxy("socks5", "127.0.0.1", 1080)
    
    # 5. 需要认证的代理
    # proxy = setup_proxy("http", "proxy.server", 8080, "username", "password")
    
    # 实际使用的代理配置
    proxy = None  # 修改这里来使用代理
    
    # 测试代理连接
    if proxy:
        print("正在测试代理连接...")
        if not test_proxy_connection(proxy):
            print("代理连接测试失败，将继续尝试发送请求...")
        print()
    
    # 尝试使用动态生成的参数
    try:
        print("尝试使用动态生成的参数:")
        result = ss(proxy)
        print("请求成功!")
        print(result)
    except Exception as e:
        print(f"动态参数请求失败: {e}")
        
        # 如果动态参数失败，尝试使用静态参数
        print("\n尝试使用静态参数:")
        try:
            result = ss()
            print("请求成功!")
            print(result)
        except Exception as e:
            print(f"静态参数请求也失败了: {e}")