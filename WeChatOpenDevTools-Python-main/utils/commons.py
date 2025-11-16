# commons.py
from utils.colors import Color
from utils.wechatutils import WechatUtils
import frida
import sys
import time
import platform
import os

class Commons:
    def __init__(self):
        self.wechatutils_instance = WechatUtils()
        self.device = frida.get_local_device()
        self.process = self.device.enumerate_processes()
        self.version_list = []
        self.configs_path = ""
        self.active_sessions = []

    def onMessage(self, message, data):
        if message['type'] == 'send':
            print(Color.GREEN + message['payload'], Color.END)
        elif message['type'] == 'error':
            print(Color.RED + message['stack'], Color.END)

    def inject_wechatEx(self, pid, code):
        try:
            session = frida.attach(pid)
            script = session.create_script(code)
            script.on("message", self.onMessage)
            script.load()
            print(Color.GREEN + f"[+] 成功注入微信PID: {pid}", Color.END)
            return session
        except Exception as e:
            print(Color.RED + f"[-] 注入微信失败PID {pid}: {e}", Color.END)
            return None

    def inject_wechatDLL(self, path, code):
        pid = self.device.spawn(path)
        session = frida.attach(pid)
        script = session.create_script(code)
        script.on("message", self.onMessage)
        script.load()
        self.device.resume(pid)
        time.sleep(10)
        session.detach()

    def load_wechatEx_configs(self):
        path = self.wechatutils_instance.get_configs_path()
        if get_cpu_architecture() == "MacOS x64":
            wechat_instances = self.wechatutils_instance.get_wechat_pids_and_versions_mac()
        else:
            wechat_instances = self.wechatutils_instance.get_wechat_pids_and_versions()

        if wechat_instances:
            for pid, version in wechat_instances:
                try:
                    # 对于微信4.1.0版本(13080813)使用专用的hook脚本
                    if version == 13080813:
                        # 优先使用综合hook脚本，如果不存在则使用普通410脚本
                        if os.path.exists(path + "../scripts/comprehensive_hook_410.js"):
                            wechatEx_hookcode = open(path + "../scripts/comprehensive_hook_410.js", "r", encoding="utf-8").read()
                            send_message = "[+] 正在使用综合调试方案"
                        else:
                            wechatEx_hookcode = open(path + "../scripts/hook_410.js", "r", encoding="utf-8").read()
                            send_message = "[+] 正在使用标准调试方案"
                    else:
                        wechatEx_hookcode = open(path + "../scripts/hook.js", "r", encoding="utf-8").read()
                        send_message = "[+] 正在使用兼容调试方案"
                        
                    # 尝试匹配版本配置文件，如果没有匹配的则使用默认配置
                    config_file = f"../configs/address_{version}_x64.json"
                    if not os.path.exists(path + config_file):
                        # 使用最新版本配置文件
                        config_file = "../configs/address_13080813_x64.json"
                    
                    wechatEx_addresses = open(path + config_file).read()
                    wechatEx_hookcode = "var address=" + wechatEx_addresses + wechatEx_hookcode
                    session = self.inject_wechatEx(pid, wechatEx_hookcode)
                    if session:
                        self.active_sessions.append(session)
                    print(Color.GREEN +f"[+] 成功注入小程序版本，PID: {pid}", Color.END)
                    print(Color.GREEN + send_message, Color.END)
                except Exception as e:
                    print(Color.RED + f"[-] 注入小程序版本失败: {e}！", Color.END)
        else:
            self.wechatutils_instance.print_process_not_found_message()

        # 管理会话
        if self.active_sessions:
            print(Color.YELLOW + "\n[*] 按 Ctrl+C 停止监听或关闭微信" + Color.END)
            try:
                while self.active_sessions:
                    self.manage_sessions()
                    time.sleep(5)  # 每5秒检查一次
            except KeyboardInterrupt:
                print(Color.YELLOW + "\n[!] 用户中断监听" + Color.END)
        else:
            try:
                input(Color.YELLOW + "\n按回车键返回..." + Color.END)
            except:
                pass

    def load_wechatEx_cookie_hook(self):
        path = self.wechatutils_instance.get_configs_path()
        if get_cpu_architecture() == "MacOS x64":
            wechat_instances = self.wechatutils_instance.get_wechat_pids_and_versions_mac()
        else:
            wechat_instances = self.wechatutils_instance.get_wechat_pids_and_versions()

        if wechat_instances:
            for pid, version in wechat_instances:
                try:
                    cookie_hook_code = open(path + "../scripts/cookie_hook.js", "r", encoding="utf-8").read()
                    session = self.inject_wechatEx(pid, cookie_hook_code)
                    if session:
                        self.active_sessions.append(session)
                    print(Color.GREEN +f"[+] 成功注入小程序Cookie监控，PID: {pid}", Color.END)
                except Exception as e:
                    print(Color.RED + f"[-] 注入小程序Cookie监控失败！", Color.END)
        else:
            self.wechatutils_instance.print_process_not_found_message()

        # 管理会话
        if self.active_sessions:
            print(Color.YELLOW + "\n[*] 按 Ctrl+C 停止监听或关闭微信" + Color.END)
            try:
                while self.active_sessions:
                    self.manage_sessions()
                    time.sleep(5)  # 每5秒检查一次
            except KeyboardInterrupt:
                print(Color.YELLOW + "\n[!] 用户中断监听" + Color.END)
        else:
            try:
                input(Color.YELLOW + "\n按回车键返回..." + Color.END)
            except:
                pass

    def load_wechatEXE_configs(self):
        wechat_instances = self.wechatutils_instance.get_wechat_pids_and_versions()
        if wechat_instances:
            print(Color.RED + f"[-] 请退出所有微信实例后再执行该命令 " + Color.END)
            try:
                input(Color.YELLOW + "\n按回车键返回..." + Color.END)
            except:
                pass
            return 0
        
        wechatEXEpath = self.wechatutils_instance.find_installation_path("微信")
        path = self.wechatutils_instance.get_configs_path()
        wechatEXE_hookcode = open(path + "..\\scripts\\WechatWin.dll\\hook.js", "r", encoding="utf-8").read()
        self.inject_wechatDLL(wechatEXEpath, wechatEXE_hookcode)
        try:
            input(Color.YELLOW + "\n按回车键返回..." + Color.END)
        except:
            pass

    def load_wechatEXE_and_wechatEx(self):
        wechat_instances = self.wechatutils_instance.get_wechat_pids_and_versions()
        if wechat_instances:
            print(Color.RED + f"[-] 请关闭所有微信实例后再执行该命令 " + Color.END)
            try:
                input(Color.YELLOW + "\n按回车键返回..." + Color.END)
            except:
                pass
            return 0
        self.load_wechatEXE_configs()
        self.load_wechatEx_configs()

    def manage_sessions(self):
        for session in self.active_sessions[:]:  # 使用切片创建副本以便在迭代时修改
            if session.is_detached:
                print(f"Session {session} detached, removing from active sessions.")
                self.active_sessions.remove(session)

def get_cpu_architecture():
    try:
        cpu_arch = platform.platform().lower()
        if "64bit" in cpu_arch and "macos" in cpu_arch:
            return "MacOS x64"
        return "Windows"  # 默认返回Windows
    except Exception as e:
        print(Color.RED, f"[-] Error detecting CPU architecture: {e} ", Color.END)
        return "Windows"

# 主函数示例
if __name__ == "__main__":
    commons = Commons()
    commons.load_wechatEx_configs()