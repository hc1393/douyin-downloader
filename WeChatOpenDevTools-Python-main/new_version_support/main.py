import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.banner import generate_banner
from utils.colors import Color
from new_version_support.debug_tool import DebugTool
from new_version_support.version_detector import VersionDetector

def show_help():
    help_text = """
    微信小程序调试工具 (新版本支持)
    
    使用方法:
        python main.py -h     查看帮助
        python main.py -x     开启小程序F12调试
        python main.py -d     检测微信进程信息
        python main.py -all   开启所有调试功能
    
    注意事项:
        1. 使用前请确保微信已运行
        2. 需要打开至少一个小程序
        3. 以管理员权限运行以确保正常工作
    """
    print(Color.GREEN + help_text + Color.END)

def main():
    try:
        generate_banner()
        
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