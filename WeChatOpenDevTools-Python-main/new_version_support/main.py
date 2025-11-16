import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# 重新定义颜色类，避免依赖
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

from new_version_support.debug_tool import DebugTool
from new_version_support.version_detector import VersionDetector
# 导入新的绕过工具
from new_version_support.bypass_login_check import WeChatLoginBypass
# 导入增强版绕过工具
from new_version_support.enhanced_login_bypass import EnhancedLoginBypass
# 导入自动启动工具
from new_version_support.auto_start_wechat import AutoStartWeChat

def show_help():
    help_text = """
    微信小程序调试工具 (新版本支持)
    
    使用方法:
        python main.py -h     查看帮助
        python main.py -x     开启小程序F12调试
        python main.py -d     检测微信进程信息
        python main.py -all   开启所有调试功能
        python main.py -b     绕过微信版本检查
        python main.py -e     使用增强版绕过微信版本检查
        python main.py -a     自动启动微信并绕过版本检查
    
    注意事项:
        1. 使用前请确保微信已运行
        2. 需要打开至少一个小程序
        3. 以管理员权限运行以确保正常工作
    """
    print(Color.GREEN + help_text + Color.END)

def main():
    try:
        # 简单的banner
        banner = r"""
____    __    ____  _______  __       __          _______   __    __   __       _______.     _______. _______ 
\   \  /  \  /   / |   ____||  |     |  |        |       \ |  |  |  | |  |     /       |    /       ||   ____|
 \   \/    \/   /  |  |__   |  |     |  |        |  .--.  ||  |  |  | |  |    |   (----`   |   (----`|  |__
  \            /   |   __|  |  |     |  |        |  |  |  ||  |  |  | |  |     \   \        \   \    |   __|
   \    /\    /    |  |____ |  `----.|  `----.   |  '--'  ||  `--'  | |  | .----)   | .----)   |   |  |____ 
    \__/  \__/     |_______||_______||_______|   |_______/  \______/  |__| |_______/  |_______/    |_______|
        """
        print(Color.GREEN + banner + Color.END)
        print(Color.GREEN + "        公众号: 一位不愿透露姓名的热心网友" + Color.END)
        print(Color.GREEN + "        Github：https://github.com/JaveleyQAQ" + Color.END)
        print()
        
        if len(sys.argv) < 2:
            show_help()
            return
            
        option = sys.argv[1]
        
        if option == '-h':
            show_help()
        elif option == '-d':
            # 检测微信进程
            detector = VersionDetector()
            detector.print_process_info()
        elif option == '-x':
            # 开启小程序调试
            print(Color.GREEN + "[*] 正在开启小程序F12调试功能..." + Color.END)
            debug_tool = DebugTool()
            debug_tool.start_debug()
        elif option == '-all':
            # 开启所有调试功能
            print(Color.GREEN + "[*] 正在开启所有调试功能..." + Color.END)
            debug_tool = DebugTool()
            debug_tool.start_debug()
        elif option == '-b':
            # 绕过微信版本检查
            print(Color.GREEN + "[*] 正在启动微信版本检查绕过工具..." + Color.END)
            bypass_tool = WeChatLoginBypass()
            bypass_tool.bypass_login_check()
        elif option == '-e':
            # 使用增强版绕过微信版本检查
            print(Color.GREEN + "[*] 正在启动增强版微信版本检查绕过工具..." + Color.END)
            enhanced_bypass_tool = EnhancedLoginBypass()
            enhanced_bypass_tool.bypass_login_check()
        elif option == '-a':
            # 自动启动微信并绕过版本检查
            print(Color.GREEN + "[*] 正在启动微信并应用版本检查绕过..." + Color.END)
            auto_starter = AutoStartWeChat()
            # 启动微信
            if auto_starter.start_wechat():
                # 等待微信启动
                if auto_starter.wait_for_wechat_startup():
                    # 应用绕过
                    auto_starter.apply_bypass()
                else:
                    print(Color.RED + "[-] 等待微信启动失败" + Color.END)
            else:
                print(Color.RED + "[-] 启动微信失败" + Color.END)
        else:
            show_help()
            
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {str(e)}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()