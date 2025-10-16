import requests
import subprocess
import json
import os
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock


class DataFetcher:
    def __init__(self, js_file_path='加密.js'):
        """初始化DataFetcher，加载JS文件路径"""
        self.js_file_path = os.path.abspath(js_file_path) if js_file_path else os.path.abspath('加密.js')
        self.lock = Lock()  # 用于线程安全的打印
    
    def get_token(self):
        """获取请求所需的token"""
        # 使用Node.js直接执行JS代码获取token
        js_code = f"""
        const fs = require('fs');
        
        // 读取加密文件（使用with open的方式）
        const jsContent = fs.readFileSync('{self.js_file_path.replace(os.sep, '/')}', 'utf-8');
        eval(jsContent);
        
        // 调用函数获取结果
        const result = s();
        console.log(JSON.stringify({{
            'token': result[0],
            'timestamp': result[1]
        }}));
        """
        
        # 创建唯一的临时JS文件并执行
        temp_js_file = f"temp_token_{uuid.uuid4().hex}.js"
        with open(temp_js_file, "w", encoding="utf-8") as f:
            f.write(js_code)
            
        try:
            # 执行JS代码
            # 显式设置环境变量解决Windows下的编码问题
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            
            result = subprocess.run(
                ["node", temp_js_file], 
                capture_output=True, 
                text=True,
                encoding='utf-8',
                cwd=os.path.dirname(os.path.abspath(__file__)),
                env=env
            )
            
            if result.returncode == 0 and result.stdout.strip():
                # 解析返回的结果
                token_data = json.loads(result.stdout.strip())
                return [token_data['token'], token_data['timestamp']]
            else:
                raise Exception(f"执行JS代码失败: {result.stderr}")
        except UnicodeDecodeError as e:
            # 如果仍然出现编码错误，尝试使用errors='ignore'或errors='replace'参数
            try:
                result = subprocess.run(
                    ["node", temp_js_file], 
                    capture_output=True, 
                    text=True,
                    encoding='utf-8',
                    errors='replace',  # 替换无法解码的字符
                    cwd=os.path.dirname(os.path.abspath(__file__)),
                    env=env
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    # 解析返回的结果
                    token_data = json.loads(result.stdout.strip())
                    return [token_data['token'], token_data['timestamp']]
                else:
                    raise Exception(f"执行JS代码失败: {result.stderr}")
            except Exception as inner_e:
                raise Exception(f"执行JS代码失败: {str(inner_e)}")
        finally:
            # 删除临时文件
            if os.path.exists(temp_js_file):
                os.remove(temp_js_file)
    
    def decrypt_data(self, encrypted_data):
        """解密返回的数据"""
        # 使用Node.js直接执行JS代码解密数据
        js_code = f"""
        const fs = require('fs');
        
        // 读取加密文件（使用with open的方式）
        const jsContent = fs.readFileSync('{self.js_file_path.replace(os.sep, '/')}', 'utf-8');
        eval(jsContent);
        
        try {{
            // 调用函数解密数据
            const result = updatePageContent('{encrypted_data}');
            console.log(JSON.stringify(result));
        }} catch (e) {{
            console.error("Decryption error: " + e.message);
        }}
        """
        
        # 创建唯一的临时JS文件并执行
        temp_js_file = f"temp_decrypt_{uuid.uuid4().hex}.js"
        with open(temp_js_file, "w", encoding="utf-8") as f:
            f.write(js_code)
            
        try:
            # 执行JS代码
            # 显式设置环境变量解决Windows下的编码问题
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            
            result = subprocess.run(
                ["node", temp_js_file], 
                capture_output=True, 
                text=True,
                encoding='utf-8',
                cwd=os.path.dirname(os.path.abspath(__file__)),
                timeout=30,
                env=env
            )
            
            if result.returncode == 0 and result.stdout.strip():
                # 解析返回的结果
                decrypted_data = json.loads(result.stdout.strip())
                return decrypted_data
            elif result.stderr:
                raise Exception(f"执行JS解密代码失败: {result.stderr}")
            else:
                raise Exception("解密结果为空")
        except UnicodeDecodeError as e:
            # 如果仍然出现编码错误，尝试使用errors='ignore'或errors='replace'参数
            try:
                result = subprocess.run(
                    ["node", temp_js_file], 
                    capture_output=True, 
                    text=True,
                    encoding='utf-8',
                    errors='replace',  # 替换无法解码的字符
                    cwd=os.path.dirname(os.path.abspath(__file__)),
                    timeout=30,
                    env=env
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    # 解析返回的结果
                    decrypted_data = json.loads(result.stdout.strip())
                    return decrypted_data
                elif result.stderr:
                    raise Exception(f"执行JS解密代码失败: {result.stderr}")
                else:
                    raise Exception("解密结果为空")
            except Exception as inner_e:
                raise Exception(f"执行JS解密代码失败: {str(inner_e)}")
        finally:
            # 删除临时文件
            if os.path.exists(temp_js_file):
                os.remove(temp_js_file)

    def process_page(self, page_num):
        """处理单个页面的数据"""
        try:
            # 添加小延迟避免触发服务器防护机制
            time.sleep(0.2)
            
            with self.lock:
                print(f"正在获取第 {page_num} 页数据...")
            
            token = self.get_token()
            encrypted_response = fetch_page_data(page_num, token)
            
            # 检查返回的数据是否包含错误信息
            if 't' not in encrypted_response:
                with self.lock:
                    print(f"第 {page_num} 页返回数据格式错误: {encrypted_response}")
                return page_num, 0, []
                
            decrypted_data = self.decrypt_data(encrypted_response['t'])
            
            # 检查解密后的数据是否正确
            if not isinstance(decrypted_data, dict):
                with self.lock:
                    print(f"第 {page_num} 页解密数据格式错误: {decrypted_data}")
                return page_num, 0, []
                
            # 检查是否有current_array字段
            if 'current_array' not in decrypted_data:
                with self.lock:
                    print(f"第 {page_num} 页缺少current_array字段: {decrypted_data}")
                return page_num, 0, []
                
            # 检查current_array的内容
            current_array = decrypted_data["current_array"]
            if not current_array:
                with self.lock:
                    print(f"第 {page_num} 页数据为空: {current_array}")
                return page_num, 0, []
                
            # 检查数组中的元素是否都是数字
            try:
                valid_numbers = []
                for x in current_array:
                    # 检查是否是提示信息
                    if isinstance(x, str) and ("请登录" in x or "登录" in x):
                        raise ValueError("需要登录才能获取数据")
                    
                    if isinstance(x, str) and x.replace('.', '', 1).isdigit():
                        valid_numbers.append(float(x))
                    elif isinstance(x, (int, float)):
                        valid_numbers.append(float(x))
                    else:
                        raise ValueError(f"非数字元素: {x}")
                
                page_sum = sum(valid_numbers)
                
                with self.lock:
                    print(f"第 {page_num} 页数据: {valid_numbers} | 本页合计: {page_sum}")
                
                return page_num, page_sum, valid_numbers
            except ValueError as e:
                with self.lock:
                    print(f"第 {page_num} 页数据转换错误: {e}")
                    print(f"数据内容: {current_array}")
                return page_num, 0, []
        except Exception as e:
            with self.lock:
                print(f"处理第 {page_num} 页时出错: {e}")
            return page_num, 0, []


def fetch_page_data(page, token):
    """获取单页数据"""
    url = f"https://www.mashangpa.com/api/problem-detail/6/data/?page={page}"
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "s": token[0],
        "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "tt": str(token[1]),
        "Referer": "https://www.mashangpa.com/problem-detail/6/",
        "cookie": "Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1758431074,1758546941,1760022553,1760231143; HMACCOUNT=81475DFC18DA7E74; sessionid=3aqg7x6jxhww1c9z8lkqz071glt3iodr; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1760234315"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()


def calculate_total():
    """计算所有页面数据总和"""
    fetcher = DataFetcher()
    total = 0
    
    print("开始获取数据...")
    
    # 使用较小的线程池并发处理页面，避免触发服务器防护机制
    # 限制为2个线程以避免触发服务器防护机制
    with ThreadPoolExecutor(max_workers=5) as executor:
        # 提交所有任务
        future_to_page = {executor.submit(fetcher.process_page, page_num): page_num for page_num in range(1, 21)}
        
        # 收集结果
        results = []
        for future in as_completed(future_to_page):
            page_num, page_sum, data = future.result()
            results.append((page_num, page_sum, data))
        
        # 按页面顺序排序结果
        results.sort(key=lambda x: x[0])
        
        # 计算总和并打印结果
        total = 0
        for page_num, page_sum, data in results:
            total += page_sum
            with fetcher.lock:
                print(f"当前累计值: {total}")
    
    return total


if __name__ == "__main__":
    try:
        start_time = time.time()
        final_total = calculate_total()
        end_time = time.time()
        print(f"最终总计: {final_total}")
        print(f"耗时: {end_time - start_time:.2f} 秒")
    except Exception as e:
        print(f"程序执行出错: {e}")
        import traceback
        traceback.print_exc()
        print("请检查网络连接和相关依赖是否正确安装")