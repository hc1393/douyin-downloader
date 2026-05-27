import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import json
import os
from datetime import datetime

class GymBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("体育馆预订系统")
        self.root.geometry("800x700")
        
        # Cookie storage
        self.cookie = ""
        
        # Order ID storage
        self.order_id = ""
        
        # Cookie file path
        self.cookie_file = "cookie.txt"
        
        # Create UI
        self.create_widgets()
        
        # Load saved cookie
        self.load_cookie()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="体育馆预订系统", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Date input
        date_label = ttk.Label(main_frame, text="日期:")
        date_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Date picker frame
        date_frame = ttk.Frame(main_frame)
        date_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Get current date components
        now = datetime.now()
        self.selected_year = tk.StringVar(value=str(now.year))
        self.selected_month = tk.StringVar(value=str(now.month).zfill(2))
        self.selected_day = tk.StringVar(value=str(now.day).zfill(2))
        
        # Year combobox
        year_label = ttk.Label(date_frame, text="年:")
        year_label.pack(side=tk.LEFT)
        self.year_combo = ttk.Combobox(date_frame, textvariable=self.selected_year, width=5, values=[str(y) for y in range(now.year, now.year + 2)])
        self.year_combo.pack(side=tk.LEFT, padx=(0, 5))
        
        # Month combobox
        month_label = ttk.Label(date_frame, text="月:")
        month_label.pack(side=tk.LEFT)
        self.month_combo = ttk.Combobox(date_frame, textvariable=self.selected_month, width=3, values=[str(m).zfill(2) for m in range(1, 13)])
        self.month_combo.pack(side=tk.LEFT, padx=(0, 5))
        
        # Day combobox
        day_label = ttk.Label(date_frame, text="日:")
        day_label.pack(side=tk.LEFT)
        self.day_combo = ttk.Combobox(date_frame, textvariable=self.selected_day, width=3, values=[str(d).zfill(2) for d in range(1, 32)])
        self.day_combo.pack(side=tk.LEFT)
        
        # Cookie input
        cookie_label = ttk.Label(main_frame, text="Cookie:")
        cookie_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        
        self.cookie_entry = scrolledtext.ScrolledText(main_frame, height=4)
        self.cookie_entry.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Save cookie button
        save_cookie_btn = ttk.Button(main_frame, text="保存Cookie", command=self.save_cookie)
        save_cookie_btn.grid(row=2, column=3, padx=(10, 0), pady=5)
        
        # Fetch slots button
        fetch_btn = ttk.Button(main_frame, text="获取可用时段", command=self.fetch_slots)
        fetch_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Slots display
        slots_label = ttk.Label(main_frame, text="可用时间段:", font=("Arial", 12, "bold"))
        slots_label.grid(row=4, column=0, sticky=tk.W, pady=(20, 5))
        
        # Treeview for slots
        columns = ("ID", "场地名称", "时间段", "状态", "Stock ID")
        self.slots_tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=10)
        
        # Define headings
        self.slots_tree.heading("ID", text="ID")
        self.slots_tree.heading("场地名称", text="场地名称")
        self.slots_tree.heading("时间段", text="时间段")
        self.slots_tree.heading("状态", text="状态")
        self.slots_tree.heading("Stock ID", text="Stock ID")
        
        # Set column widths
        self.slots_tree.column("ID", width=80)
        self.slots_tree.column("场地名称", width=120)
        self.slots_tree.column("时间段", width=120)
        self.slots_tree.column("状态", width=80)
        self.slots_tree.column("Stock ID", width=80)
        
        # Scrollbar for treeview
        slots_scroll = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.slots_tree.yview)
        self.slots_tree.configure(yscroll=slots_scroll.set)
        
        self.slots_tree.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        slots_scroll.grid(row=5, column=3, sticky=(tk.N, tk.S), pady=5)
        
        # Book button
        book_btn = ttk.Button(main_frame, text="预订选中时段", command=self.book_slot)
        book_btn.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Payment section
        payment_label = ttk.Label(main_frame, text="支付", font=("Arial", 14, "bold"))
        payment_label.grid(row=7, column=0, sticky=tk.W, pady=(30, 10))
        
        # Order ID display
        order_label = ttk.Label(main_frame, text="订单号:")
        order_label.grid(row=8, column=0, sticky=tk.W, pady=5)
        
        self.order_entry = ttk.Entry(main_frame, width=30, state="readonly")
        self.order_entry.grid(row=8, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Payment button
        pay_btn = ttk.Button(main_frame, text="处理支付", command=self.process_payment)
        pay_btn.grid(row=9, column=0, columnspan=2, pady=10)
        
        # Status display
        status_label = ttk.Label(main_frame, text="状态:", font=("Arial", 10, "bold"))
        status_label.grid(row=10, column=0, sticky=tk.W, pady=(20, 5))
        
        self.status_text = scrolledtext.ScrolledText(main_frame, height=6)
        self.status_text.grid(row=11, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        self.status_text.insert(tk.END, "应用程序已启动。请输入日期和Cookie开始。\n")
        
        # Configure row weights for resizing
        main_frame.rowconfigure(5, weight=1)
        main_frame.rowconfigure(11, weight=1)
        
    def load_cookie(self):
        """Load saved cookie from file"""
        if os.path.exists(self.cookie_file):
            try:
                with open(self.cookie_file, "r", encoding="utf-8") as f:
                    saved_cookie = f.read().strip()
                    if saved_cookie:
                        self.cookie = saved_cookie
                        self.cookie_entry.insert("1.0", self.cookie)
                        self.update_status("已加载保存的Cookie。")
            except Exception as e:
                self.update_status(f"加载Cookie文件时出错: {str(e)}")
        else:
            self.update_status("未找到保存的Cookie文件。")
        
    def save_cookie(self):
        self.cookie = self.cookie_entry.get("1.0", tk.END).strip()
        self.update_status("Cookie保存成功。")
        # Save to file
        try:
            with open(self.cookie_file, "w", encoding="utf-8") as f:
                f.write(self.cookie)
        except Exception as e:
            self.update_status(f"保存Cookie文件时出错: {str(e)}")
        
    def update_status(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.status_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.status_text.see(tk.END)
        
    def get_id(self, time, cookie):
        url = f"https://webvpn.cqnu.edu.cn/webvpn/LjIwNS4xNjcuMTY2LjE2Ni4xNzA=/LjIwNC4xNzIuMTU5LjEwMC4xNTQuMjEyLjE2Ni4xNjkuOTkuMjAyLjIwMi4xNzIuOTUuMjAwLjE1OA==/app/product/findOkArea.html?vpn-12-gym.cqnu.edu.cn=&s_date={time}&serviceid=301"
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0",
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'x-requested-with': "XMLHttpRequest",
            'referer': "https://webvpn.cqnu.edu.cn/webvpn/LjIwNS4xNjcuMTY2LjE2Ni4xNzA=/LjIwNC4xNzIuMTU5LjEwMC4xNTQuMjEyLjE2Ni4xNjkuOTkuMjAyLjIwMi4xNzIuOTUuMjAwLjE1OA==/app/product/show.html?vpn-0&id=301",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'priority': "u=0",
            'te': "trailers",
            'Cookie': cookie
        }
        try:
            response = requests.get(url, headers=headers)
            return response.json()
        except Exception as e:
            self.update_status(f"Error fetching data: {str(e)}")
            return None
            
    def send_request(self, id, stockid, cookie):
        url = "https://webvpn.cqnu.edu.cn/webvpn/LjIwNS4xNjcuMTY2LjE2Ni4xNzA=/LjIwNC4xNzIuMTU5LjEwMC4xNTQuMjEyLjE2Ni4xNjkuOTkuMjAyLjIwMi4xNzIuOTUuMjAwLjE1OA==/app/order/tobook.html?vpn-12-gym.cqnu.edu.cn="
        
        payload = {
            'param': f'{{"stockdetail":{{"{stockid}":"{id}"}}, "serviceid":"301", "stockid":"{stockid},", "remark":""}}',
            'num': "1",
            'json': "true"
        }
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0",
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'x-requested-with': "XMLHttpRequest",
            'origin': "https://webvpn.cqnu.edu.cn",
            'referer': "https://webvpn.cqnu.edu.cn/webvpn/LjIwNS4xNjcuMTY2LjE2Ni4xNzA=/LjIwNC4xNzIuMTU5LjEwMC4xNTQuMjEyLjE2Ni4xNjkuOTkuMjAyLjIwMi4xNzIuOTUuMjAwLjE1OA==/app/product/show.html?vpn-0&id=301",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'priority': "u=0",
            'te': "trailers",
            'Cookie': cookie
        }
        try:
            response = requests.post(url, data=payload, headers=headers)
            result = response.json()
            self.update_status(f"Booking response: {result}")
            if response.status_code == 200:
                return result['object']['order']['orderid']
            else:
                return 'Request failed'
        except Exception as e:
            self.update_status(f"Error sending booking request: {str(e)}")
            return None
    
    def fetch_slots(self):
        # Construct date from selected values
        year = self.selected_year.get()
        month = self.selected_month.get()
        day = self.selected_day.get()
        date = f"{year}-{month}-{day}"
        
        if not date:
            messagebox.showerror("错误", "请选择日期")
            return
            
        if not self.cookie:
            messagebox.showerror("错误", "请保存您的Cookie")
            return
            
        self.update_status(f"正在获取 {date} 的可用时段...")
        
        # Clear existing items
        for item in self.slots_tree.get_children():
            self.slots_tree.delete(item)
            
        # Get data
        data = self.get_id(date, self.cookie)
        if not data:
            self.update_status("获取数据失败")
            return
            
        self.update_status(f"接收到 {len(data.get('object', []))} 个时段的数据")
        
        # Process and display data
        if 'object' in data and data['object']:
            for item in data['object']:
                slot_id = item.get('id', 'N/A')
                name = item.get('name', 'N/A')
                time_slot = item.get('stock', {}).get('time_no', 'N/A')
                status = "可预订" if item.get('status', 0) == 1 else "不可用"
                stock_id = item.get('stockid', 'N/A')
                sname = item.get('sname', 'N/A')
                
                self.slots_tree.insert("", tk.END, values=(slot_id, sname, time_slot, status, stock_id))
        else:
            self.update_status("没有可用时段")
            
    def book_slot(self):
        selected = self.slots_tree.selection()
        if not selected:
            messagebox.showerror("错误", "请选择一个时段进行预订")
            return
            
        if not self.cookie:
            messagebox.showerror("错误", "请保存您的Cookie")
            return
            
        item = self.slots_tree.item(selected[0])
        values = item['values']
        
        slot_id = values[0]
        stock_id = values[4]  # Use the stock ID from the selected row
        
        self.update_status(f"正在预订时段 {slot_id}...")
        
        order_id = self.send_request(slot_id, stock_id, self.cookie)
        if order_id and order_id != 'Request failed':
            self.order_id = order_id
            self.order_entry.config(state="normal")
            self.order_entry.delete(0, tk.END)
            self.order_entry.insert(0, order_id)
            self.order_entry.config(state="readonly")
            self.update_status(f"时段预订成功。订单号: {order_id}")
            messagebox.showinfo("成功", f"时段预订成功! 订单号: {order_id}")
        else:
            self.update_status("预订时段失败")
            messagebox.showerror("错误", "预订时段失败")
            
    def process_payment(self):
        if not self.order_id:
            messagebox.showerror("错误", "没有订单需要处理。请先预订一个时段。")
            return
            
        self.update_status(f"正在处理订单 {self.order_id} 的支付...")
        # 在真实应用中，这里会连接到支付网关
        messagebox.showinfo("支付", f"正在处理订单 {self.order_id} 的支付\n在真实应用中，这里会连接到支付网关")


if __name__ == "__main__":
    root = tk.Tk()
    app = GymBookingApp(root)
    root.mainloop()