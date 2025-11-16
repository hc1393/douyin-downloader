#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
微信4.1.0调试功能启用器
专门针对微信4.1.0版本(版本号13080813)的调试功能启用工具
"""

import os
import sys
import json
import time
import psutil
from utils.commons import Commons
from utils.colors import Color
from utils.wechatutils import WechatUtils

class WeChat410DebugEnabler:
    def __init__(self):
        self.commons = Commons()
        self.wechat_utils = WechatUtils()
        self.target_version = 13080813  # 微信4.1.0版本号
        
    def check_frida_available(self):
        """检查Frida是否可用"""
        try:
            import frida
            print(Color.GREEN + "[+] Frida库可用" + Color.END)
            return True
        except ImportError:
            print(Color.RED + "[-] 未安装Frida库，请先安装: pip install frida" + Color.END)
            return False
            
    def find_wechat_410_process(self):
        """查找微信4.1.0进程"""
        try:
            # 获取所有微信进程
            wechat_instances = self.wechat_utils.get_wechat_pids_and_versions()
            
            # 筛选4.1.0版本进程
            wechat_410_instances = [
                (pid, version) for pid, version in wechat_instances 
                if version == self.target_version
            ]
            
            if wechat_410_instances:
                print(Color.GREEN + f"[+] 找到 {len(wechat_410_instances)} 个微信4.1.0进程" + Color.END)
                for pid, version in wechat_410_instances:
                    print(Color.GREEN + f"    PID: {pid}, 版本: {version}" + Color.END)
                return wechat_410_instances
            else:
                print(Color.YELLOW + "[-] 未找到微信4.1.0进程" + Color.END)
                return []
                
        except Exception as e:
            print(Color.RED + f"[-] 查找微信进程时出错: {e}" + Color.END)
            return []
            
    def start_wechat_410(self):
        """启动微信4.1.0"""
        try:
            print(Color.YELLOW + "[*] 正在查找微信4.1.0安装路径..." + Color.END)
            
            # 查找微信安装路径
            install_path = self.wechat_utils.find_installation_path("微信")
            
            # 如果通过注册表未找到，尝试常见路径
            if not install_path or not os.path.exists(install_path):
                common_paths = [
                    r"D:\Weixin\WeChat.exe",
                    r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",
                    r"C:\Program Files\Tencent\WeChat\WeChat.exe"
                ]
                
                for path in common_paths:
                    if os.path.exists(path):
                        install_path = path
                        break
            
            if not install_path or not os.path.exists(install_path):
                print(Color.RED + "[-] 未找到微信安装路径" + Color.END)
                return False
                
            print(Color.GREEN + f"[+] 微信安装路径: {install_path}" + Color.END)
            
            # 检查是否已经是4.1.0版本
            # 这里简单地启动微信，实际版本检查需要更复杂的逻辑
            print(Color.YELLOW + "[*] 正在启动微信..." + Color.END)
            
            # 关闭现有微信进程
            self.kill_wechat_processes()
            
            # 启动微信
            os.startfile(install_path)
            print(Color.GREEN + "[+] 微信启动命令已发送" + Color.END)
            
            # 等待微信启动
            print(Color.YELLOW + "[*] 等待微信启动完成 (约10秒)..." + Color.END)
            time.sleep(10)
            
            return True
            
        except Exception as e:
            print(Color.RED + f"[-] 启动微信时出错: {e}" + Color.END)
            return False
            
    def kill_wechat_processes(self):
        """关闭所有微信进程"""
        try:
            killed_count = 0
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if 'WeChat' in proc.info['name'] or 'wechat' in proc.info['name']:
                        proc.kill()
                        print(Color.GREEN + f"[+] 已关闭进程: {proc.info['name']} (PID: {proc.info['pid']})" + Color.END)
                        killed_count += 1
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
                    
            if killed_count > 0:
                print(Color.YELLOW + f"[*] 共关闭 {killed_count} 个微信进程，等待3秒..." + Color.END)
                time.sleep(3)
            else:
                print(Color.GREEN + "[+] 未发现微信进程" + Color.END)
                
        except Exception as e:
            print(Color.RED + f"[-] 关闭微信进程时出错: {e}" + Color.END)
            
    def inject_debug_script(self, pid):
        """为指定PID的微信进程注入调试脚本"""
        try:
            print(Color.YELLOW + f"[*] 正在为PID {pid} 注入调试脚本..." + Color.END)
            
            # 获取配置路径
            configs_path = self.wechat_utils.get_configs_path()
            
            # 读取hook脚本
            hook_script_path = os.path.join(configs_path, "..", "scripts", "hook.js")
            if not os.path.exists(hook_script_path):
                print(Color.RED + f"[-] Hook脚本不存在: {hook_script_path}" + Color.END)
                return None
                
            with open(hook_script_path, "r", encoding="utf-8") as f:
                hook_code = f.read()
                
            # 读取地址配置
            address_config_path = os.path.join(configs_path, f"address_{self.target_version}_x64.json")
            if not os.path.exists(address_config_path):
                print(Color.RED + f"[-] 地址配置文件不存在: {address_config_path}" + Color.END)
                return None
                
            with open(address_config_path, "r", encoding="utf-8") as f:
                address_config = f.read()
                
            # 组合脚本
            full_script = "var address=" + address_config + hook_code
            
            # 注入脚本
            session = self.commons.inject_wechatEx(pid, full_script)
            if session:
                print(Color.GREEN + f"[+] 成功为PID {pid} 注入调试脚本" + Color.END)
                return session
            else:
                print(Color.RED + f"[-] 为PID {pid} 注入调试脚本失败" + Color.END)
                return None
                
        except Exception as e:
            print(Color.RED + f"[-] 注入调试脚本时出错: {e}" + Color.END)
            return None
            
    def enable_debug(self):
        """启用微信4.1.0调试功能主函数"""
        print(Color.GREEN + """
