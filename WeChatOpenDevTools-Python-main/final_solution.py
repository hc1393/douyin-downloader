import os
import sys
import json
import psutil
import time
import winreg
from pathlib import Path

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def find_wechat_install_path():
    """
    查找微信安装路径
    """
    possible_paths = [
        r"D:\Weixin\Weixin.exe",
        r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",
        r"C:\Program Files\Tencent\WeChat\WeChat.exe",
    ]
    
    # 通过注册表查找
    try:
        reg_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
        
        for i in range(1024):
            try:
                sub_key_name = winreg.EnumKey(reg_key, i)
                sub_key = winreg.OpenKey(reg_key, sub_key_name)
                display_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
                if "微信" in display_name or "WeChat" in display_name:
                    install_location = winreg.QueryValueEx(sub_key, "InstallLocation")[0].strip('"')
                    exe_path = os.path.join(install_location, "WeChat.exe")
                    if os.path.exists(exe_path):
                        return exe_path
            except WindowsError:
                pass
    except Exception as e:
        pass
        
    # 检查常见路径
    for path in possible_paths:
        if os.path.exists(path):
            return path
            
    return None

def kill_wechat_processes():
    """
    关闭所有微信进程
    """
    print(Color.YELLOW + "[*] 正在关闭微信进程..." + Color.END)
    
    killed = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'WeChat' in proc.info['name']:
                proc.kill()
                print(Color.GREEN + f"[+] 已关闭进程: {proc.info['name']} (PID: {proc.info['pid']})" + Color.END)
                killed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
            
    if not killed:
        print(Color.YELLOW + "[-] 未发现微信进程" + Color.END)
        
    # 等待进程完全关闭
    time.sleep(3)

def start_wechat():
    """
    启动微信
    """
    path = find_wechat_install_path()
    if not path:
        print(Color.RED + "[-] 未找到微信安装路径" + Color.END)
        return False
        
    try:
        os.startfile(path)
        print(Color.GREEN + f"[+] 已启动微信: {path}" + Color.END)
        return True
    except Exception as e:
        print(Color.RED + f"[-] 启动微信失败: {e}" + Color.END)
        return False

def find_wechat_data_paths():
    """
    查找微信数据目录
    """
    paths = [
        os.path.expanduser(r"~\Documents\WeChat Files"),
        os.path.expanduser(r"~\AppData\Roaming\Tencent\WeChat"),
        os.path.expanduser(r"~\AppData\Local\Tencent\WeChat"),
    ]
    
    return [path for path in paths if os.path.exists(path)]

def enable_debug_in_config_files():
    """
    在配置文件中启用调试
    """
    data_paths = find_wechat_data_paths()
    if not data_paths:
        print(Color.RED + "[-] 未找到微信数据目录" + Color.END)
        return False
        
    debug_settings = {
        "debug": True,
        "enable_vconsole": True,
        "devtools": True,
        "inspect": True,
        "show_devtools": True
    }
    
    modified_count = 0
    
    for data_path in data_paths:
        print(Color.YELLOW + f"[*] 搜索目录: {data_path}" + Color.END)
        
        # 创建调试配置文件
        config_path = os.path.join(data_path, "debug_config.json")
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(debug_settings, f, ensure_ascii=False, indent=2)
            print(Color.GREEN + f"[+] 创建调试配置文件: {config_path}" + Color.END)
            modified_count += 1
        except Exception as e:
            print(Color.RED + f"[-] 创建配置文件失败: {e}" + Color.END)
            
        # 搜索并修改现有配置文件
        for root, dirs, files in os.walk(data_path):
            if root.count(os.sep) - data_path.count(os.sep) > 4:
                del dirs[:]
                continue
                
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            
                        # 备份原文件
                        backup_path = file_path + '.backup'
                        if not os.path.exists(backup_path):
                            with open(backup_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                                
                        # 字符串替换
                        modified = False
                        replacements = [
                            ('"debug": false', '"debug": true'),
                            ('"debug":false', '"debug":true'),
                            ('"enable_vconsole": false', '"enable_vconsole": true'),
                            ('"enable_vconsole":false', '"enable_vconsole":true'),
                            ('"devtools": false', '"devtools": true'),
                            ('"devtools":false', '"devtools":true'),
                        ]
                        
                        for old, new in replacements:
                            if old in content:
                                content = content.replace(old, new)
                                modified = True
                                
                        if modified:
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            print(Color.GREEN + f"[+] 修改配置文件: {file_path}" + Color.END)
                            modified_count += 1
                            
                    except Exception as e:
                        pass
    
    print(Color.GREEN + f"[+] 共修改了 {modified_count} 个文件" + Color.END)
    return modified_count > 0

def create_desktop_shortcut():
    """
    创建桌面快捷方式和说明文件
    """
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # 创建说明文件
    readme_content = """
微信小程序调试解决方案
====================

使用步骤：
1. 运行此脚本关闭并重新启动微信
2. 打开任意小程序
3. 查看是否出现调试界面

如果仍然无法看到调试界面，请：
1. 下载微信开发者工具
   https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
2. 使用USB调试连接手机微信
3. 在开发者工具中调试小程序

注意事项：
- 本工具仅供学习交流使用
- 微信4.1.0版本可能已禁用传统调试方法
- 建议使用官方开发者工具进行调试
"""
    
    readme_path = os.path.join(desktop, "微信调试说明.txt")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(Color.GREEN + f"[+] 创建说明文件: {readme_path}" + Color.END)
    
    return readme_path

def main():
    print(Color.GREEN + """
===============================
微信小程序调试终极解决方案
===============================
    """ + Color.END)
    
    # 关闭微信进程
    kill_wechat_processes()
    
    # 启用调试配置
    print(Color.YELLOW + "[*] 正在启用调试配置..." + Color.END)
    enable_debug_in_config_files()
    
    # 启动微信
    print(Color.YELLOW + "[*] 正在启动微信..." + Color.END)
    if start_wechat():
        print(Color.GREEN + "[+] 微信启动成功，请打开小程序查看调试功能" + Color.END)
    else:
        print(Color.RED + "[-] 微信启动失败" + Color.END)
    
    # 创建说明文件
    create_desktop_shortcut()
    
    print(Color.GREEN + """
===============================
操作完成
===============================

请按以下步骤操作：
1. 打开任意小程序
2. 查看是否出现调试界面（F12或右键菜单）
3. 如果没有调试界面，请参考桌面的说明文件

如需再次运行此工具，请执行：
python final_solution.py
    """ + Color.END)

if __name__ == "__main__":
    main()