import os
import sys
import psutil
import subprocess
import time

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 修复模块导入问题
from utils.wechatutils import WechatUtils
from new_version_support.bypass_login_check import WeChatLoginBypass

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class AutoStartWeChat:
    """
    自动启动微信并应用版本检查绕过
    """
    
    def __init__(self):
        self.wechat_utils = WechatUtils()
        
    def find_wechat_installation(self):
        """
        查找微信安装路径
        """
        print(Color.GREEN + "[*] 正在查找微信安装路径..." + Color.END)
        install_path = self.wechat_utils.find_installation_path("微信")
        if not install_path:
            install_path = self.wechat_utils.find_installation_path("WeChat")
        return install_path
        
    def start_wechat(self):
        """
        启动微信
        """
        # 检查微信是否已经运行
        if self.is_wechat_running():
            print(Color.YELLOW + "[*] 微信已经在运行中" + Color.END)
            return True
            
        # 查找微信安装路径
        install_path = self.find_wechat_installation()
        if not install_path:
            print(Color.RED + "[-] 未找到微信安装路径" + Color.END)
            return False
            
        # 启动微信
        try:
            print(Color.GREEN + f"[+] 正在启动微信: {install_path}" + Color.END)
            subprocess.Popen([install_path], shell=False)
            print(Color.GREEN + "[+] 微信启动命令已发送" + Color.END)
            return True
        except Exception as e:
            print(Color.RED + f"[-] 启动微信失败: {e}" + Color.END)
            return False
            
    def is_wechat_running(self):
        """
        检查微信是否正在运行
        """
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] == 'WeChat.exe':
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False
        
    def wait_for_wechat_startup(self, timeout=30):
        """
        等待微信启动完成
        """
        print(Color.GREEN + f"[*] 等待微信启动完成 (超时时间: {timeout}秒)..." + Color.END)
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if self.is_wechat_running():
                print(Color.GREEN + "[+] 微信已启动" + Color.END)
                # 再等待几秒钟确保微信完全初始化
                time.sleep(3)
                return True
            time.sleep(1)
            
        print(Color.RED + "[-] 微信启动超时" + Color.END)
        return False
        
    def apply_bypass(self):
        """
        应用版本检查绕过
        """
        print(Color.GREEN + "[*] 正在应用版本检查绕过..." + Color.END)
        bypass_tool = WeChatLoginBypass()
        return bypass_tool.bypass_login_check()

def show_help():
    help_text = """
微信自动启动并绕过版本检查工具
    
使用方法:
    python auto_start_wechat.py         自动启动微信并应用版本检查绕过
    python auto_start_wechat.py -h      查看帮助
    
注意事项:
    1. 以管理员权限运行以确保正常工作
    2. 本工具仅用于学习研究，请遵守相关法律法规
    """
    print(Color.GREEN + help_text + Color.END)

def main():
    try:
        banner = r"""
    ___       __              __  ___         __        __    __  __          
   /   | ____/ /___ _____   /  |/  /___  ____/ /____   / /   / /_/ /____  _____
  / /| |/ ___/ / __ `/ __ \ / /|_/ / __ \/ __  / ___/  / /   / __/ __/ _ \/ ___/
 / ___ / /__/ / /_/ / / / // /  / / /_/ / /_/ (__  )  / /___/ /_/ /_/  __/ /    
/_/  |_\___/_/\__,_/_/ /_//_/  /_/\____/\__,_/____/  /_____/\__/\__/\___/_/     
                                                                                
        """
        print(Color.GREEN + banner + Color.END)
        print(Color.GREEN + "        微信自动启动并绕过版本检查工具" + Color.END)
        print(Color.GREEN + "        公众号: 一位不愿透露姓名的热心网友" + Color.END)
        print()
        
        if len(sys.argv) > 1 and sys.argv[1] == '-h':
            show_help()
            return
            
        auto_starter = AutoStartWeChat()
        
        # 启动微信
        if not auto_starter.start_wechat():
            print(Color.RED + "[-] 启动微信失败" + Color.END)
            return
            
        # 等待微信启动
        if not auto_starter.wait_for_wechat_startup():
            print(Color.RED + "[-] 等待微信启动失败" + Color.END)
            return
            
        # 应用绕过
        auto_starter.apply_bypass()
        
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {str(e)}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()