=====================================
微信4.1.0调试功能启用器
=====================================
        """ + Color.END)
        
        # 检查依赖
        if not self.check_frida_available():
            return False
            
        # 查找微信4.1.0进程
        wechat_processes = self.find_wechat_410_process()
        
        # 如果没有找到，则尝试启动微信
        if not wechat_processes:
            print(Color.YELLOW + "[*] 未找到微信4.1.0进程，正在尝试启动..." + Color.END)
            if not self.start_wechat_410():
                return False
                
            # 再次查找进程
            time.sleep(5)
            wechat_processes = self.find_wechat_410_process()
            
            if not wechat_processes:
                print(Color.RED + "[-] 启动微信后仍未找到微信4.1.0进程" + Color.END)
                return False
                
        # 为所有微信4.1.0进程注入调试脚本
        print(Color.YELLOW + "[*] 正在注入调试脚本..." + Color.END)
        
        success_count = 0
        sessions = []
        
        for pid, version in wechat_processes:
            session = self.inject_debug_script(pid)
            if session:
                sessions.append(session)
                success_count += 1
                
        if success_count > 0:
            print(Color.GREEN + f"""
=====================================
✅ 调试功能启用成功
=====================================
成功为 {success_count} 个微信进程启用调试功能

使用方法：
1. 在微信中打开任意小程序
2. 按 F12 键尝试打开调试界面
3. 或者右键点击小程序界面查看是否有调试选项

注意事项：
- 微信4.1.0可能已加强安全限制，传统调试方法可能无效
- 如果无法打开调试界面，请使用微信官方开发者工具
- 官方开发者工具下载地址：
  https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
            """ + Color.END)
            
            # 保持会话活跃
            if sessions:
                print(Color.YELLOW + "[*] 按 Ctrl+C 退出程序" + Color.END)
                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    print(Color.YELLOW + "\n[!] 程序已退出" + Color.END)
                    
            return True
        else:
            print(Color.RED + """
=====================================
❌ 调试功能启用失败
=====================================
可能的原因：
1. 微信4.1.0已完全禁用非官方调试方法
2. Frida注入被安全软件拦截
3. 配置文件与实际版本不匹配

建议：
请使用微信官方开发者工具进行小程序调试
下载地址：
https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
            """ + Color.END)
            return False

def main():
    try:
        enabler = WeChat410DebugEnabler()
        enabler.enable_debug()
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"\n[-] 程序运行出错: {e}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()