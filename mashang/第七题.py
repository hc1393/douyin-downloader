import requests
import json
import execjs
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock


class ProblemSolver:
    def __init__(self):
        # 读取js文件
        with open('ssss.js', 'r', encoding='utf-8') as f:
            js_content = f.read()
            self.ctx = execjs.compile(js_content)
        # 创建会话对象，复用连接
        self.session = requests.Session()
        # 设置会话的默认headers
        self.session.headers.update({
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "Referer": "https://www.mashangpa.com/problem-detail/7/",
            'cookie': 'sessionid=3aqg7x6jxhww1c9z8lkqz071glt3iodr; Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1760439553,1760452447,1760530880,1760576639; HMACCOUNT=81475DFC18DA7E74; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1760576660',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
        })
        # 创建锁对象，确保线程安全的打印
        self.lock = Lock()
        # 初始化cookies
        self._init_cookies()

    def _init_cookies(self):
        """初始化cookies"""
        try:
            self.session.get("https://www.mashangpa.com/problem-detail/7/", headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            })
        except Exception as e:
            with self.lock:
                print(f"初始化cookies失败: {e}")

    def get_token(self):
        """获取请求参数token"""
        try:
            result = self.ctx.call('hh')
            return result
        except Exception as e:
            with self.lock:
                print(f"获取token失败: {e}")
            return None

    def decrypt_data(self, encrypted_data):
        """解密返回的数据"""
        try:
            result = self.ctx.call('jiema', encrypted_data)
            return result
        except Exception as e:
            with self.lock:
                print(f"解密数据失败: {e}")
            return None

    def fetch_page_data(self, page):
        """获取单页数据"""
        token = self.get_token()
        if not token:
            return page, 0, []

        try:
            # 确保token中的值是字符串
            x_value = str(token[0]) if len(token) > 0 and token[0] else ""
            m_value = str(token[1]) if len(token) > 1 and token[1] else ""
            ts_value = str(token[2]) if len(token) > 2 and token[2] else ""

            # 构造URL
            url = f"https://www.mashangpa.com/api/problem-detail/7/data/?page={page}&x={x_value}"

            # 更新headers中的动态值
            headers = {
                "m": m_value,
                "ts": ts_value,
            }

            # 发送API请求
            response = self.session.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            # 解密数据
            if isinstance(data, dict) and 'r' in data:
                encrypted_content = data['r']
                decrypted_content = self.decrypt_data(encrypted_content)

                if isinstance(decrypted_content, str):
                    # 如果解密后的内容是字符串，尝试解析为JSON
                    try:
                        decrypted_content = json.loads(decrypted_content)
                    except json.JSONDecodeError:
                        with self.lock:
                            print(f"第{page}页解密内容无法解析为JSON: {decrypted_content}")
                        return page, 0, []

                if isinstance(decrypted_content, dict) and 'current_array' in decrypted_content:
                    current_array = decrypted_content['current_array']
                    # 计算当前页的和
                    page_sum = sum(current_array)
                    with self.lock:
                        print(f"第{page}页数据: {current_array}, 本页合计: {page_sum}")
                    return page, page_sum, current_array
                else:
                    with self.lock:
                        print(f"第{page}页解密后格式不正确: {decrypted_content}")
            else:
                with self.lock:
                    print(f"第{page}页响应格式不正确: {data}")
            return page, 0, []
        except requests.exceptions.HTTPError as e:
            if response.status_code == 403:
                with self.lock:
                    print(f"第{page}页请求被拒绝(403)，可能需要等待或检查认证信息")
            else:
                with self.lock:
                    print(f"第{page}页HTTP错误: {e}")
            return page, 0, []
        except Exception as e:
            with self.lock:
                print(f"获取第{page}页数据时出错: {e}")
                import traceback
                traceback.print_exc()
            return page, 0, []


def calculate_total():
    """计算所有页面数据总和"""
    solver = ProblemSolver()
    total = 0

    print("开始获取数据...")

    # 使用线程池并发处理页面，但控制并发数避免触发反爬机制
    with ThreadPoolExecutor(max_workers=5) as executor:  # 增加到5个线程
        # 提交所有任务
        future_to_page = {executor.submit(solver.fetch_page_data, page_num): page_num for page_num in range(1, 21)}

        # 收集结果
        results = []
        for future in as_completed(future_to_page):
            page_num, page_sum, data = future.result()
            results.append((page_num, page_sum, data))

        # 按页面顺序排序结果
        results.sort(key=lambda x: x[0])

        # 计算总和并打印结果
        for page_num, page_sum, data in results:
            total += page_sum
            with solver.lock:
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