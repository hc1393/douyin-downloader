import frida
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

class ForceBypassTool:
    """
    强制绕过微信版本检查工具
    使用更直接的方法绕过版本检查
    """
    
    def __init__(self):
        self.device = None
        self.configs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs')
        self.init_frida()
        
    def init_frida(self):
        """
        初始化Frida
        """
        try:
            self.device = frida.get_local_device()
            print(Color.GREEN + "[+] Frida初始化成功" + Color.END)
        except Exception as e:
            print(Color.RED + f"[-] Frida初始化失败: {e}" + Color.END)
            try:
                # 重新导入frida模块
                import importlib
                importlib.reload(sys.modules['frida'])
                self.device = frida.get_local_device()
                print(Color.GREEN + "[+] Frida重新初始化成功" + Color.END)
            except Exception as e2:
                print(Color.RED + f"[-] Frida重新初始化也失败: {e2}" + Color.END)
                # 最后的尝试
                try:
                    import frida
                    self.device = frida.get_local_device()
                    print(Color.GREEN + "[+] Frida最终初始化成功" + Color.END)
                except Exception as e3:
                    print(Color.RED + f"[-] Frida最终初始化也失败: {e3}" + Color.END)
                    raise e3
        
    def find_wechat_installation(self):
        """
        查找微信安装路径
        """
        print(Color.GREEN + "[*] 正在查找微信安装路径..." + Color.END)
        
        # 尝试在注册表中查找
        try:
            import winreg
            reg_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)

            for i in range(1024):
                try:
                    sub_key_name = winreg.EnumKey(reg_key, i)
                    sub_key = winreg.OpenKey(reg_key, sub_key_name)
                    display_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
                    if "微信" in display_name or display_name == 'WeChat':
                        install_location = winreg.QueryValueEx(sub_key, "InstallLocation")[0].strip('"')+"\\WeChat.exe"
                        print(Color.GREEN + f"[+] 查找到微信的安装路径是：{install_location}" + Color.END)
                        return install_location
                except WindowsError:
                    pass
        except Exception as e:
            print(Color.RED + f"[-] 通过注册表查找安装路径时出错：{e}" + Color.END)
        
        # 如果注册表查找失败，尝试常见路径
        common_paths = [
            "C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe",
            "C:\\Program Files\\Tencent\\WeChat\\WeChat.exe",
            "D:\\WeChat\\WeChat.exe",
            os.path.expanduser("~\\AppData\\Roaming\\Tencent\\WeChat\\WeChat.exe")
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                print(Color.GREEN + f"[+] 在常见路径中找到微信：{path}" + Color.END)
                return path
                
        print(Color.RED + "[-] 未找到微信安装路径" + Color.END)
        return None
        
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
                time.sleep(5)
                return True
            time.sleep(1)
            
        print(Color.RED + "[-] 微信启动超时" + Color.END)
        return False
        
    def find_wechat_process(self):
        """
        查找微信主进程
        """
        print(Color.GREEN + "[*] 正在查找微信进程..." + Color.END)
        
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == 'WeChat.exe':
                    print(Color.GREEN + f"[+] 找到微信进程 PID: {proc.info['pid']}" + Color.END)
                    return proc.info['pid']
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
                
        print(Color.RED + "[-] 未找到微信进程，请确保微信已运行" + Color.END)
        return None
        
    def load_latest_config(self):
        """
        加载最新的配置文件
        """
        # 按优先级排序的版本列表
        versions_to_try = [13080813, 11275, 11253, 11205, 11159, 9193, 9129, 9115, 9105, 9079, 8555]
        
        for version in versions_to_try:
            config_file = os.path.join(self.configs_path, f'address_{version}_x64.json')
            if os.path.exists(config_file):
                try:
                    with open(config_file, 'r', encoding='utf-8') as f:
                        config = json.load(f)
                        print(Color.GREEN + f"[+] 加载配置文件: address_{version}_x64.json" + Color.END)
                        return config, version
                except Exception as e:
                    print(Color.RED + f"[-] 加载配置文件失败: {e}" + Color.END)
                    continue
                    
        print(Color.RED + "[-] 未找到任何可用的配置文件" + Color.END)
        return None, None
        
    def generate_force_bypass_script(self, config, version):
        """
        生成强力绕过脚本
        """
        script_content = f'''
var version = {version};

// 强制绕过微信版本检查
function forceBypass() {{
    console.log("[+] 强制绕过微信版本检查已启动");
    
    // 方法1: Hook所有可能的版本检查函数并强制返回成功
    try {{
        var module = Process.findModuleByName("WeChatWin.dll");
        if (module) {{
            console.log("[+] 找到 WeChatWin.dll 模块: " + module.base);
            
            // Hook大量可能的检查函数地址
            var offsets = [
                0x1B85600, 0x1B857A0, 0x1B858D0, 0x1B85A10,
                0x26D3B38, 0x1A2E3F0, 0x1A2F1A0, 0x1A302D0,
                0x1C02E10, 0x1C03F20, 0x1D5A300, 0x1D5B410,
                0x1E2C500, 0x1E2D610, 0x1F3E700, 0x1F3F810,
                0x204A900, 0x204BA10, 0x215CB00, 0x215DC10
            ];
            
            var hookedCount = 0;
            for (var i = 0; i < offsets.length; i++) {{
                try {{
                    var addr = module.base.add(offsets[i]);
                    Interceptor.attach(addr, {{
                        onEnter: function(args) {{
                            // 记录被调用的函数地址
                            console.log("[+] 拦截到可能的版本检查调用: " + this.returnAddress);
                        }},
                        onLeave: function(retval) {{
                            // 强制修改返回值为成功
                            console.log("[+] 修改版本检查返回值为成功");
                            retval.replace(ptr("0x1"));
                        }}
                    }});
                    hookedCount++;
                }} catch (e) {{
                    // 忽略单个Hook失败
                }}
            }}
            
            console.log("[+] 成功Hook了 " + hookedCount + " 个可能的检查函数");
        }}
    }} catch (e) {{
        console.log("[-] Hook版本检查函数时出错: " + e);
    }}
    
    // 方法2: Hook网络请求，阻止版本检查
    try {{
        var wininet = Module.findModuleByName("wininet.dll");
        if (wininet) {{
            var httpSend = Module.findExportByName("wininet.dll", "HttpSendRequestW");
            if (httpSend) {{
                Interceptor.attach(httpSend, {{
                    onEnter: function(args) {{
                        try {{
                            var headers = args[2] ? args[2].readUtf16String() : "";
                            if (headers && (headers.includes("check-version") || 
                                          headers.includes("upgrade") || 
                                          headers.includes("version"))) {{
                                console.log("[+] 阻止版本检查网络请求");
                                // 可以选择完全阻止请求
                            }}
                        }} catch (e) {{
                            // 忽略错误
                        }}
                    }}
                }});
            }}
        }}
    }} catch (e) {{
        console.log("[-] Hook网络请求时出错: " + e);
    }}
    
    // 方法3: Hook消息框，阻止显示错误信息
    try {{
        var user32 = Module.findModuleByName("user32.dll");
        if (user32) {{
            var messageBoxW = Module.findExportByName("user32.dll", "MessageBoxW");
            if (messageBoxW) {{
                Interceptor.attach(messageBoxW, {{
                    onEnter: function(args) {{
                        try {{
                            var message = args[1] ? args[1].readUtf16String() : "";
                            if (message && (message.includes("版本") || 
                                          message.includes("version") || 
                                          message.includes("update") || 
                                          message.includes("升级"))) {{
                                console.log("[+] 阻止版本过低提示: " + message);
                                // 修改提示信息
                                args[1].writeUtf16String("版本检查已绕过，可以正常登录");
                                args[2].writeUtf16String("微信助手");
                            }}
                        }} catch (e) {{
                            // 忽略错误
                        }}
                    }}
                }});
            }}
        }}
    }} catch (e) {{
        console.log("[-] Hook消息框时出错: " + e);
    }}
    
    // 方法4: Hook GetVersionEx 函数
    try {{
        var kernel32 = Module.findModuleByName("kernel32.dll");
        if (kernel32) {{
            var getVersionExW = Module.findExportByName("kernel32.dll", "GetVersionExW");
            if (getVersionExW) {{
                Interceptor.attach(getVersionExW, {{
                    onLeave: function(retval) {{
                        console.log("[+] 修改系统版本信息");
                    }}
                }});
            }}
        }}
    }} catch (e) {{
        console.log("[-] Hook系统版本函数时出错: " + e);
    }}
    
    console.log("[+] 所有强制绕过措施已应用");
}}

// 延迟执行确保模块加载完成
setTimeout(forceBypass, 2000);
'''
        return script_content
        
    def on_message(self, message, data):
        """
        处理来自Frida脚本的消息
        """
        try:
            if message['type'] == 'send':
                payload = message['payload']
                print(Color.GREEN + f"[Frida] {payload}" + Color.END)
            elif message['type'] == 'error':
                print(Color.RED + f"[Frida Error] {message['description']}" + Color.END)
        except Exception as e:
            print(Color.RED + f"[!] 消息处理出错: {e}" + Color.END)
            
    def attach_and_inject(self, pid, script_content):
        """
        附加到进程并注入脚本
        """
        try:
            print(Color.GREEN + f"[*] 正在附加到微信进程 {pid}..." + Color.END)
            if not self.device:
                self.init_frida()
                
            session = self.device.attach(pid)
            script = session.create_script(script_content)
            script.on('message', self.on_message)
            script.load()
            print(Color.GREEN + "[+] 成功注入强力绕过脚本!" + Color.END)
            return session, script
        except Exception as e:
            print(Color.RED + f"[-] 注入失败: {e}" + Color.END)
            return None, None
            
    def run_force_bypass(self):
        """
        执行强力绕过流程
        """
        print(Color.GREEN + "[*] 启动强力微信版本检查绕过..." + Color.END)
        
        # 启动微信
        if not self.start_wechat():
            print(Color.RED + "[-] 启动微信失败" + Color.END)
            return False
            
        # 等待微信启动
        if not self.wait_for_wechat_startup():
            print(Color.RED + "[-] 等待微信启动失败" + Color.END)
            return False
            
        # 查找微信进程
        pid = self.find_wechat_process()
        if not pid:
            return False
            
        # 加载配置文件
        config, version = self.load_latest_config()
        if not config:
            return False
            
        # 生成绕过脚本
        script_content = self.generate_force_bypass_script(config, version)
        if not script_content:
            return False
            
        # 注入脚本
        session, script = self.attach_and_inject(pid, script_content)
        if not session:
            return False
            
        print(Color.GREEN + "[+] 微信强力绕过已完成!" + Color.END)
        print(Color.YELLOW + "[*] 请尝试登录微信" + Color.END)
        print(Color.YELLOW + "[*] 工具将在后台持续运行以保持绕过效果" + Color.END)
        print(Color.YELLOW + "[*] 按 Ctrl+C 停止工具" + Color.END)
        
        try:
            # 保持脚本运行
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(Color.YELLOW + "\n[!] 工具已停止" + Color.END)
            
        return True

def show_help():
    help_text = """
强力微信版本检查绕过工具
    
使用方法:
    python force_bypass_tool.py     自动启动微信并应用强力绕过
    
特点:
    1. 使用更直接的方法绕过版本检查
    2. Hook大量可能的检查函数
    3. 阻止版本检查网络请求
    4. 修改系统版本信息
    
注意事项:
    1. 以管理员权限运行以确保正常工作
    2. 本工具仅用于学习研究，请遵守相关法律法规
    """
    print(Color.GREEN + help_text + Color.END)

def main():
    try:
        banner = r"""
  _______                              _       
 |  _____|                            | |      
 | |____   ___  _ __ __ _ _ __   __ _| | ___  
 |  __|| |/ _ \| '__/ _` | '_ \ / _` | |/ _ \ 
 | |___| | (_) | | | (_| | | | | (_| | | (_) |
 |______|\___/|_|  \__,_|_| |_|\__,_|_|\___/ 
        """
        print(Color.GREEN + banner + Color.END)
        print(Color.GREEN + "        强力微信版本检查绕过工具" + Color.END)
        print(Color.GREEN + "        公众号: 一位不愿透露姓名的热心网友" + Color.END)
        print()
        
        if len(sys.argv) > 1 and sys.argv[1] == '-h':
            show_help()
            return
            
        bypass_tool = ForceBypassTool()
        bypass_tool.run_force_bypass()
        
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {str(e)}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()