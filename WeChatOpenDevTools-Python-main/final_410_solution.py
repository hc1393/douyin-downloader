#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import psutil
import subprocess
import winreg
import signal
from pathlib import Path

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class WeChat410FinalSolution:
    def __init__(self):
        self.target_version = 13080813
        
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

    def create_debug_files(self):
        """创建调试配置文件"""
        debug_configs = [
            {
                "debug": True,
                "enable_vconsole": True,
                "devtools": True,
                "inspect": True,
                "show_devtools": True,
                "developer_mode": True,
                "enable_inspector": True,
                "vconsole": True
            },
            {
                "debug": {
                    "enabled": True,
                    "devtools": True,
                    "inspect": True
                },
                "features": {
                    "vconsole": True,
                    "devtools": True
                }
            }
        ]
        
        # 创建配置文件目录
        config_dirs = [
            r"C:\Users\Public\Documents\WeChatDebug",
            os.path.expanduser(r"~\Documents\WeChatDebug")
        ]
        
        for config_dir in config_dirs:
            try:
                os.makedirs(config_dir, exist_ok=True)
                
                # 写入配置文件
                for i, config in enumerate(debug_configs):
                    config_file = os.path.join(config_dir, f"debug_config_{i+1}.json")
                    try:
                        with open(config_file, 'w', encoding='utf-8') as f:
                            json.dump(config, f, ensure_ascii=False, indent=2)
                        print(Color.GREEN + f"[+] 创建配置文件: {config_file}" + Color.END)
                    except Exception as e:
                        print(Color.RED + f"[-] 创建配置文件失败 {config_file}: {e}" + Color.END)
            except Exception as e:
                print(Color.RED + f"[-] 创建目录失败 {config_dir}: {e}" + Color.END)

    def patch_user_configs(self):
        """修改用户配置文件"""
        # 微信用户配置目录
        user_dirs = [
            os.path.expanduser(r"~\Documents\WeChat Files"),
            os.path.expanduser(r"~\Documents\Weixin Files")
        ]
        
        patched = False
        for user_dir in user_dirs:
            if not os.path.exists(user_dir):
                continue
                
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
                                ('"developer_mode": false', '"developer_mode": true'),
                                ('"enable_inspector": false', '"enable_inspector": true'),
                                ('"vconsole": false', '"vconsole": true'),
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

    def show_manual_instructions(self):
        """显示手动操作说明"""
        instructions = """
微信4.1.0调试功能使用说明
======================

重要提示：
微信4.1.0版本加强了安全机制，传统的调试方法可能已失效。

使用步骤：
1. 确保微信已完全关闭
2. 运行本程序: python final_410_solution.py
3. 等待微信自动启动
4. 打开任意小程序
5. 尝试以下操作启用调试：
   a) 按 F12 键
   b) 右键点击小程序界面
   c) 查看是否有"检查"、"调试"等相关选项

如果上述方法无效，请使用微信官方开发者工具：
1. 下载地址：
   https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
2. 安装并运行开发者工具
3. 使用USB调试连接手机微信
4. 在开发者工具中调试小程序

注意事项：
- 本工具仅供学习交流使用
- 微信4.1.0可能已禁用传统调试方法
- 使用过程中可能导致微信功能异常
        """
        
        print(Color.BLUE + instructions + Color.END)
        
        # 保存到文件
        try:
            with open("wechat_410_debug_instructions.txt", "w", encoding="utf-8") as f:
                f.write(instructions)
            print(Color.GREEN + "[+] 操作说明已保存到 wechat_410_debug_instructions.txt" + Color.END)
        except Exception as e:
            print(Color.RED + f"[-] 保存操作说明失败: {e}" + Color.END)

    def run_solution(self):
        """运行完整解决方案"""
        print(Color.GREEN + """
=================================
微信4.1.0调试功能最终解决方案
=================================
        """ + Color.END)
        
        # 1. 关闭微信进程
        self.kill_wechat_processes()
        
        # 2. 创建调试配置文件
        print(Color.YELLOW + "\n[*] 正在创建调试配置文件..." + Color.END)
        self.create_debug_files()
        
        # 3. 修改用户配置
        print(Color.YELLOW + "\n[*] 正在修改用户配置..." + Color.END)
        self.patch_user_configs()
        
        # 4. 启动微信
        print(Color.YELLOW + "\n[*] 正在启动微信..." + Color.END)
        self.start_wechat()
        
        # 5. 显示操作说明
        print(Color.YELLOW + "\n[*] 正在生成操作说明..." + Color.END)
        self.show_manual_instructions()
        
        print(Color.GREEN + """
[*] 微信4.1.0调试解决方案已执行完成
=====================================

请按照操作说明尝试启用调试功能。
如果仍有问题，建议使用微信官方开发者工具。
        """ + Color.END)

def main():
    try:
        solution = WeChat410FinalSolution()
        solution.run_solution()
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"\n[-] 程序运行出错: {e}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()