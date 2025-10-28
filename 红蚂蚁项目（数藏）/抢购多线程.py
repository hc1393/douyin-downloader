import requests
import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

class ApiHeaders:
    """API请求头管理类"""
    @staticmethod
    def get_login_headers():
        """获取登录请求头"""
        return {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Windows\"",
            'sec-ch-ua': "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
            'version': "1.0.1",
            'sec-ch-ua-mobile': "?0",
            'Origin': "https://hyart.art",
            'Sec-Fetch-Site': "same-site",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://hyart.art/",
            'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
        }
    
    @staticmethod
    def get_market_headers(token):
        """获取市场相关请求头"""
        return {
            'accept': "*/*",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            'cache-control': "no-cache",
            'content-type': "application/json",
            'pragma': "no-cache",
            'sec-ch-ua': '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': "?0",
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'token': token,
            'referrer': "https://hyart.art/"
        }
    
    @staticmethod
    def get_common_headers(token):
        """获取通用认证请求头"""
        return {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'sec-ch-ua-mobile': "?0",
            'sec-ch-ua-platform': "\"Windows\"",
            'sec-ch-ua': "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
            'version': "1.0.1",
            'token': token,
            'Origin': "https://hyart.art",
            'Sec-Fetch-Site': "same-site",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://hyart.art/",
            'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
        }

def login(account, password):
    """用户登录获取token"""
    url = "https://api.hyart.art/api/user/login"
    payload = {
        "account": account,
        "password": password
    }
    headers = ApiHeaders.get_login_headers()
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        return response.json()['data']['userinfo']['token']
    except Exception as e:
        print(f"登录失败: {e}")
        return None

def get_market_goods_detail(token, goods_id, goods_type):
    """
    获取市场商品详情
    
    Args:
        token (str): 用户身份验证令牌
        goods_id (str): 商品ID
        goods_type (str): 商品类型
    
    Returns:
        dict: 商品详情数据
    """
    url = "https://api.hyart.art/api/market/market/marketGoodsDetail"
    
    payload = {
        "id": goods_id,
        "type": goods_type
    }
    
    headers = ApiHeaders.get_market_headers(token)
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"获取商品详情失败: {e}")
        return None

def read_accounts():
    """从文件中读取账户信息"""
    try:
        with open('账号.txt', 'r', encoding='utf-8') as f:
            accounts = []
            for line in f.readlines():
                line = line.strip()
                if line:
                    parts = line.split("——")
                    if len(parts) >= 3:  # 账号——密码——token格式
                        accounts.append({
                            'account': parts[0],
                            'password': parts[1],
                            'token': parts[2]
                        })
                    elif len(parts) == 2:  # 账号——密码格式
                        accounts.append({
                            'account': parts[0],
                            'password': parts[1],
                            'token': None
                        })
            return accounts
    except FileNotFoundError:
        print("未找到账号.txt文件")
        return []

def hecheng_worker(token, worker_id):
    """合成任务工作函数"""
    url = "https://api.hyart.art/api/synthesis/playInfo"
    payload = {
        "play_id": "",
        "grp": "",
        "classify": "",
        "user_json": "W10="
    }
    headers = ApiHeaders.get_common_headers(token)
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        result = response.json()
        print(f"线程{worker_id}: 合成请求完成，结果: {result}")
        return result
    except Exception as e:
        print(f"线程{worker_id}: 合成请求失败: {e}")
        return None

def hecheng_multithread(tokens, max_threads=5):
    """多线程执行合成任务"""
    print(f"开始多线程合成任务，使用 {min(len(tokens), max_threads)} 个线程")
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # 提交所有任务
        futures = {executor.submit(hecheng_worker, token, i): i 
                  for i, token in enumerate(tokens)}
        
        # 获取结果
        results = []
        for future in as_completed(futures):
            worker_id = futures[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"线程{worker_id}: 执行异常: {e}")
        
        return results

def hecheng_main():
    """合成主函数"""
    # 从文件读取账户信息
    accounts = read_accounts()
    if not accounts:
        print("没有找到有效的账户信息")
        return
    
    # 获取所有有效的token
    tokens = [account['token'] for account in accounts if account['token']]
    if not tokens:
        print("没有找到有效的token，请先执行登录获取token")
        return
    
    # 获取用户输入的线程数
    try:
        max_threads = int(input(f"请输入线程数（默认为{min(len(tokens), 5)}，最大支持{len(tokens)}）: ") or min(len(tokens), 5))
        max_threads = min(max_threads, len(tokens))
    except ValueError:
        max_threads = min(len(tokens), 5)
    
    # 执行多线程合成任务
    results = hecheng_multithread(tokens, max_threads)
    print(f"合成任务完成，共处理 {len(results)} 个请求")

def buy(token, key, goods_id, price):
    """购买藏品"""
    url = "https://api.hyart.art/api/order/pay/batchBuy"

    payload = {
        "price": price,
        "num": 10,
        "key": key,
        "goods_id": goods_id
    }
    headers = ApiHeaders.get_common_headers(token)
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"购买请求失败: {e}")
        return None

def main():
    """主函数 - 登录并更新token"""
    # 读取账号文件
    try:
        with open('账号.txt', 'r', encoding='utf-8') as f:
            accounts = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("未找到账号.txt文件")
        return
    
    updated_accounts = []
    
    # 遍历所有账号进行登录
    for account_info in accounts:
        # 解析账号信息
        parts = account_info.split("——")
        if len(parts) < 2:
            print(f"账号格式错误: {account_info}")
            updated_accounts.append(account_info)  # 保持原样
            continue
        
        account = parts[0]
        password = parts[1]
        
        # 登录获取token
        token = login(account, password)
        if not token:
            print(f"账号 {account} 登录失败")
            # 保留原有token如果存在
            if len(parts) >= 3:
                updated_account_info = account_info  # 保留原有信息包括token
            else:
                updated_account_info = account_info  # 保持原样
            updated_accounts.append(updated_account_info)
            continue
        
        print(f"账号 {account} 登录成功")
        # 将token添加到账号信息中
        updated_account_info = f"{account}——{password}——{token}"
        updated_accounts.append(updated_account_info)
    
    # 将更新后的账号信息写回文件
    with open('账号.txt', 'w', encoding='utf-8') as f:
        for account_info in updated_accounts:
            f.write(f"{account_info}\n")
    
    print("所有账号登录完成，token已写入文件")

if __name__ == "__main__":
    # 运行合成任务
    hecheng_main()