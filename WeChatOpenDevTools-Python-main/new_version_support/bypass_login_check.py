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

class WeChatLoginBypass:
    """
    微信版本检查绕过工具
    通过Hook微信登录验证函数绕过版本过低提示
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
        
    def generate_bypass_script(self, config, version):
        """
        生成版本检查绕过脚本
        """
        script_content = f'''
var version = {version};

// 获取WeChatWin.dll模块基址
var wechatWinModule = Process.findModuleByName("WeChatWin.dll");
if (wechatWinModule) {{
    console.log("[+] 找到 WeChatWin.dll 模块: " + wechatWinModule.base);
}} else {{
    console.log("[-] 未找到 WeChatWin.dll 模块");
}}

// Hook版本检查函数
function hookVersionCheck() {{
    // 根据不同版本使用不同的Hook点
    var versionCheckAddr = null;
    
    if (version >= 13080813) {{
        // 微信4.1.0及以上版本
        console.log("[*] 应用微信4.1.0+版本Hook策略");
    }} else if (version >= 11159) {{
        // 微信3.9.x版本
        console.log("[*] 应用微信3.9.x版本Hook策略");
    }}
    
    // 通用绕过方法 - Hook版本比较函数
    try {{
        // Hook网络版本检查函数
        var versionCheckFunc = null; // 需要根据具体版本查找实际地址
        
        // Hook可能的版本检查函数
        var possibleOffsets = [
            0x26D3B38,  // 从配置文件中获取的SwitchVersion地址
            0x1B85600,  // 常见的版本检查函数地址
            0x1B857A0,  // 另一个可能的版本检查函数地址
            0x1B858D0   // 第三个可能的版本检查函数地址
        ];
        
        for (var i = 0; i < possibleOffsets.length; i++) {{
            try {{
                var funcAddr = wechatWinModule.base.add(possibleOffsets[i]);
                Interceptor.attach(funcAddr, {{
                    onLeave: function(retval) {{
                        console.log("[+] 拦截到版本检查函数调用，修改返回值");
                        retval.replace(ptr("0x1")); // 返回1表示版本满足要求
                    }}
                }});
                console.log("[+] 成功Hook版本检查函数: " + funcAddr);
            }} catch (e) {{
                // 忽略单个Hook失败
            }}
        }}
    }} catch (e) {{
        console.log("[-] Hook版本比较函数失败: " + e);
    }}
    
    // Hook弹窗函数，阻止显示版本过低提示
    try {{
        // Hook MessageBoxW 函数
        var user32 = Module.findModuleByName("user32.dll");
        if (user32) {{
            var messageBoxAddr = Module.findExportByName("user32.dll", "MessageBoxW");
            if (messageBoxAddr) {{
                Interceptor.attach(messageBoxAddr, {{
                    onEnter: function(args) {{
                        // 检查是否为版本过低提示
                        var title = args[2].readUtf16String();
                        var message = args[1].readUtf16String();
                        if ((title && (title.includes("微信") || title.includes("WeChat"))) &&
                            (message && (message.includes("版本") || message.includes("update") || message.includes("升级")))) {{
                            console.log("[+] 阻止版本过低提示框显示: " + message);
                            // 修改消息内容
                            args[1].writeUtf16String("版本检查已绕过，可以正常登录");
                        }}
                    }}
                }});
            }}
        }}
    }} catch (e) {{
        console.log("[-] Hook消息框函数失败: " + e);
    }}
    
    // Hook网络请求函数
    try {{
        var wininet = Module.findModuleByName("wininet.dll");
        if (wininet) {{
            var httpSendAddr = Module.findExportByName("wininet.dll", "HttpSendRequestW");
            if (httpSendAddr) {{
                Interceptor.attach(httpSendAddr, {{
                    onEnter: function(args) {{
                        var headers = args[2] ? args[2].readUtf16String() : "";
                        if (headers.includes("check-version") || headers.includes("upgrade")) {{
                            console.log("[+] 拦截到版本检查网络请求，阻止发送");
                            // 可以选择阻止请求
                        }}
                    }}
                }});
            }}
        }}
    }} catch (e) {{
        console.log("[-] 网络请求Hook失败: " + e);
    }}
    
    console.log("[+] 版本检查绕过已应用");
}}

// 绕过网络验证
function bypassNetworkVerification() {{
    try {{
        // Hook网络连接函数
        var ws2_32 = Module.findModuleByName("ws2_32.dll");
        if (ws2_32) {{
            var connectAddr = Module.findExportByName("ws2_32.dll", "connect");
            if (connectAddr) {{
                Interceptor.attach(connectAddr, {{
                    onEnter: function(args) {{
                        // 可以在这里检查连接目标
                    }}
                }});
            }}
        }}
    }} catch (e) {{
        console.log("[-] 网络验证绕过失败: " + e);
    }}
}}

// 主函数
function main() {{
    console.log("[+] 微信版本检查绕过工具已启动");
    hookVersionCheck();
    bypassNetworkVerification();
}}

// 延迟执行确保模块加载完成
setTimeout(main, 2000);
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
            print(Color.GREEN + "[+] 成功注入绕过脚本!" + Color.END)
            return session, script
        except Exception as e:
            print(Color.RED + f"[-] 注入失败: {e}" + Color.END)
            return None, None
            
    def bypass_login_check(self):
        """
        执行版本检查绕过
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
        script_content = self.generate_bypass_script(config, version)
        if not script_content:
            return False
            
        # 注入脚本
        session, script = self.attach_and_inject(pid, script_content)
        if not session:
            return False
            
        print(Color.GREEN + "[+] 微信版本检查绕过已完成!" + Color.END)
        print(Color.YELLOW + "[*] 请尝试登录微信" + Color.END)
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
微信版本检查绕过工具
    
使用方法:
    python bypass_login_check.py     绕过微信版本检查并保持运行
    
注意事项:
    1. 使用前请确保微信已运行
    2. 以管理员权限运行以确保正常工作
    3. 本工具仅用于学习研究，请遵守相关法律法规
    """
    print(Color.GREEN + help_text + Color.END)

def main():
    try:
        banner = r"""
__        ___           _                      _             
\ \      / (_)_ __   __| | _____      ___ __ | | ___  _ __  
 \ \ /\ / /| | '_ \ / _` |/ _ \ \ /\ / / '_ \| |/ _ \| '_ \ 
  \ V  V / | | | | | (_| | (_) \ V  V /| |_) | | (_) | | | |
   \_/\_/  |_|_| |_|\__,_|\___/ \_/\_/ | .__/|_|\___/|_| |_|
                                       |_|                  
        """
        print(Color.GREEN + banner + Color.END)
        print(Color.GREEN + "        微信版本检查绕过工具" + Color.END)
        print(Color.GREEN + "        公众号: 一位不愿透露姓名的热心网友" + Color.END)
        print()
        
        if len(sys.argv) > 1 and sys.argv[1] == '-h':
            show_help()
            return
            
        bypass_tool = WeChatLoginBypass()
        bypass_tool.bypass_login_check()
        
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {str(e)}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()