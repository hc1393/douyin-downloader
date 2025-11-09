#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import psutil
import subprocess
import winreg
from pathlib import Path

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class WeChat410CompleteAdapter:
    def __init__(self):
        self.target_version = 13080813
        self.configs_dir = os.path.join(os.path.dirname(__file__), "configs")
        self.scripts_dir = os.path.join(os.path.dirname(__file__), "scripts")
        
    def find_wechat_install_path(self):
        """查找微信安装路径"""
        # 常见安装路径
        common_paths = [
            r"D:\Weixin\WeChat.exe",
            r"D:\Weixin\Weixin.exe",
            r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",
            r"C:\Program Files\Tencent\WeChat\WeChat.exe"
        ]
        
        # 检查常见路径
        for path in common_paths:
            if os.path.exists(path):
                return path
                
        # 通过注册表查找
        try:
            reg_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as reg_key:
                for i in range(1024):
                    try:
                        sub_key_name = winreg.EnumKey(reg_key, i)
                        with winreg.OpenKey(reg_key, sub_key_name) as sub_key:
                            display_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
                            if "微信" in display_name or "WeChat" in display_name:
                                install_location = winreg.QueryValueEx(sub_key, "InstallLocation")[0].strip('"')
                                exe_path = os.path.join(install_location, "WeChat.exe")
                                if os.path.exists(exe_path):
                                    return exe_path
                                # 检查Weixin.exe
                                exe_path = os.path.join(install_location, "Weixin.exe")
                                if os.path.exists(exe_path):
                                    return exe_path
                    except WindowsError:
                        pass
        except Exception as e:
            pass
            
        return None

    def kill_wechat_processes(self):
        """关闭所有微信进程"""
        print(Color.YELLOW + "[*] 正在关闭所有微信进程..." + Color.END)
        killed_count = 0
        
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if 'WeChat' in proc.info['name']:
                    proc.kill()
                    print(Color.GREEN + f"[+] 已关闭: {proc.info['name']} (PID: {proc.info['pid']})" + Color.END)
                    killed_count += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
                
        if killed_count == 0:
            print(Color.GREEN + "[+] 未发现微信进程" + Color.END)
        else:
            print(Color.YELLOW + f"[*] 共关闭 {killed_count} 个微信进程，等待3秒..." + Color.END)
            time.sleep(3)

    def start_wechat(self):
        """启动微信"""
        exe_path = self.find_wechat_install_path()
        if not exe_path:
            print(Color.RED + "[-] 未找到微信安装路径" + Color.END)
            return False
            
        try:
            subprocess.Popen([exe_path])
            print(Color.GREEN + f"[+] 已启动微信: {exe_path}" + Color.END)
            return True
        except Exception as e:
            print(Color.RED + f"[-] 启动微信失败: {e}" + Color.END)
            return False

    def check_wechat_processes(self):
        """检查微信4.1.0进程"""
        wechat_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'] == 'WeChatAppEx.exe':
                    # 检查是否为4.1.0版本
                    cmdline = ' '.join(proc.info['cmdline'])
                    if str(self.target_version) in cmdline:
                        wechat_processes.append(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
                
        return wechat_processes

    def create_debug_config(self):
        """创建调试配置文件"""
        debug_config = {
            "debug": True,
            "enable_vconsole": True,
            "devtools": True,
            "inspect": True,
            "show_devtools": True,
            "developer_mode": True,
            "enable_inspector": True,
            "vconsole": True
        }
        
        # 创建配置文件目录
        config_dir = r"C:\Users\Public\Documents\WeChatDebug"
        os.makedirs(config_dir, exist_ok=True)
        
        # 写入配置文件
        config_files = [
            os.path.join(config_dir, "debug_config.json"),
            os.path.join(config_dir, "wechat_debug.json")
        ]
        
        for config_file in config_files:
            try:
                with open(config_file, 'w', encoding='utf-8') as f:
                    json.dump(debug_config, f, ensure_ascii=False, indent=2)
                print(Color.GREEN + f"[+] 创建配置文件: {config_file}" + Color.END)
            except Exception as e:
                print(Color.RED + f"[-] 创建配置文件失败 {config_file}: {e}" + Color.END)

    def patch_wechat_config(self):
        """修改微信配置以启用调试"""
        # 微信用户配置目录
        user_dir = os.path.expanduser(r"~\Documents\WeChat Files")
        if not os.path.exists(user_dir):
            print(Color.YELLOW + "[-] 未找到微信用户目录" + Color.END)
            return False
            
        patched = False
        for root, dirs, files in os.walk(user_dir):
            # 限制搜索深度
            if root.count(os.sep) - user_dir.count(os.sep) > 3:
                del dirs[:]
                continue
                
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            
                        original_content = content
                        # 替换配置项
                        replacements = [
                            ('"debug": false', '"debug": true'),
                            ('"enable_vconsole": false', '"enable_vconsole": true'),
                            ('"devtools": false', '"devtools": true'),
                            ('"inspect": false', '"inspect": true'),
                            ('"show_devtools": false', '"show_devtools": true'),
                        ]
                        
                        for old, new in replacements:
                            content = content.replace(old, new)
                            
                        if content != original_content:
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            print(Color.GREEN + f"[+] 修改配置文件: {file_path}" + Color.END)
                            patched = True
                    except Exception as e:
                        pass
                        
        return patched

    def run_complete_solution(self):
        """运行完整解决方案"""
        print(Color.GREEN + """
=================================
微信4.1.0调试功能完整解决方案
=================================
        """ + Color.END)
        
        # 1. 关闭微信进程
        self.kill_wechat_processes()
        
        # 2. 创建调试配置文件
        print(Color.YELLOW + "\n[*] 正在创建调试配置文件..." + Color.END)
        self.create_debug_config()
        
        # 3. 修改现有配置
        print(Color.YELLOW + "\n[*] 正在修改微信配置..." + Color.END)
        self.patch_wechat_config()
        
        # 4. 启动微信
        print(Color.YELLOW + "\n[*] 正在启动微信..." + Color.END)
        self.start_wechat()
        
        # 5. 等待并检查微信进程
        print(Color.YELLOW + "\n[*] 等待微信启动..." + Color.END)
        time.sleep(5)
        
        processes = self.check_wechat_processes()
        if processes:
            print(Color.GREEN + f"[+] 检测到微信4.1.0进程: {processes}" + Color.END)
            print(Color.GREEN + """
[*] 微信4.1.0调试功能已启用
=================================

使用说明：
1. 在微信中打开任意小程序
2. 按 F12 键尝试打开调试界面
3. 或者右键点击小程序界面查看是否有调试选项

注意事项：
- 微信4.1.0可能已加强安全限制，传统调试方法可能无效
- 如果无法打开调试界面，请使用微信官方开发者工具
            """ + Color.END)
        else:
            print(Color.YELLOW + "[-] 未检测到微信4.1.0进程，请手动启动微信" + Color.END)

def main():
    try:
        adapter = WeChat410CompleteAdapter()
        adapter.run_complete_solution()
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"\n[-] 程序运行出错: {e}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()