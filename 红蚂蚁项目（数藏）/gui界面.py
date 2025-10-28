import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import requests
import json
import os
from datetime import datetime

class RedAntGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("红蚂蚁数藏工具")
        self.root.geometry("900x700")
        
        # 商品key缓存
        self.goods_key = None
        self.goods_detail_data = None
        
        # 创建界面
        self.create_widgets()
        
        # 任务控制变量
        self.is_running = False
        
    def create_widgets(self):
        # 创建标签页
        tab_control = ttk.Notebook(self.root)
        
        # 登录标签页
        self.login_tab = ttk.Frame(tab_control)
        tab_control.add(self.login_tab, text="账号登录")
        
        # 合成标签页
        self.synthesis_tab = ttk.Frame(tab_control)
        tab_control.add(self.synthesis_tab, text="合成操作")
        
        # 商品详情标签页
        self.goods_detail_tab = ttk.Frame(tab_control)
        tab_control.add(self.goods_detail_tab, text="商品详情")
        
        # 购买标签页
        self.purchase_tab = ttk.Frame(tab_control)
        tab_control.add(self.purchase_tab, text="购买操作")
        
        # 日志标签页
        self.log_tab = ttk.Frame(tab_control)
        tab_control.add(self.log_tab, text="运行日志")
        
        tab_control.pack(expand=1, fill="both")
        
        # 登录标签页内容
        self.create_login_tab()
        
        # 合成标签页内容
        self.create_synthesis_tab()
        
        # 商品详情标签页内容
        self.create_goods_detail_tab()
        
        # 购买标签页内容
        self.create_purchase_tab()
        
        # 日志标签页内容
        self.create_log_tab()
        
    def create_login_tab(self):
        # 账号文件选择
        file_frame = ttk.Frame(self.login_tab)
        file_frame.pack(pady=10, padx=10, fill="x")
        
        ttk.Label(file_frame, text="账号文件:").pack(side="left")
        self.file_path_var = tk.StringVar(value="账号.txt")
        ttk.Entry(file_frame, textvariable=self.file_path_var, width=50).pack(side="left", padx=5)
        ttk.Button(file_frame, text="浏览", command=self.browse_file).pack(side="left", padx=5)
        
        # 登录按钮
        button_frame = ttk.Frame(self.login_tab)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="执行登录", command=self.login_accounts).pack(side="left", padx=5)
        ttk.Button(button_frame, text="刷新Token", command=self.refresh_tokens).pack(side="left", padx=5)
        
        # 账号显示区域
        account_frame = ttk.LabelFrame(self.login_tab, text="账号列表")
        account_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # 创建表格
        columns = ("账号", "密码", "Token状态")
        self.account_tree = ttk.Treeview(account_frame, columns=columns, show="headings", height=15)
        
        # 定义列标题
        for col in columns:
            self.account_tree.heading(col, text=col)
            self.account_tree.column(col, width=150)
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(account_frame, orient="vertical", command=self.account_tree.yview)
        self.account_tree.configure(yscrollcommand=scrollbar.set)
        
        self.account_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # 初始化显示账号
        self.load_accounts()
        
    def create_synthesis_tab(self):
        # 线程设置
        thread_frame = ttk.Frame(self.synthesis_tab)
        thread_frame.pack(pady=10, padx=10, fill="x")
        
        ttk.Label(thread_frame, text="线程数:").pack(side="left")
        self.thread_count_var = tk.StringVar(value="5")
        thread_spinbox = ttk.Spinbox(thread_frame, from_=1, to=50, textvariable=self.thread_count_var, width=10)
        thread_spinbox.pack(side="left", padx=5)
        
        # 控制按钮
        button_frame = ttk.Frame(self.synthesis_tab)
        button_frame.pack(pady=10)
        
        self.start_synthesis_btn = ttk.Button(button_frame, text="开始合成", command=self.start_synthesis)
        self.start_synthesis_btn.pack(side="left", padx=5)
        
        self.stop_synthesis_btn = ttk.Button(button_frame, text="停止合成", command=self.stop_synthesis, state="disabled")
        self.stop_synthesis_btn.pack(side="left", padx=5)
        
        # 进度条
        progress_frame = ttk.Frame(self.synthesis_tab)
        progress_frame.pack(pady=10, padx=10, fill="x")
        
        self.progress_var = tk.StringVar(value="就绪")
        ttk.Label(progress_frame, textvariable=self.progress_var).pack(side="left")
        
        self.progress_bar = ttk.Progressbar(progress_frame, mode="indeterminate")
        self.progress_bar.pack(side="left", fill="x", expand=True, padx=10)
        
    def create_goods_detail_tab(self):
        # 商品信息输入
        input_frame = ttk.LabelFrame(self.goods_detail_tab, text="商品信息")
        input_frame.pack(pady=10, padx=10, fill="x")
        
        input_row = ttk.Frame(input_frame)
        input_row.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(input_row, text="商品ID:").grid(row=0, column=0, sticky="w", padx=5)
        self.detail_goods_id_var = tk.StringVar()
        ttk.Entry(input_row, textvariable=self.detail_goods_id_var, width=20).grid(row=0, column=1, padx=5)
        
        ttk.Label(input_row, text="商品类型:").grid(row=0, column=2, sticky="w", padx=5)
        self.detail_goods_type_var = tk.StringVar()
        ttk.Entry(input_row, textvariable=self.detail_goods_type_var, width=20).grid(row=0, column=3, padx=5)
        
        # 按钮
        button_frame = ttk.Frame(input_frame)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="获取商品详情", command=self.get_goods_detail).pack(side="left", padx=5)
        ttk.Button(button_frame, text="清空详情", command=self.clear_goods_detail).pack(side="left", padx=5)
        
        # 商品详情显示
        detail_frame = ttk.LabelFrame(self.goods_detail_tab, text="商品详情")
        detail_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.goods_detail_text = scrolledtext.ScrolledText(detail_frame, height=20)
        self.goods_detail_text.pack(fill="both", expand=True, padx=5, pady=5)
        
    def create_purchase_tab(self):
        # 商品信息
        goods_frame = ttk.LabelFrame(self.purchase_tab, text="商品信息")
        goods_frame.pack(pady=10, padx=10, fill="x")
        
        goods_info_frame = ttk.Frame(goods_frame)
        goods_info_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(goods_info_frame, text="商品ID:").grid(row=0, column=0, sticky="w", padx=5)
        self.goods_id_var = tk.StringVar()
        ttk.Entry(goods_info_frame, textvariable=self.goods_id_var, width=20).grid(row=0, column=1, padx=5)
        
        ttk.Label(goods_info_frame, text="商品类型:").grid(row=0, column=2, sticky="w", padx=5)
        self.goods_type_var = tk.StringVar()
        ttk.Entry(goods_info_frame, textvariable=self.goods_type_var, width=20).grid(row=0, column=3, padx=5)
        
        ttk.Label(goods_info_frame, text="价格:").grid(row=1, column=0, sticky="w", padx=5)
        self.price_var = tk.StringVar()
        ttk.Entry(goods_info_frame, textvariable=self.price_var, width=20).grid(row=1, column=1, padx=5)
        
        ttk.Label(goods_info_frame, text="数量:").grid(row=1, column=2, sticky="w", padx=5)
        self.quantity_var = tk.StringVar(value="10")
        ttk.Entry(goods_info_frame, textvariable=self.quantity_var, width=20).grid(row=1, column=3, padx=5)
        
        # 倒计时设置
        countdown_frame = ttk.LabelFrame(self.purchase_tab, text="定时抢购")
        countdown_frame.pack(pady=10, padx=10, fill="x")
        
        countdown_info_frame = ttk.Frame(countdown_frame)
        countdown_info_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(countdown_info_frame, text="定时抢购时间 (YYYY-MM-DD HH:MM:SS):").pack(side="left", padx=5)
        self.countdown_time_var = tk.StringVar()
        ttk.Entry(countdown_info_frame, textvariable=self.countdown_time_var, width=25).pack(side="left", padx=5)
        
        # 按钮
        button_frame = ttk.Frame(self.purchase_tab)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="获取商品详情", command=self.get_goods_detail_for_purchase).pack(side="left", padx=5)
        self.start_purchase_btn = ttk.Button(button_frame, text="开始购买", command=self.start_purchase)
        self.start_purchase_btn.pack(side="left", padx=5)
        self.countdown_purchase_btn = ttk.Button(button_frame, text="定时抢购", command=self.countdown_purchase)
        self.countdown_purchase_btn.pack(side="left", padx=5)
        
        # 商品详情显示
        detail_frame = ttk.LabelFrame(self.purchase_tab, text="商品详情")
        detail_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.purchase_detail_text = scrolledtext.ScrolledText(detail_frame, height=10)
        self.purchase_detail_text.pack(fill="both", expand=True, padx=5, pady=5)
        
    def create_log_tab(self):
        # 日志显示区域
        log_frame = ttk.Frame(self.log_tab)
        log_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=20)
        self.log_text.pack(fill="both", expand=True)
        
        # 清空日志按钮
        button_frame = ttk.Frame(self.log_tab)
        button_frame.pack(pady=5)
        
        ttk.Button(button_frame, text="清空日志", command=self.clear_log).pack(side="left", padx=5)
        
        # 重定向print输出到日志
        self.redirect_print_to_log()
        
    def redirect_print_to_log(self):
        # 重定向print输出到日志窗口
        import sys
        import io
        
        class LogWriter(io.StringIO):
            def __init__(self, log_text):
                super().__init__()
                self.log_text = log_text
                
            def write(self, text):
                self.log_text.insert(tk.END, text)
                self.log_text.see(tk.END)
                
            def flush(self):
                pass
                
        sys.stdout = LogWriter(self.log_text)
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="选择账号文件",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.file_path_var.set(file_path)
            self.load_accounts()
            
    def load_accounts(self):
        # 清空现有数据
        for item in self.account_tree.get_children():
            self.account_tree.delete(item)
            
        file_path = self.file_path_var.get()
        if not os.path.exists(file_path):
            return
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if line:
                        parts = line.split("——")
                        if len(parts) >= 2:
                            account = parts[0]
                            password = parts[1]
                            token_status = "已获取" if len(parts) >= 3 and parts[2] else "未获取"
                            self.account_tree.insert("", "end", values=(account, password, token_status))
        except Exception as e:
            messagebox.showerror("错误", f"读取账号文件失败: {e}")
            
    def login_accounts(self):
        def login_thread():
            file_path = self.file_path_var.get()
            if not os.path.exists(file_path):
                print("账号文件不存在")
                return
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    accounts = [line.strip() for line in f.readlines() if line.strip()]
                    
                updated_accounts = []
                for i, account_info in enumerate(accounts):
                    parts = account_info.split("——")
                    if len(parts) < 2:
                        print(f"账号格式错误: {account_info}")
                        updated_accounts.append(account_info)
                        continue
                        
                    account = parts[0]
                    password = parts[1]
                    
                    # 登录获取token
                    token = self.login(account, password)
                    if not token:
                        print(f"账号 {account} 登录失败")
                        if len(parts) >= 3:
                            updated_account_info = account_info
                        else:
                            updated_account_info = account_info
                        updated_accounts.append(updated_account_info)
                        continue
                    
                    print(f"账号 {account} 登录成功")
                    updated_account_info = f"{account}——{password}——{token}"
                    updated_accounts.append(updated_account_info)
                    
                # 写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    for account_info in updated_accounts:
                        f.write(f"{account_info}\n")
                        
                print("所有账号登录完成，token已写入文件")
                self.load_accounts()  # 刷新显示
                
            except Exception as e:
                print(f"登录过程出错: {e}")
                
        threading.Thread(target=login_thread, daemon=True).start()
        
    def login(self, account, password):
        url = "https://api.hyart.art/api/user/login"
        payload = {
            "account": account,
            "password": password
        }
        headers = {
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
        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()
            return response.json()['data']['userinfo']['token']
        except Exception as e:
            print(f"登录失败: {e}")
            return None
            
    def refresh_tokens(self):
        self.load_accounts()
        messagebox.showinfo("提示", "账号列表已刷新")
        
    def start_synthesis(self):
        if self.is_running:
            return
            
        self.is_running = True
        self.start_synthesis_btn.config(state="disabled")
        self.stop_synthesis_btn.config(state="normal")
        self.progress_var.set("正在执行合成任务...")
        self.progress_bar.start()
        
        def synthesis_thread():
            try:
                # 读取账号
                file_path = self.file_path_var.get()
                if not os.path.exists(file_path):
                    print("账号文件不存在")
                    return
                    
                tokens = []
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            parts = line.split("——")
                            if len(parts) >= 3 and parts[2]:  # 有token
                                tokens.append(parts[2])
                                
                if not tokens:
                    print("没有找到有效的token，请先执行登录获取token")
                    return
                    
                # 获取线程数
                try:
                    max_threads = int(self.thread_count_var.get())
                    max_threads = min(max_threads, len(tokens))
                except ValueError:
                    max_threads = min(5, len(tokens))
                    
                print(f"开始多线程合成任务，使用 {max_threads} 个线程")
                
                # 执行合成任务
                self.hecheng_multithread(tokens, max_threads)
                
            except Exception as e:
                print(f"合成任务出错: {e}")
            finally:
                self.is_running = False
                self.root.after(0, self.synthesis_finished)
                
        threading.Thread(target=synthesis_thread, daemon=True).start()
        
    def synthesis_finished(self):
        self.start_synthesis_btn.config(state="normal")
        self.stop_synthesis_btn.config(state="disabled")
        self.progress_var.set("任务完成")
        self.progress_bar.stop()
        messagebox.showinfo("提示", "合成任务已完成")
        
    def stop_synthesis(self):
        self.is_running = False
        self.start_synthesis_btn.config(state="normal")
        self.stop_synthesis_btn.config(state="disabled")
        self.progress_var.set("任务已停止")
        self.progress_bar.stop()
        print("合成任务已手动停止")
        
    def hecheng_multithread(self, tokens, max_threads):
        """多线程执行合成任务"""
        print(f"开始多线程合成任务，使用 {max_threads} 个线程")
        
        def hecheng_worker(token, worker_id):
            """合成任务工作函数"""
            url = "https://api.hyart.art/api/synthesis/playInfo"
            payload = {
                "play_id": "",
                "grp": "",
                "classify": "",
                "user_json": "W10="
            }
            headers = {
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
            
            try:
                response = requests.post(url, data=json.dumps(payload), headers=headers)
                response.raise_for_status()
                result = response.json()
                print(f"线程{worker_id}: 合成请求完成")
                return result
            except Exception as e:
                print(f"线程{worker_id}: 合成请求失败: {e}")
                return None
                
        # 创建线程池执行任务
        with threading.ThreadPoolExecutor(max_workers=max_threads) as executor:
            # 提交所有任务
            futures = {executor.submit(hecheng_worker, token, i): i 
                      for i, token in enumerate(tokens[:max_threads])}
            
            # 等待任务完成
            for future in threading.futures.as_completed(futures):
                if not self.is_running:  # 如果任务被停止
                    break
                worker_id = futures[future]
                try:
                    result = future.result()
                except Exception as e:
                    print(f"线程{worker_id}: 执行异常: {e}")
                    
        print("合成任务执行完毕")
        
    def get_goods_detail(self):
        # 获取商品详情
        goods_id = self.detail_goods_id_var.get()
        goods_type = self.detail_goods_type_var.get()
        
        if not goods_id or not goods_type:
            messagebox.showwarning("警告", "请填写商品ID和商品类型")
            return
            
        # 读取一个token
        file_path = self.file_path_var.get()
        if not os.path.exists(file_path):
            messagebox.showerror("错误", "账号文件不存在")
            return
            
        token = None
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split("——")
                        if len(parts) >= 3 and parts[2]:
                            token = parts[2]
                            break
        except Exception as e:
            messagebox.showerror("错误", f"读取账号文件失败: {e}")
            return
            
        if not token:
            messagebox.showwarning("警告", "没有找到有效的token，请先执行登录")
            return
            
        # 获取商品详情
        try:
            url = "https://api.hyart.art/api/market/market/marketGoodsDetail"
            payload = {
                "id": goods_id,
                "type": goods_type
            }
            headers = {
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
            
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()
            result = response.json()
            
            # 保存商品详情数据
            self.goods_detail_data = result
            
            # 显示结果
            self.goods_detail_text.delete(1.0, tk.END)
            self.goods_detail_text.insert(tk.END, json.dumps(result, indent=2, ensure_ascii=False))
            
            # 提取key并保存
            try:
                self.goods_key = result.get('data', {}).get('key')
                if self.goods_key:
                    print(f"获取到商品key: {self.goods_key}")
                else:
                    print("未能从商品详情中提取key")
            except:
                self.goods_key = None
                print("提取商品key时出错")
                
            messagebox.showinfo("成功", "商品详情获取成功")
        except Exception as e:
            messagebox.showerror("错误", f"获取商品详情失败: {e}")
            
    def clear_goods_detail(self):
        self.goods_detail_text.delete(1.0, tk.END)
        self.goods_detail_data = None
        self.goods_key = None
        print("商品详情已清空")
        
    def get_goods_detail_for_purchase(self):
        # 获取商品详情用于购买
        goods_id = self.goods_id_var.get()
        goods_type = self.goods_type_var.get()
        
        if not goods_id or not goods_type:
            messagebox.showwarning("警告", "请填写商品ID和商品类型")
            return
            
        # 读取一个token
        file_path = self.file_path_var.get()
        if not os.path.exists(file_path):
            messagebox.showerror("错误", "账号文件不存在")
            return
            
        token = None
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split("——")
                        if len(parts) >= 3 and parts[2]:
                            token = parts[2]
                            break
        except Exception as e:
            messagebox.showerror("错误", f"读取账号文件失败: {e}")
            return
            
        if not token:
            messagebox.showwarning("警告", "没有找到有效的token，请先执行登录")
            return
            
        # 获取商品详情
        try:
            url = "https://api.hyart.art/api/market/market/marketGoodsDetail"
            payload = {
                "id": goods_id,
                "type": goods_type
            }
            headers = {
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
            
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()
            result = response.json()
            
            # 保存商品详情数据
            self.goods_detail_data = result
            
            # 显示结果
            self.purchase_detail_text.delete(1.0, tk.END)
            self.purchase_detail_text.insert(tk.END, json.dumps(result, indent=2, ensure_ascii=False))
            
            # 提取key并保存
            try:
                self.goods_key = result.get('data', {}).get('key')
                if self.goods_key:
                    print(f"获取到商品key: {self.goods_key}")
                else:
                    print("未能从商品详情中提取key")
            except:
                self.goods_key = None
                print("提取商品key时出错")
            
            # 如果有价格信息，自动填充
            try:
                price = result.get('data', {}).get('price')
                if price:
                    self.price_var.set(price)
            except:
                pass
                
            messagebox.showinfo("成功", "商品详情获取成功")
        except Exception as e:
            messagebox.showerror("错误", f"获取商品详情失败: {e}")
            
    def start_purchase(self):
        goods_id = self.goods_id_var.get()
        price = self.price_var.get()
        quantity = self.quantity_var.get()
        
        if not goods_id or not price:
            messagebox.showwarning("警告", "请填写商品ID和价格")
            return
            
        # 检查是否有商品key
        if not self.goods_key:
            messagebox.showwarning("警告", "请先获取商品详情以获取商品key")
            return
            
        # 读取token
        file_path = self.file_path_var.get()
        if not os.path.exists(file_path):
            messagebox.showerror("错误", "账号文件不存在")
            return
            
        tokens = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split("——")
                        if len(parts) >= 3 and parts[2]:
                            tokens.append(parts[2])
        except Exception as e:
            messagebox.showerror("错误", f"读取账号文件失败: {e}")
            return
            
        if not tokens:
            messagebox.showwarning("警告", "没有找到有效的token，请先执行登录")
            return
            
        def purchase_thread():
            print(f"开始购买任务，使用 {len(tokens)} 个账号")
            success_count = 0
            
            for i, token in enumerate(tokens):
                try:
                    url = "https://api.hyart.art/api/order/pay/batchBuy"
                    payload = {
                        "price": int(price),
                        "num": int(quantity),
                        "key": self.goods_key,  # 使用从商品详情中获取的key
                        "goods_id": int(goods_id)
                    }
                    headers = {
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
                    
                    response = requests.post(url, data=json.dumps(payload), headers=headers)
                    response.raise_for_status()
                    result = response.json()
                    
                    if result.get('code') == 200:
                        print(f"账号 {i+1} 购买成功")
                        success_count += 1
                    else:
                        print(f"账号 {i+1} 购买失败: {result.get('message', '未知错误')}")
                        
                except Exception as e:
                    print(f"账号 {i+1} 购买请求失败: {e}")
                    
            print(f"购买任务完成，成功: {success_count}/{len(tokens)}")
            messagebox.showinfo("购买完成", f"购买任务完成，成功: {success_count}/{len(tokens)}")
            
        threading.Thread(target=purchase_thread, daemon=True).start()
        
    def countdown_purchase(self):
        countdown_time_str = self.countdown_time_var.get()
        if not countdown_time_str:
            messagebox.showwarning("警告", "请设置定时抢购时间")
            return
            
        try:
            countdown_time = datetime.strptime(countdown_time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("错误", "时间格式错误，请使用 YYYY-MM-DD HH:MM:SS 格式")
            return
            
        current_time = datetime.now()
        if countdown_time <= current_time:
            messagebox.showwarning("警告", "设定时间必须晚于当前时间")
            return
            
        # 禁用按钮
        self.countdown_purchase_btn.config(state="disabled", text="等待抢购...")
        
        def countdown_thread():
            try:
                # 等待到指定时间
                while datetime.now() < countdown_time:
                    # 每秒检查一次，避免长时间阻塞
                    self.root.after(1000)
                    if not self.countdown_purchase_btn.cget("text") == "等待抢购...":
                        print("定时抢购已取消")
                        return
                
                # 时间到了，执行购买
                self.root.after(0, self.start_purchase)
            except Exception as e:
                print(f"倒计时过程出错: {e}")
            finally:
                self.root.after(0, lambda: self.countdown_purchase_btn.config(state="normal", text="定时抢购"))
                
        threading.Thread(target=countdown_thread, daemon=True).start()
        print(f"已设置定时抢购任务，将在 {countdown_time_str} 执行")
        
    def clear_log(self):
        self.log_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = RedAntGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()