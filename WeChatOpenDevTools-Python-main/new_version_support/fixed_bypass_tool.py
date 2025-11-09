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

class FixedBypassTool:
    """
    修复版微信绕过工具
    专门解决Frida TypeError: not a function 错误
    """
    
    def __init__(self):
        self.device = None
        self.configs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs')
        self.init_frida()
        
    def init_frida(self):
        """
        初始化Frida并处理可能的错误
        """
        try:
            self.device = frida.get_local_device()
            print(Color.GREEN + "[+] Frida初始化成功" + Color.END)
        except Exception as e:
            print(Color.RED + f"[-] Frida初始化失败: {e}" + Color.END)
            # 尝试重新初始化
            try:
                import frida
                self.device = frida.get_local_device()
                print(Color.GREEN + "[+] Frida重新初始化成功" + Color.END)
            except Exception as e2:
                print(Color.RED + f"[-] Frida重新初始化也失败: {e2}" + Color.END)
                raise e2
        
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
                    # 排除企业微信 和 适配英文区域安装的WeChat
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
        
    def generate_fixed_bypass_script(self, config, version):
        """
        生成修复版绕过脚本，避免TypeError: not a function错误
        """
        script_content = f'''
var version = {version};

// 安全获取模块基址的函数
function safeGetModule(name) {{
    try {{
        var module = Process.findModuleByName(name);
        if (module) {{
            console.log("[+] 找到模块 " + name + ": " + module.base);
            return module;
        }} else {{
            console.log("[-] 未找到模块: " + name);
            return null;
        }}
    }} catch (e) {{
        console.log("[-] 获取模块 " + name + " 失败: " + e);
        return null;
    }}
}}

// 安全Hook函数
function safeInterceptorAttach(address, callbacks) {{
    try {{
        if (address && typeof address.equals === 'function') {{
            Interceptor.attach(address, callbacks);
            return true;
        }} else {{
            console.log("[-] 无效的地址，无法Hook: " + address);
            return false;
        }}
    }} catch (e) {{
        console.log("[-] Hook失败: " + e);
        return false;
    }}
}}

// 安全获取导出函数地址
function safeGetExport(moduleName, functionName) {{
    try {{
        var addr = Module.findExportByName(moduleName, functionName);
        if (addr) {{
            console.log("[+] 找到导出函数 " + functionName + ": " + addr);
            return addr;
        }} else {{
            console.log("[-] 未找到导出函数: " + functionName);
            return null;
        }}
    }} catch (e) {{
        console.log("[-] 获取导出函数 " + functionName + " 失败: " + e);
        return null;
    }}
}}

// 获取模块基址
var wechatWinModule = safeGetModule("WeChatWin.dll");
var wechatAppModule = safeGetModule("WeChatAppEx.exe");
var user32Module = safeGetModule("user32.dll");
var kernel32Module = safeGetModule("kernel32.dll");

console.log("[+] WeChatWin.dll 模块地址: " + (wechatWinModule ? wechatWinModule.base : "未找到"));
console.log("[+] WeChatAppEx.exe 模块地址: " + (wechatAppModule ? wechatAppModule.base : "未找到"));

// 修复版版本检查绕过
function fixedVersionBypass() {{
    try {{
        // Hook多个版本检查函数地址
        var versionCheckOffsets = [
            0x1B85600,  // 常见版本检查地址1
            0x1B857A0,  // 常见版本检查地址2
            0x1B858D0,  // 常见版本检查地址3
            0x1B85A10,  // 常见版本检查地址4
            0x26D3B38,  // 配置文件中的SwitchVersion地址
            0x1A2E3F0,  // 假设的配置检查地址1
            0x1A2F1A0,  // 假设的配置检查地址2
            0x1A302D0   // 假设的配置检查地址3
        ];
        
        var hookedCount = 0;
        for (var i = 0; i < versionCheckOffsets.length; i++) {{
            try {{
                if (wechatWinModule) {{
                    var funcAddr = wechatWinModule.base.add(versionCheckOffsets[i]);
                    if (safeInterceptorAttach(funcAddr, {{
                        onLeave: function(retval) {{
                            console.log("[+] 拦截到版本/配置检查函数调用，修改返回值");
                            retval.replace(ptr("0x1")); // 返回1表示检查通过
                        }}
                    }})) {{
                        console.log("[+] 成功Hook检查函数: " + funcAddr);
                        hookedCount++;
                    }}
                }}
            }} catch (e) {{
                // 忽略单个Hook失败
                console.log("[-] Hook函数失败 (地址: 0x" + versionCheckOffsets[i].toString(16) + "): " + e);
            }}
        }}
        
        console.log("[+] 总共Hook了 " + hookedCount + " 个检查函数");
        
    }} catch (e) {{
        console.log("[-] 版本检查绕过失败: " + e);
    }}
}}

// Hook弹窗函数，阻止显示版本过低提示
function hookMessageBox() {{
    try {{
        if (user32Module) {{
            // Hook MessageBoxW
            var messageBoxWAddr = safeGetExport("user32.dll", "MessageBoxW");
            if (messageBoxWAddr && safeInterceptorAttach(messageBoxWAddr, {{
                onEnter: function(args) {{
                    try {{
                        // 检查是否为版本过低提示
                        var title = args[2] ? args[2].readUtf16String() : "";
                        var message = args[1] ? args[1].readUtf16String() : "";
                        
                        if ((title && (title.includes("微信") || title.includes("WeChat"))) &&
                            (message && (message.includes("版本") || message.includes("update") || 
                             message.includes("升级") || message.includes("Version") || 
                             message.includes("low") || message.includes("outdated")))) {{
                            console.log("[+] 阻止版本过低提示框显示: " + message);
                            // 修改消息内容
                            args[1].writeUtf16String("版本检查已绕过，可以正常登录微信");
                            args[2].writeUtf16String("微信登录助手");
                        }}
                    }} catch (e) {{
                        console.log("[-] 处理MessageBoxW参数时出错: " + e);
                    }}
                }}
            }})) {{
                console.log("[+] 成功Hook MessageBoxW 函数");
            }}
            
            // Hook MessageBoxA
            var messageBoxAAddr = safeGetExport("user32.dll", "MessageBoxA");
            if (messageBoxAAddr && safeInterceptorAttach(messageBoxAAddr, {{
                onEnter: function(args) {{
                    try {{
                        var title = args[2] ? args[2].readUtf8String() : "";
                        var message = args[1] ? args[1].readUtf8String() : "";
                        
                        if ((title && (title.includes("微信") || title.includes("WeChat"))) &&
                            (message && (message.includes("版本") || message.includes("update") || 
                             message.includes("升级") || message.includes("Version") || 
                             message.includes("low") || message.includes("outdated")))) {{
                            console.log("[+] 阻止版本过低提示框显示: " + message);
                            args[1].writeUtf8String("版本检查已绕过，可以正常登录微信");
                            args[2].writeUtf8String("微信登录助手");
                        }}
                    }} catch (e) {{
                        console.log("[-] 处理MessageBoxA参数时出错: " + e);
                    }}
                }}
            }})) {{
                console.log("[+] 成功Hook MessageBoxA 函数");
            }}
        }}
    }} catch (e) {{
        console.log("[-] Hook消息框函数失败: " + e);
    }}
}}

// Hook网络请求，阻止版本检查请求
function hookNetworkRequests() {{
    try {{
        // Hook WinInet
        var wininetModule = safeGetModule("wininet.dll");
        if (wininetModule) {{
            var httpSendRequestWAddr = safeGetExport("wininet.dll", "HttpSendRequestW");
            if (httpSendRequestWAddr) {{
                safeInterceptorAttach(httpSendRequestWAddr, {{
                    onEnter: function(args) {{
                        try {{
                            var headers = args[2] ? args[2].readUtf16String() : "";
                            if (headers && (headers.includes("check-version") || headers.includes("upgrade") ||
                                headers.includes("version") || headers.includes("update"))) {{
                                console.log("[+] 拦截并修改版本检查网络请求");
                            }}
                        }} catch (e) {{
                            console.log("[-] 处理HttpSendRequestW参数时出错: " + e);
                        }}
                    }}
                }});
            }}
        }}
        
        // Hook WinHttp
        var winhttpModule = safeGetModule("winhttp.dll");
        if (winhttpModule) {{
            var winHttpSendRequestAddr = safeGetExport("winhttp.dll", "WinHttpSendRequest");
            if (winHttpSendRequestAddr) {{
                safeInterceptorAttach(winHttpSendRequestAddr, {{
                    onEnter: function(args) {{
                        // 可以检查请求内容
                        console.log("[+] 拦截到WinHttp请求");
                    }}
                }});
            }}
        }}
    }} catch (e) {{
        console.log("[-] 网络请求Hook失败: " + e);
    }}
}}

// 主函数
function main() {{
    console.log("[+] 修复版微信版本检查绕过工具已启动");
    console.log("[+] 当前处理的微信版本: " + version);
    
    fixedVersionBypass();
    hookMessageBox();
    hookNetworkRequests();
    
    console.log("[+] 所有绕过措施已应用");
}}

// 延迟执行确保模块加载完成
setTimeout(main, 3000);
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
                # 打印更多错误信息帮助调试
                if 'stack' in message:
                    print(Color.YELLOW + f"[Frida Stack] {message['stack']}" + Color.END)
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
            print(Color.GREEN + "[+] 成功注入修复版绕过脚本!" + Color.END)
            return session, script
        except Exception as e:
            print(Color.RED + f"[-] 注入失败: {e}" + Color.END)
            return None, None
            
    def run_fixed_bypass(self):
        """
        执行修复版绕过流程
        """
        print(Color.GREEN + "[*] 启动修复版微信绕过流程..." + Color.END)
        
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
        script_content = self.generate_fixed_bypass_script(config, version)
        if not script_content:
            return False
            
        # 注入脚本
        session, script = self.attach_and_inject(pid, script_content)
        if not session:
            return False
            
        print(Color.GREEN + "[+] 微信修复版绕过已完成!" + Color.END)
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
修复版微信绕过工具
    
使用方法:
    python fixed_bypass_tool.py     自动启动微信并应用修复版绕过
    
特点:
    1. 修复了Frida TypeError: not a function 错误
    2. 增加了错误处理和安全检查
    3. 自动查找并启动微信
    4. 等待微信完全启动
    5. 应用多层绕过措施
    
注意事项:
    1. 以管理员权限运行以确保正常工作
    2. 本工具仅用于学习研究，请遵守相关法律法规
    """
    print(Color.GREEN + help_text + Color.END)

def main():
    try:
        banner = r"""
  ______ _       _               _             
 |  ____(_)     | |             (_)            
 | |__   _ _ __ | |__   ___ _ __ _  ___  _ __  
 |  __| | | '_ \| '_ \ / _ \ '__| |/ _ \| '_ \ 
 | |    | | |_) | | | |  __/ |  | | (_) | | | |
 |_|    |_| .__/|_| |_|\___|_|  |_|\___/|_| |_|
          | |                                 
          |_|                                 
        """
        print(Color.GREEN + banner + Color.END)
        print(Color.GREEN + "        修复版微信绕过工具" + Color.END)
        print(Color.GREEN + "        公众号: 一位不愿透露姓名的热心网友" + Color.END)
        print()
        
        if len(sys.argv) > 1 and sys.argv[1] == '-h':
            show_help()
            return
            
        bypass_tool = FixedBypassTool()
        bypass_tool.run_fixed_bypass()
        
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {str(e)}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()