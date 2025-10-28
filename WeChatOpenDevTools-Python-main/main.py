from argparse import RawTextHelpFormatter
from utils.commons import Commons
from utils.banner import generate_banner
from utils.colors import Color
from utils.cleanup import CleanupUtils
import argparse
import sys



def print_colored_message(message, color):
    print(color + message + Color.END)

def main():
    HELPALL = """
    请选择要执行的方法：         
                        [+] python  main.py -h  查看帮助
                        [+] python  main.py -x  开启小程序F12              
                        [+] python  main.py -c  开启内置浏览器F12
                        [+] python  main.py -all   开启内置浏览器F12与小程序F12
                        [+] python  main.py -cookie 跟踪小程序Cookie
                        [+] python  main.py -clean 清理微信缓存文件
                                     
    """
    try:
        parser = argparse.ArgumentParser(description=HELPALL, formatter_class=RawTextHelpFormatter)
        parser.add_argument('-x', action='store_true', help='开启小程序F12')
        parser.add_argument('-c', action='store_true', help='开启内置浏览器F12')
        parser.add_argument('-all', action='store_true', help='开启内置浏览器F12与小程序F12')
        parser.add_argument('-cookie', action='store_true', help='跟踪小程序Cookie')
        parser.add_argument('-clean', action='store_true', help='清理微信缓存文件')
        args = parser.parse_args()

        if args.x:
            print_colored_message("[*] 正在开启小程序F12调试功能...", Color.GREEN)
            commons.load_wechatEx_configs()
        elif args.c:
            print_colored_message("[*] 正在开启内置浏览器F12调试功能...", Color.GREEN)
            commons.load_wechatEXE_configs()
        elif args.all:
            print_colored_message("[*] 正在开启所有F12调试功能...", Color.GREEN)
            commons.load_wechatEXE_and_wechatEx()
        elif args.cookie:
            print_colored_message("[*] 正在启动小程序Cookie跟踪功能...", Color.GREEN)
            commons.load_wechatEx_cookie_hook()
        elif args.clean:
            print_colored_message("[*] 正在清理微信缓存文件...", Color.GREEN)
            cleanup = CleanupUtils()
            cleanup.clean_wechat_cache()
        else:
            print_colored_message(HELPALL, Color.RED)
    except KeyboardInterrupt:
        print_colored_message("\n[!] 用户中断程序", Color.YELLOW)
    except Exception as e:
        print_colored_message(f"[-] 程序运行出错: {str(e)}", Color.RED)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    commons = None
    try:
        generate_banner()
        commons = Commons()
        main()
    except KeyboardInterrupt:
        print_colored_message("\n[!] 用户中断程序", Color.YELLOW)
    except Exception as e:
        print_colored_message(f"[-] 程序启动出错: {str(e)}", Color.RED)
        import traceback
        traceback.print_exc()
    
    # 程序正常退出
    sys.exit(0)
