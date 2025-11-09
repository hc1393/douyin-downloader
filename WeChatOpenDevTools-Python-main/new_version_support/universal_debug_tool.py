import frida
import psutil
import time

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class UniversalDebugTool:
    """
    通用微信小程序调试工具
    不依赖特定版本配置，尝试多种方式启用调试
    """
    
    def __init__(self):
        self.device = frida.get_local_device()
        self.session = None
        self.script = None
        
    def find_wechat_appex_process(self):
        """
        查找微信小程序进程
        """
        print(Color.GREEN + "[*] 正在查找微信小程序进程..." + Color.END)
        
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == 'WeChatAppEx.exe':
                    print(Color.GREEN + f"[+] 找到微信小程序进程 PID: {proc.info['pid']}" + Color.END)
                    return proc.info['pid']
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
                
        print(Color.RED + "[-] 未找到微信小程序进程" + Color.END)
        return None
        
    def on_message(self, message, data):
        """
        处理来自Frida脚本的消息
        """
        try:
            if message['type'] == 'send':
                payload = message.get('payload', {})
                if isinstance(payload, dict):
                    msg_type = payload.get('type', 'info')
                    msg_content = payload.get('message', '')
                    if msg_type == 'debug':
                        print(Color.GREEN + f"[Frida] {msg_content}" + Color.END)
                    elif msg_type == 'error':
                        print(Color.RED + f"[Frida Error] {msg_content}" + Color.END)
                    else:
                        print(Color.BLUE + f"[Frida] {msg_content}" + Color.END)
                else:
                    print(Color.GREEN + f"[Frida] {payload}" + Color.END)
            elif message['type'] == 'error':
                print(Color.RED + f"[Frida Error] {message['description']}" + Color.END)
        except Exception as e:
            print(Color.RED + f"[!] 消息处理出错: {e}" + Color.END)
            
    def load_universal_hook_script(self):
        """
        加载通用Hook脚本
        """
        try:
            script_path = "scripts/universal_hook.js"
            with open(script_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            # 尝试从上级目录加载
            try:
                script_path = "../scripts/universal_hook.js"
                with open(script_path, 'r', encoding='utf-8') as f:
                    return f.read()
            except FileNotFoundError:
                print(Color.RED + "[-] 未找到通用Hook脚本文件" + Color.END)
                return None
        except Exception as e:
            print(Color.RED + f"[-] 加载通用Hook脚本失败: {e}" + Color.END)
            return None
            
    def attach_and_inject(self, pid):
        """
        附加到进程并注入脚本
        """
        try:
            print(Color.GREEN + f"[*] 正在附加到进程 {pid}..." + Color.END)
            self.session = self.device.attach(pid)
            
            # 加载Hook脚本
            script_content = self.load_universal_hook_script()
            if not script_content:
                return False
                
            print(Color.GREEN + "[*] 正在加载Hook脚本..." + Color.END)
            self.script = self.session.create_script(script_content)
            self.script.on('message', self.on_message)
            self.script.load()
            
            print(Color.GREEN + "[+] Hook脚本加载成功" + Color.END)
            return True
            
        except Exception as e:
            print(Color.RED + f"[-] 附加到进程失败: {e}" + Color.END)
            return False
            
    def start_debug(self):
        """
        启动调试
        """
        # 查找微信小程序进程
        pid = self.find_wechat_appex_process()
        if not pid:
            return False
            
        # 附加并注入
        if not self.attach_and_inject(pid):
            return False
            
        print(Color.GREEN + "[+] 通用调试工具已启动" + Color.END)
        print(Color.YELLOW + "[*] 请在微信中重新打开小程序以应用调试设置" + Color.END)
        print(Color.YELLOW + "[*] 按 Ctrl+C 停止调试" + Color.END)
        
        try:
            # 保持运行
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(Color.YELLOW + "\n[!] 调试已停止" + Color.END)
            return True
            
    def stop_debug(self):
        """
        停止调试
        """
        if self.script:
            try:
                self.script.unload()
            except:
                pass
                
        if self.session:
            try:
                self.session.detach()
            except:
                pass
                
        print(Color.GREEN + "[+] 调试会话已清理" + Color.END)

def main():
    print(Color.GREEN + """
    ===============================
    微信小程序通用调试工具
    ===============================
    """ + Color.END)
    
    tool = UniversalDebugTool()
    
    try:
        tool.start_debug()
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {e}" + Color.END)
    finally:
        tool.stop_debug()

if __name__ == "__main__":
    main()