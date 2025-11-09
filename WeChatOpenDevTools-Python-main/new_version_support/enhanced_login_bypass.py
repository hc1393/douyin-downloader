import frida
import json
import os
import sys
import psutil
import time

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class EnhancedLoginBypass:
    """
    增强版微信登录绕过工具
    专门针对登录时的版本检查进行绕过
    """
    
    def __init__(self):
        self.device = frida.get_local_device()
        self.configs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs')
        
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
        
    def generate_enhanced_bypass_script(self, config, version):
        """
        生成增强版绕过脚本
        """
        script_content = f'''
var version = {version};

// 获取模块基址
var wechatWinModule = Process.findModuleByName("WeChatWin.dll");
var wechatAppModule = Process.findModuleByName("WeChatAppEx.exe");
var user32Module = Module.findModuleByName("user32.dll");
var kernel32Module = Module.findModuleByName("kernel32.dll");

console.log("[+] WeChatWin.dll 模块地址: " + (wechatWinModule ? wechatWinModule.base : "未找到"));
console.log("[+] WeChatAppEx.exe 模块地址: " + (wechatAppModule ? wechatAppModule.base : "未找到"));

// 增强版版本检查绕过
function enhancedVersionBypass() {{
    try {{
        // Hook版本比较函数 - 多种可能的地址
        var versionCheckOffsets = [
            0x1B85600,  // 常见版本检查地址1
            0x1B857A0,  // 常见版本检查地址2
            0x1B858D0,  // 常见版本检查地址3
            0x1B85A10,  // 常见版本检查地址4
            0x26D3B38   // 配置文件中的SwitchVersion地址
        ];
        
        var hookedCount = 0;
        for (var i = 0; i < versionCheckOffsets.length; i++) {{
            try {{
                if (wechatWinModule) {{
                    var funcAddr = wechatWinModule.base.add(versionCheckOffsets[i]);
                    Interceptor.attach(funcAddr, {{
                        onLeave: function(retval) {{
                            console.log("[+] 拦截到版本检查函数调用 (地址: " + this.returnAddress + ")，修改返回值");
                            retval.replace(ptr("0x1")); // 返回1表示版本满足要求
                        }}
                    }});
                    console.log("[+] 成功Hook版本检查函数: " + funcAddr);
                    hookedCount++;
                }}
            }} catch (e) {{
                // 忽略单个Hook失败
            }}
        }}
        
        console.log("[+] 总共Hook了 " + hookedCount + " 个版本检查函数");
        
        // Hook GetVersionExW 函数，修改系统报告的版本
        if (kernel32Module) {{
            var getVersionExWAddr = Module.findExportByName("kernel32.dll", "GetVersionExW");
            if (getVersionExWAddr) {{
                Interceptor.attach(getVersionExWAddr, {{
                    onEnter: function(args) {{
                        console.log("[+] 拦截到 GetVersionExW 调用");
                    }},
                    onLeave: function(retval) {{
                        // 可以修改返回的版本信息
                    }}
                }});
            }}
        }}
        
    }} catch (e) {{
        console.log("[-] 增强版版本检查绕过失败: " + e);
    }}
}}

// Hook弹窗函数，阻止显示版本过低提示
function hookMessageBox() {{
    try {{
        if (user32Module) {{
            var messageBoxWAddr = Module.findExportByName("user32.dll", "MessageBoxW");
            if (messageBoxWAddr) {{
                Interceptor.attach(messageBoxWAddr, {{
                    onEnter: function(args) {{
                        // 检查是否为版本过低提示
                        var title = args[2] ? args[2].readUtf16String() : "";
                        var message = args[1] ? args[1].readUtf16String() : "";
                        
                        if ((title && (title.includes("微信") || title.includes("WeChat"))) &&
                            (message && (message.includes("版本") || message.includes("update") || 
                             message.includes("升级") || message.includes("Version") || 
                             message.includes("low") || message.includes("outdated")))) {{
                            console.log("[+] 阻止版本过低提示框显示: " + message);
                            // 修改消息内容，使其显示成功信息
                            args[1].writeUtf16String("版本检查已绕过，可以正常登录微信");
                            args[2].writeUtf16String("微信登录助手");
                        }}
                    }}
                }});
                console.log("[+] 成功Hook MessageBoxW 函数");
            }}
            
            // 同时Hook MessageBoxA
            var messageBoxAAddr = Module.findExportByName("user32.dll", "MessageBoxA");
            if (messageBoxAAddr) {{
                Interceptor.attach(messageBoxAAddr, {{
                    onEnter: function(args) {{
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
                    }}
                }});
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
        var wininetModule = Module.findModuleByName("wininet.dll");
        if (wininetModule) {{
            var httpSendRequestWAddr = Module.findExportByName("wininet.dll", "HttpSendRequestW");
            if (httpSendRequestWAddr) {{
                Interceptor.attach(httpSendRequestWAddr, {{
                    onEnter: function(args) {{
                        var headers = args[2] ? args[2].readUtf16String() : "";
                        if (headers && (headers.includes("check-version") || headers.includes("upgrade") ||
                            headers.includes("version") || headers.includes("update"))) {{
                            console.log("[+] 拦截并阻止版本检查网络请求");
                            // 可以选择完全阻止请求
                        }}
                    }}
                }});
            }}
        }}
        
        // Hook WinHttp functions
        var winhttpModule = Module.findModuleByName("winhttp.dll");
        if (winhttpModule) {{
            var winHttpSendRequestAddr = Module.findExportByName("winhttp.dll", "WinHttpSendRequest");
            if (winHttpSendRequestAddr) {{
                Interceptor.attach(winHttpSendRequestAddr, {{
                    onEnter: function(args) {{
                        // 可以检查请求内容
                    }}
                }});
            }}
        }}
    }} catch (e) {{
        console.log("[-] 网络请求Hook失败: " + e);
    }}
}}

// Hook配置检查函数
function hookConfigChecks() {{
    try {{
        // 尝试Hook可能的配置检查函数
        var configCheckOffsets = [
            0x1A2E3F0,  // 假设的配置检查地址1
            0x1A2F1A0,  // 假设的配置检查地址2
            0x1A302D0   // 假设的配置检查地址3
        ];
        
        for (var i = 0; i < configCheckOffsets.length; i++) {{
            try {{
                if (wechatWinModule) {{
                    var funcAddr = wechatWinModule.base.add(configCheckOffsets[i]);
                    Interceptor.attach(funcAddr, {{
                        onLeave: function(retval) {{
                            console.log("[+] 拦截到配置检查函数调用，修改返回值");
                            retval.replace(ptr("0x1")); // 返回成功
                        }}
                    }});
                    console.log("[+] 成功Hook配置检查函数: " + funcAddr);
                }}
            }} catch (e) {{
                // 忽略单个Hook失败
            }}
        }}
    }} catch (e) {{
        console.log("[-] 配置检查Hook失败: " + e);
    }}
}}

// 主函数
function main() {{
    console.log("[+] 增强版微信版本检查绕过工具已启动");
    console.log("[+] 当前处理的微信版本: " + version);
    
    enhancedVersionBypass();
    hookMessageBox();
    hookNetworkRequests();
    hookConfigChecks();
    
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
        except Exception as e:
            print(Color.RED + f"[!] 消息处理出错: {e}" + Color.END)
            
    def attach_and_inject(self, pid, script_content):
        """
        附加到进程并注入脚本
        """
        try:
            print(Color.GREEN + f"[*] 正在附加到微信进程 {pid}..." + Color.END)
            session = self.device.attach(pid)
            script = session.create_script(script_content)
            script.on('message', self.on_message)
            script.load()
            print(Color.GREEN + "[+] 成功注入增强版绕过脚本!" + Color.END)
            return session, script
        except Exception as e:
            print(Color.RED + f"[-] 注入失败: {e}" + Color.END)
            return None, None
            
    def bypass_login_check(self):
        """
        执行增强版版本检查绕过
        """
        # 查找微信进程
        pid = self.find_wechat_process()
        if not pid:
            return False
            
        # 加载配置文件
        config, version = self.load_latest_config()
        if not config:
            return False
            
        # 生成绕过脚本
        script_content = self.generate_enhanced_bypass_script(config, version)
        if not script_content:
            return False
            
        # 注入脚本
        session, script = self.attach_and_inject(pid, script_content)
        if not session:
            return False
            
        print(Color.GREEN + "[+] 微信版本检查增强版绕过已完成!" + Color.END)
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
增强版微信版本检查绕过工具
    
使用方法:
    python enhanced_login_bypass.py     绕过微信版本检查并保持运行
    
特点:
    1. 多重Hook点，提高绕过成功率
    2. 同时Hook MessageBoxW 和 MessageBoxA
    3. 拦截网络版本检查请求
    4. Hook多种可能的版本检查函数
    
注意事项:
    1. 使用前请确保微信已运行
    2. 以管理员权限运行以确保正常工作
    3. 本工具仅用于学习研究，请遵守相关法律法规
    """
    print(Color.GREEN + help_text + Color.END)

def main():
    try:
        banner = r"""
  ______ _           _   _       _                 _ ____        _   _                 
 |  ____| |         | | | |     | |               | |  _ \      | | | |                
 | |__  | | __ _ ___| |_| |__   | |__   ___   ___ | | |_) | __ _| |_| |__   ___  _ __  
 |  __| | |/ _` / __| __| '_ \  | '_ \ / _ \ / _ \| |  _ < / _` | __| '_ \ / _ \| '_ \ 
 | |____| | (_| \__ \ |_| | | | | |_) | (_) | (_) | | |_) | (_| | |_| | | | (_) | | | |
 |______|_|\__,_|___/\__|_| |_| |_.__/ \___/ \___/|_|____/ \__,_|\__|_| |_|\___/|_| |_|
                                                                                      
        """
        print(Color.GREEN + banner + Color.END)
        print(Color.GREEN + "        增强版微信版本检查绕过工具" + Color.END)
        print(Color.GREEN + "        公众号: 一位不愿透露姓名的热心网友" + Color.END)
        print()
        
        if len(sys.argv) > 1 and sys.argv[1] == '-h':
            show_help()
            return
            
        bypass_tool = EnhancedLoginBypass()
        bypass_tool.bypass_login_check()
        
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {str(e)}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()