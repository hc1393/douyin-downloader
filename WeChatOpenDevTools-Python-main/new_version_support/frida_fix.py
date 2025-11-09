import json
import os
import sys
import psutil
import subprocess
import time

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class FridaFix:
    """
    Frida初始化问题修复工具
    专门解决Frida初始化失败的问题
    """
    
    def __init__(self):
        self.device = None
        self.configs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs')
        self.init_frida()
        
    def init_frida(self):
        """
        初始化Frida，使用多种方法确保成功
        """
        print(Color.GREEN + "[*] 开始修复Frida初始化问题..." + Color.END)
        
        # 方法1: 清理可能存在的frida模块并重新导入
        try:
            if 'frida' in sys.modules:
                del sys.modules['frida']
            import frida
            self.device = frida.get_local_device()
            print(Color.GREEN + "[+] Frida初始化成功 (方法1)" + Color.END)
            return
        except Exception as e1:
            print(Color.YELLOW + f"[-] 方法1失败: {e1}" + Color.END)
        
        # 方法2: 使用importlib重新加载
        try:
            import importlib
            if 'frida' in sys.modules:
                importlib.reload(sys.modules['frida'])
            else:
                importlib.import_module('frida')
            import frida
            self.device = frida.get_local_device()
            print(Color.GREEN + "[+] Frida初始化成功 (方法2)" + Color.END)
            return
        except Exception as e2:
            print(Color.YELLOW + f"[-] 方法2失败: {e2}" + Color.END)
            
        # 方法3: 手动执行import语句
        try:
            exec("import frida")
            self.device = eval("frida.get_local_device()")
            print(Color.GREEN + "[+] Frida初始化成功 (方法3)" + Color.END)
            return
        except Exception as e3:
            print(Color.YELLOW + f"[-] 方法3失败: {e3}" + Color.END)
            
        # 方法4: 重新执行整个导入过程
        try:
            # 清理所有可能的frida相关模块
            frida_modules = [mod for mod in sys.modules.keys() if mod.startswith('frida')]
            for mod in frida_modules:
                del sys.modules[mod]
                
            # 重新导入
            import frida
            self.device = frida.get_local_device()
            print(Color.GREEN + "[+] Frida初始化成功 (方法4)" + Color.END)
            return
        except Exception as e4:
            print(Color.YELLOW + f"[-] 方法4失败: {e4}" + Color.END)
            
        # 方法5: 最后的尝试
        try:
            # 尝试直接重新执行导入
            code = compile("import frida; device = frida.get_local_device()", '<string>', 'exec')
            namespace = {}
            exec(code, namespace)
            self.device = namespace['device']
            print(Color.GREEN + "[+] Frida初始化成功 (方法5)" + Color.END)
            return
        except Exception as e5:
            print(Color.RED + f"[-] 所有方法都失败了: {e5}" + Color.END)
            raise Exception("Frida初始化失败，请检查是否以管理员权限运行")
        
    def test_frida(self):
        """
        测试Frida是否正常工作
        """
        try:
            if not self.device:
                self.init_frida()
                
            # 列出进程测试
            processes = self.device.enumerate_processes()
            wechat_process = None
            for process in processes:
                if process.name == "WeChat.exe":
                    wechat_process = process
                    break
                    
            if wechat_process:
                print(Color.GREEN + f"[+] 找到微信进程: PID {wechat_process.pid}" + Color.END)
                return wechat_process.pid
            else:
                print(Color.YELLOW + "[-] 未找到微信进程" + Color.END)
                return None
        except Exception as e:
            print(Color.RED + f"[-] Frida测试失败: {e}" + Color.END)
            return None
            
    def run_fix(self):
        """
        运行Frida修复
        """
        print(Color.GREEN + "[*] 运行Frida初始化修复..." + Color.END)
        
        try:
            pid = self.test_frida()
            if pid:
                print(Color.GREEN + "[+] Frida修复成功，可以正常工作" + Color.END)
                return True
            else:
                print(Color.YELLOW + "[-] Frida修复完成，但未找到微信进程" + Color.END)
                return True
        except Exception as e:
            print(Color.RED + f"[-] Frida修复失败: {e}" + Color.END)
            return False

def show_help():
    help_text = """
Frida初始化问题修复工具
    
使用方法:
    python frida_fix.py     修复Frida初始化问题
    
特点:
    1. 多种方法修复Frida初始化失败问题
    2. 自动测试Frida是否正常工作
    3. 检测微信进程是否存在
    
注意事项:
    1. 以管理员权限运行以确保正常工作
    2. 本工具仅用于学习研究，请遵守相关法律法规
    """
    print(Color.GREEN + help_text + Color.END)

def main():
    try:
        banner = r"""
  _______           _     _       _____ _ _           
 |  _____|         (_)   | |     |  ___(_) |          
 | |__  __ _ _ __   _  __| | __ _| |__  _| | ___  ___ 
 |  __|/ _` | '_ \ | |/ _` |/ _` |  __|| | |/ _ \/ __|
 | |  | (_| | |_) || | (_| | (_| | |   | | |  __/\__ \
 \_|   \__,_| .__/ |_|\__,_|\__,_\_|   |_|_|\___||___/
            | |                                      
            |_|                                      
        """
        print(Color.GREEN + banner + Color.END)
        print(Color.GREEN + "        Frida初始化问题修复工具" + Color.END)
        print(Color.GREEN + "        公众号: 一位不愿透露姓名的热心网友" + Color.END)
        print()
        
        if len(sys.argv) > 1 and sys.argv[1] == '-h':
            show_help()
            return
            
        fixer = FridaFix()
        if fixer.run_fix():
            print(Color.GREEN + "[+] Frida初始化问题修复完成" + Color.END)
        else:
            print(Color.RED + "[-] Frida初始化问题修复失败" + Color.END)
        
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {str(e)}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()