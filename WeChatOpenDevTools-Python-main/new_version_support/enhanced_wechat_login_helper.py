import json
import os
import sys
import psutil
import subprocess
import time
import winreg
import frida

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class EnhancedWeChatLoginHelper:
    """
    增强版微信登录助手
    自动启动微信并处理登录限制
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
            sys.exit(1)
        
    def find_wechat_installation(self):
        """
        查找微信安装路径
        """
        print(Color.GREEN + "[*] 正在查找微信安装路径..." + Color.END)
        
        # 尝试在注册表中查找
        try:
            reg_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as reg_key:
                for i in range(1024):
                    try:
                        sub_key_name = winreg.EnumKey(reg_key, i)
                        with winreg.OpenKey(reg_key, sub_key_name) as sub_key:
                            display_name, _ = winreg.QueryValueEx(sub_key, "DisplayName")
                            if "微信" in display_name or display_name == 'WeChat':
                                install_location, _ = winreg.QueryValueEx(sub_key, "InstallLocation")
                                install_location = install_location.strip('"') + "\\WeChat.exe"
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
            print(Color.YELLOW + "[*] 微信已经在运行中，正在关闭..." + Color.END)
            self.kill_wechat()
            time.sleep(2)
            
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
            
    def kill_wechat(self):
        """
        关闭微信进程
        """
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'WeChat.exe':
                    proc.kill()
                    print(Color.GREEN + f"[+] 已关闭微信进程 PID: {proc.info['pid']}" + Color.END)
        except Exception as e:
            print(Color.RED + f"[-] 关闭微信进程时出错: {e}" + Color.END)
            
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
        
    def generate_enhanced_script(self, config, version):
        """
        生成增强版登录助手脚本
        """
        script_content = f'''
// 增强版微信登录助手脚本
var version = {version};

// 安全函数定义
function safeGetModule(name) {{
    try {{
        var module = Process.findModuleByName(name);
        if (module) {{
            console.log("[+] 找到模块: " + name + " 基址: " + module.base);
            return module;
        }} else {{
            console.log("[-] 未找到模块: " + name);
            return null;
        }}
    }} catch (e) {{
        console.log("[-] 获取模块失败: " + name + ", 错误: " + e);
        return null;
    }}
}}

function safeHook(address, callbacks) {{
    try {{
        if (address) {{
            Interceptor.attach(address, callbacks);
            console.log("[+] 成功Hook地址: " + address);
            return true;
        }}
        console.log("[-] 无效的Hook地址");
        return false;
    }} catch (e) {{
        console.log("[-] Hook失败: " + e);
        return false;
    }}
}}

function safeGetExport(moduleName, funcName) {{
    try {{
        var addr = Module.findExportByName(moduleName, funcName);
        if (addr) {{
            console.log("[+] 找到导出函数: " + funcName + " 地址: " + addr);
            return addr;
        }} else {{
            console.log("[-] 未找到导出函数: " + funcName);
            return null;
        }}
    }} catch (e) {{
        console.log("[-] 获取导出函数失败: " + funcName + ", 错误: " + e);
        return null;
    }}
}}

// 增强版登录助手主函数
function enhancedLoginHelper() {{
    console.log("[+] 增强版微信登录助手已启动");
    console.log("[+] 当前处理版本: " + version);
    
    // 获取必要模块
    var wechatWin = safeGetModule("WeChatWin.dll");
    var user32 = safeGetModule("user32.dll");
    var kernel32 = safeGetModule("kernel32.dll");
    var wininet = safeGetModule("wininet.dll");
    
    // 核心功能1: 绕过版本检查
    if (wechatWin) {{
        console.log("[*] 开始处理版本检查绕过...");
        
        // 多个版本的登录相关函数地址
        var loginOffsets = [
            0x1B85600,  // 登录版本检查1
            0x1B857A0,  // 登录版本检查2
            0x26D3B38,  // SwitchVersion
            0x1A2E3F0,  // 配置检查
            0x1C02E10,  // 登录检查1
            0x1E2C500,  // 登录检查2
            0x204A900,  // 登录检查3
            0x215CB00,  // 登录检查4
            0x1B858B0,  // 版本检查1
            0x1B859C0,  // 版本检查2
            0x1B85AD0,  // 版本检查3
            0x1C02F20,  // 登录检查5
            0x1C03030   // 登录检查6
        ];
        
        var successCount = 0;
        for (var i = 0; i < loginOffsets.length; i++) {{
            try {{
                var funcAddr = wechatWin.base.add(loginOffsets[i]);
                if (safeHook(funcAddr, {{
                    onEnter: function(args) {{
                        console.log("[+] 拦截到登录检查调用: " + this.returnAddress);
                    }},
                    onLeave: function(retval) {{
                        console.log("[+] 强制登录检查通过");
                        retval.replace(ptr("0x1")); // 强制返回成功
                    }}
                }})) {{
                    successCount++;
                }}
            }} catch (e) {{
                console.log("[-] Hook登录检查函数失败: " + e);
            }}
        }}
        
        console.log("[+] 成功处理了 " + successCount + " 个登录检查点");
    }}
    
    // 核心功能2: 拦截错误提示
    if (user32) {{
        console.log("[*] 开始处理消息框拦截...");
        
        var messageBoxW = safeGetExport("user32.dll", "MessageBoxW");
        if (messageBoxW) {{
            safeHook(messageBoxW, {{
                onEnter: function(args) {{
                    try {{
                        var title = args[2] ? args[2].readUtf16String() : "";
                        var message = args[1] ? args[1].readUtf16String() : "";
                        if ((title && (title.includes("微信") || title.includes("WeChat"))) &&
                            (message && (message.includes("版本") || 
                                       message.includes("version") ||
                                       message.includes("update") ||
                                       message.includes("升级") ||
                                       message.includes("login") ||
                                       message.includes("登录")))) {{
                            console.log("[+] 拦截并修改登录相关提示");
                            console.log("    标题: " + title);
                            console.log("    内容: " + message);
                            
                            // 直接返回，不显示对话框
                            this.context.pc = this.context.lr; // 直接返回
                        }}
                    }} catch (e) {{
                        console.log("[-] 处理消息框参数时出错: " + e);
                    }}
                }}
            }});
        }}
        
        // 拦截更多消息框函数
        var messageBoxA = safeGetExport("user32.dll", "MessageBoxA");
        if (messageBoxA) {{
            safeHook(messageBoxA, {{
                onEnter: function(args) {{
                    try {{
                        var title = args[2] ? args[2].readCString() : "";
                        var message = args[1] ? args[1].readCString() : "";
                        if ((title && (title.includes("微信") || title.includes("WeChat"))) &&
                            (message && (message.includes("版本") || 
                                       message.includes("version") ||
                                       message.includes("update") ||
                                       message.includes("升级") ||
                                       message.includes("login") ||
                                       message.includes("登录")))) {{
                            console.log("[+] 拦截并修改登录相关提示 (ASCII)");
                            console.log("    标题: " + title);
                            console.log("    内容: " + message);
                            
                            // 直接返回，不显示对话框
                            this.context.pc = this.context.lr; // 直接返回
                        }}
                    }} catch (e) {{
                        console.log("[-] 处理消息框参数时出错: " + e);
                    }}
                }}
            }});
        }}
    }}
    
    // 核心功能3: 拦截网络请求检查
    console.log("[*] 开始处理网络请求拦截...");
    if (wininet) {{
        var httpSendRequestW = safeGetExport("wininet.dll", "HttpSendRequestW");
        if (httpSendRequestW) {{
            safeHook(httpSendRequestW, {{
                onEnter: function(args) {{
                    try {{
                        var headers = args[2] ? args[2].readUtf16String() : "";
                        var url = args[0] ? args[0].readPointer().readUtf16String() : "";
                        if ((headers && (headers.includes("check-version") ||
                                       headers.includes("login") ||
                                       headers.includes("upgrade") ||
                                       headers.includes("version"))) ||
                            (url && (url.includes("weixin.qq.com") ||
                                   url.includes("wechat.com") ||
                                   url.includes("check-version") ||
                                   url.includes("login")))) {{
                            console.log("[+] 拦截登录版本检查网络请求");
                            console.log("    URL: " + url);
                            
                            // 直接返回成功
                            this.context.pc = this.context.lr; // 直接返回
                        }}
                    }} catch (e) {{
                        console.log("[-] 处理网络请求参数时出错: " + e);
                    }}
                }}
            }});
        }}
        
        // 拦截更多网络函数
        var internetOpenUrlW = safeGetExport("wininet.dll", "InternetOpenUrlW");
        if (internetOpenUrlW) {{
            safeHook(internetOpenUrlW, {{
                onEnter: function(args) {{
                    try {{
                        var url = args[1] ? args[1].readUtf16String() : "";
                        if (url && (url.includes("check-version") ||
                                  url.includes("login") ||
                                  url.includes("upgrade") ||
                                  url.includes("version"))) {{
                            console.log("[+] 拦截版本检查URL请求");
                            console.log("    URL: " + url);
                            
                            // 直接返回空指针
                            this.context.x0 = ptr("0x0"); // 返回空指针
                        }}
                    }} catch (e) {{
                        console.log("[-] 处理URL请求参数时出错: " + e);
                    }}
                }}
            }});
        }}
    }}
    
    // 核心功能4: 绕过系统版本检查
    if (kernel32) {{
        console.log("[*] 开始处理系统版本检查...");
        var getVersion = safeGetExport("kernel32.dll", "GetVersion");
        if (getVersion) {{
            safeHook(getVersion, {{
                onLeave: function(retval) {{
                    console.log("[+] 修改系统版本信息");
                    // 返回一个较新的Windows版本
                    retval.replace(0x06010106); // Windows 7 (实际返回新版本)
                }}
            }});
        }}
        
        // 拦截更多版本检查函数
        var getVersionExW = safeGetExport("kernel32.dll", "GetVersionExW");
        if (getVersionExW) {{
            safeHook(getVersionExW, {{
                onEnter: function(args) {{
                    console.log("[+] 拦截系统版本详细信息请求");
                }},
                onLeave: function(retval) {{
                    console.log("[+] 修改系统版本详细信息");
                }}
            }});
        }}
    }}
    
    // 核心功能5: 绕过网络连接检查
    console.log("[*] 开始处理网络连接检查...");
    if (wininet) {{
        var internetCheckConnectionW = safeGetExport("wininet.dll", "InternetCheckConnectionW");
        if (internetCheckConnectionW) {{
            safeHook(internetCheckConnectionW, {{
                onLeave: function(retval) {{
                    console.log("[+] 强制网络连接检查通过");
                    retval.replace(1); // 强制返回连接成功
                }}
            }});
        }}
    }}
    
    console.log("[+] 增强版微信登录助手已完成所有设置");
    console.log("[*] 请尝试登录微信");
}}

// 立即执行
setImmediate(enhancedLoginHelper);
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
            print(Color.GREEN + "[+] 成功注入增强版登录助手脚本!" + Color.END)
            return session, script
        except Exception as e:
            print(Color.RED + f"[-] 注入失败: {e}" + Color.END)
            return None, None
            
    def run_enhanced_login_helper(self):
        """
        运行增强版登录助手
        """
        print(Color.GREEN + "[*] 启动增强版微信登录助手..." + Color.END)
        
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
            
        # 生成助手脚本
        script_content = self.generate_enhanced_script(config, version)
        if not script_content:
            return False
            
        # 注入脚本
        session, script = self.attach_and_inject(pid, script_content)
        if not session:
            return False
            
        print(Color.GREEN + "[+] 增强版微信登录助手已就绪!" + Color.END)
        print(Color.YELLOW + "[*] 请在微信登录界面尝试登录" + Color.END)
        print(Color.YELLOW + "[*] 工具将在后台持续运行以保持效果" + Color.END)
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
增强版微信登录助手
    
使用方法:
    python enhanced_wechat_login_helper.py     自动启动微信并处理登录限制
    
特点:
    1. 自动启动微信并处理登录限制
    2. 绕过版本检查和网络验证
    3. 拦截并修改错误提示信息
    4. 持续在后台运行保持效果
    5. 增强了对更多函数的Hook处理
    
注意事项:
    1. 以管理员权限运行以确保正常工作
    2. 本工具仅用于学习研究，请遵守相关法律法规
    """
    print(Color.GREEN + help_text + Color.END)

def main():
    try:
        banner = r"""
  ______                       _    _       _   _                 
 |  ____|                     | |  | |     | | | |                
 | |__   _ __   __ _ _ __   __| |  | | __ _| |_| |__   ___  _ __  
 |  __| | '_ \ / _` | '_ \ / _` |  | |/ _` | __| '_ \ / _ \| '_ \ 
 | |____| | | | (_| | | | | (_| |  | | (_| | |_| | | | (_) | | | |
 |______|_| |_|\__,_|_| |_|\__,_|  |_|\__,_|\__|_| |_|\___/|_| |_|
                                                                 
        """
        print(Color.GREEN + banner + Color.END)
        print(Color.GREEN + "        增强版微信登录助手" + Color.END)
        print(Color.GREEN + "        公众号: 一位不愿透露姓名的热心网友" + Color.END)
        print()
        
        if len(sys.argv) > 1 and sys.argv[1] == '-h':
            show_help()
            return
            
        helper = EnhancedWeChatLoginHelper()
        helper.run_enhanced_login_helper()
        
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {str(e)}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()