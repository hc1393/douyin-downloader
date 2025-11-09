import os
import json
import psutil
import subprocess
import time
from utils.commons import Commons
from utils.colors import Color

class WeChat410Adapter:
    def __init__(self):
        self.commons = Commons()
        self.target_version = 13080813  # 微信4.1.0版本号
        
    def check_wechat_running(self):
        """检查微信是否正在运行"""
        try:
            wechat_instances = self.commons.wechatutils_instance.get_wechat_pids_and_versions()
            wechat_410_instances = [(pid, version) for pid, version in wechat_instances if version == self.target_version]
            
            if wechat_410_instances:
                print(Color.GREEN + f"[+] 检测到微信4.1.0进程，PID: {[pid for pid, version in wechat_410_instances]}" + Color.END)
                return wechat_410_instances
            else:
                print(Color.YELLOW + "[-] 未检测到微信4.1.0进程" + Color.END)
                return []
        except Exception as e:
            print(Color.RED + f"[-] 检查微信进程时出错: {e}" + Color.END)
            return []

    def inject_frida_script(self):
        """使用Frida注入脚本以启用调试功能"""
        try:
            print(Color.YELLOW + "[*] 正在为微信4.1.0注入调试脚本..." + Color.END)
            
            # 获取配置路径
            path = self.commons.wechatutils_instance.get_configs_path()
            
            # 获取微信4.1.0进程
            wechat_instances = self.check_wechat_running()
            
            if not wechat_instances:
                print(Color.RED + "[-] 请先启动微信4.1.0" + Color.END)
                return False
                
            success_count = 0
            for pid, version in wechat_instances:
                try:
                    # 读取hook脚本
                    wechatEx_hookcode = open(path + "../scripts/hook.js", "r", encoding="utf-8").read()
                    wechatEx_addresses = open(path + f"../configs/address_{version}_x64.json").read()
                    wechatEx_hookcode = "var address=" + wechatEx_addresses + wechatEx_hookcode
                    
                    # 注入脚本
                    session = self.commons.inject_wechatEx(pid, wechatEx_hookcode)
                    if session:
                        self.commons.active_sessions.append(session)
                        print(Color.GREEN + f"[+] 成功为PID {pid} 注入调试脚本" + Color.END)
                        success_count += 1
                    else:
                        print(Color.RED + f"[-] 为PID {pid} 注入调试脚本失败" + Color.END)
                        
                except Exception as e:
                    print(Color.RED + f"[-] 注入过程出错: {e}" + Color.END)
            
            if success_count > 0:
                print(Color.GREEN + f"[+] 成功为 {success_count} 个微信进程注入调试脚本" + Color.END)
                return True
            else:
                print(Color.RED + "[-] 所有注入尝试均失败" + Color.END)
                return False
                
        except Exception as e:
            print(Color.RED + f"[-] 注入脚本时发生错误: {e}" + Color.END)
            return False

    def start_wechat_if_needed(self):
        """如果微信未运行则启动它"""
        instances = self.check_wechat_running()
        if not instances:
            print(Color.YELLOW + "[*] 正在启动微信4.1.0..." + Color.END)
            try:
                # 查找微信安装路径
                wechat_path = self.commons.wechatutils_instance.find_installation_path("微信")
                if not wechat_path or not os.path.exists(wechat_path):
                    print(Color.RED + "[-] 未找到微信安装路径" + Color.END)
                    return False
                    
                # 启动微信
                subprocess.Popen([wechat_path])
                print(Color.GREEN + "[+] 微信启动命令已发送，等待微信启动..." + Color.END)
                time.sleep(5)  # 等待微信启动
                return True
            except Exception as e:
                print(Color.RED + f"[-] 启动微信时出错: {e}" + Color.END)
                return False
        return True

    def enable_debug_features(self):
        """启用调试功能的主要方法"""
        print(Color.GREEN + """
====================================
微信4.1.0调试功能启用工具
====================================
        """ + Color.END)
        
        # 确保微信正在运行
        if not self.start_wechat_if_needed():
            return False
            
        # 等待微信完全启动
        print(Color.YELLOW + "[*] 等待微信完全启动..." + Color.END)
        time.sleep(3)
        
        # 注入调试脚本
        if self.inject_frida_script():
            print(Color.GREEN + """
[*] 调试功能已启用
====================================
使用说明：
1. 打开任意小程序
2. 按 F12 键启用调试
3. 如果F12无效，尝试右键点击小程序界面
4. 如果仍然无效，可能需要使用微信官方开发者工具

注意：微信4.1.0可能已加强安全限制，
传统调试方法可能无法正常工作。
            """ + Color.END)
            return True
        else:
            print(Color.RED + """
[-] 调试功能启用失败
====================================
可能的原因：
1. 微信4.1.0已禁用非官方调试方法
2. Frida注入被安全软件拦截
3. 配置文件不匹配

建议使用微信官方开发者工具：
https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
            """ + Color.END)
            return False

def main():
    adapter = WeChat410Adapter()
    try:
        adapter.enable_debug_features()
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"\n[-] 程序运行出错: {e}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()