import os
import sys
import json
import psutil
import subprocess
import time
from pathlib import Path

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class WeChatDevTools:
    """
    微信开发者工具类
    提供微信小程序调试功能
    """
    
    def __init__(self):
        self.wechat_processes = []
        self.miniprogram_processes = []
        
    def check_wechat_running(self):
        """
        检查微信是否正在运行
        """
        print(Color.GREEN + "[*] 检查微信运行状态..." + Color.END)
        
        wechat_found = False
        miniprogram_found = False
        
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == 'WeChat.exe':
                    wechat_found = True
                    print(Color.GREEN + f"[+] 发现微信主进程 PID: {proc.info['pid']}" + Color.END)
                elif proc.info['name'] == 'WeChatAppEx.exe':
                    miniprogram_found = True
                    print(Color.GREEN + f"[+] 发现小程序进程 PID: {proc.info['pid']}" + Color.END)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
                
        if not wechat_found:
            print(Color.YELLOW + "[-] 微信主进程未运行" + Color.END)
            
        return wechat_found, miniprogram_found
        
    def start_wechat(self):
        """
        启动微信
        """
        print(Color.GREEN + "[*] 尝试启动微信..." + Color.END)
        
        # 尝试多种可能的微信安装路径
        possible_paths = [
            r"D:\Weixin\Weixin.exe",
            r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",
            r"C:\Program Files\Tencent\WeChat\WeChat.exe",
            r"C:\Users\Public\Desktop\微信.lnk",
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                try:
                    subprocess.Popen([path])
                    print(Color.GREEN + f"[+] 成功启动微信: {path}" + Color.END)
                    return True
                except Exception as e:
                    print(Color.YELLOW + f"[-] 启动微信失败: {e}" + Color.END)
                    
        print(Color.RED + "[-] 无法找到微信安装路径" + Color.END)
        return False
        
    def wait_for_miniprogram(self, timeout=30):
        """
        等待小程序进程启动
        """
        print(Color.GREEN + f"[*] 等待小程序进程启动 (超时: {timeout}秒)..." + Color.END)
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if proc.info['name'] == 'WeChatAppEx.exe':
                        print(Color.GREEN + f"[+] 小程序进程已启动 PID: {proc.info['pid']}" + Color.END)
                        return proc.info['pid']
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            time.sleep(1)
            
        print(Color.RED + "[-] 等待超时，未检测到小程序进程" + Color.END)
        return None
        
    def create_debug_shortcut(self):
        """
        创建调试快捷方式
        """
        print(Color.GREEN + "[*] 创建调试快捷方式..." + Color.END)
        
        # 获取桌面路径
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        shortcut_path = os.path.join(desktop, "微信调试工具.lnk")
        
        # 创建一个批处理文件
        bat_content = """
@echo off
echo 微信小程序调试工具
echo ==================
echo 请按以下步骤操作：
echo 1. 确保微信已运行
echo 2. 打开任意小程序
echo 3. 按任意键尝试启用调试功能
pause

REM 这里可以添加更多调试命令
echo 正在检查微信进程...
tasklist | findstr WeChat

echo.
echo 如果需要更多帮助，请参考相关文档
pause
"""
        
        bat_path = os.path.join(desktop, "wechat_debug.bat")
        with open(bat_path, 'w', encoding='utf-8') as f:
            f.write(bat_content)
            
        print(Color.GREEN + f"[+] 已创建批处理文件: {bat_path}" + Color.END)
        print(Color.GREEN + f"[+] 快捷方式路径: {shortcut_path}" + Color.END)
        
    def print_debug_instructions(self):
        """
        打印调试说明
        """
        instructions = """
===============================
微信小程序调试使用说明
===============================

由于微信4.1.0版本加强了安全机制，传统的调试方法可能无法正常工作。
请按照以下步骤进行调试：

方法一：使用微信官方开发者工具（推荐）
1. 下载并安装微信开发者工具
   地址：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
2. 使用USB调试连接手机微信
3. 在开发者工具中调试小程序

方法二：手动启用调试功能
1. 完全关闭微信客户端
2. 导航到微信数据目录：
   - C:\\Users\\[用户名]\\Documents\\WeChat Files\\
   - C:\\Users\\[用户名]\\AppData\\Roaming\\Tencent\\WeChat\\
3. 查找配置文件并修改以下内容：
   {
     "debug": true,
     "enable_vconsole": true,
     "devtools": true
   }
4. 保存文件并设置为只读
5. 重新启动微信

方法三：使用浏览器调试
1. 在微信中打开小程序
2. 选择"更多" -> "在浏览器中打开"
3. 使用浏览器的开发者工具(F12)进行调试

注意事项：
- 本工具仅供学习交流使用
- 请勿用于非法用途
- 使用过程中可能导致微信功能异常
- 建议在测试环境中使用

如需更多帮助，请参考：
- 微信开发者文档：https://developers.weixin.qq.com/
- 微信开放社区：https://developers.weixin.qq.com/community/
        """
        
        print(Color.GREEN + instructions + Color.END)
        
    def run(self):
        """
        运行微信开发者工具
        """
        print(Color.GREEN + """
===============================
微信小程序开发者工具
===============================
        """ + Color.END)
        
        # 检查微信运行状态
        wechat_running, miniprogram_running = self.check_wechat_running()
        
        if not wechat_running:
            # 尝试启动微信
            if self.start_wechat():
                print(Color.YELLOW + "[*] 请等待微信启动完成..." + Color.END)
                time.sleep(5)
                
        # 再次检查
        wechat_running, miniprogram_running = self.check_wechat_running()
        
        if wechat_running:
            print(Color.GREEN + "[+] 微信正在运行" + Color.END)
            
            if not miniprogram_running:
                print(Color.YELLOW + "[*] 请手动打开一个小程序以启动调试" + Color.END)
                
            # 等待小程序启动
            pid = self.wait_for_miniprogram(10)
            if pid:
                print(Color.GREEN + f"[+] 检测到小程序进程 PID: {pid}" + Color.END)
        else:
            print(Color.RED + "[-] 微信未运行，请手动启动微信" + Color.END)
            
        # 创建调试快捷方式
        self.create_debug_shortcut()
        
        # 打印调试说明
        self.print_debug_instructions()
        
        print(Color.GREEN + """
===============================
工具运行完成
===============================

请按照上述说明进行操作。
如需进一步帮助，请查阅相关文档或社区。
        """ + Color.END)

def main():
    try:
        devtools = WeChatDevTools()
        devtools.run()
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {e}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()