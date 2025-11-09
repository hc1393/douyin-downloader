import os
import sys
import json
import psutil
import time
import winreg
import subprocess
from pathlib import Path

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class UltimateWeChatDebugger:
    def __init__(self):
        self.target_directory = r"C:\Users\ThinkPad\Documents\xwechat_files"
        self.debug_config = {
            "debug": True,
            "enable_vconsole": True,
            "devtools": True,
            "inspect": True,
            "show_devtools": True,
            "developer_mode": True,
            "enable_inspector": True,
            "vconsole": True
        }
        
    def kill_all_wechat_processes(self):
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
            
    def find_wechat_installation(self):
        """查找微信安装路径"""
        print(Color.YELLOW + "[*] 查找微信安装路径..." + Color.END)
        
        # 常见安装路径
        common_paths = [
            r"D:\Weixin\Weixin.exe",
            r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",
            r"C:\Program Files\Tencent\WeChat\WeChat.exe"
        ]
        
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
                                    print(Color.GREEN + f"[+] 通过注册表找到微信: {exe_path}" + Color.END)
                                    return exe_path
                    except WindowsError:
                        pass
        except Exception as e:
            print(Color.YELLOW + f"[-] 注册表查询失败: {e}" + Color.END)
            
        # 检查常见路径
        for path in common_paths:
            if os.path.exists(path):
                print(Color.GREEN + f"[+] 找到微信安装路径: {path}" + Color.END)
                return path
                
        print(Color.RED + "[-] 未找到微信安装路径" + Color.END)
        return None
        
    def start_wechat(self):
        """启动微信"""
        exe_path = self.find_wechat_installation()
        if not exe_path:
            return False
            
        try:
            subprocess.Popen([exe_path])
            print(Color.GREEN + f"[+] 已启动微信: {exe_path}" + Color.END)
            return True
        except Exception as e:
            print(Color.RED + f"[-] 启动微信失败: {e}" + Color.END)
            return False
            
    def create_debug_files(self):
        """创建调试配置文件"""
        print(Color.YELLOW + "[*] 创建调试配置文件..." + Color.END)
        
        if not os.path.exists(self.target_directory):
            print(Color.YELLOW + f"[-] 目录不存在，尝试创建: {self.target_directory}" + Color.END)
            try:
                os.makedirs(self.target_directory, exist_ok=True)
            except Exception as e:
                print(Color.RED + f"[-] 创建目录失败: {e}" + Color.END)
                return False
                
        # 创建主要调试配置文件
        config_paths = [
            os.path.join(self.target_directory, "debug_config.json"),
            os.path.join(self.target_directory, "wechat_debug.json"),
            os.path.join(self.target_directory, "devtools_config.json")
        ]
        
        created_files = []
        for config_path in config_paths:
            try:
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(self.debug_config, f, ensure_ascii=False, indent=2)
                print(Color.GREEN + f"[+] 创建配置文件: {config_path}" + Color.END)
                created_files.append(config_path)
            except Exception as e:
                print(Color.RED + f"[-] 创建文件失败 {config_path}: {e}" + Color.END)
                
        return len(created_files) > 0
        
    def modify_existing_configs(self):
        """修改现有的配置文件"""
        print(Color.YELLOW + "[*] 搜索并修改现有配置文件..." + Color.END)
        
        if not os.path.exists(self.target_directory):
            print(Color.RED + f"[-] 目标目录不存在: {self.target_directory}" + Color.END)
            return False
            
        modified_count = 0
        for root, dirs, files in os.walk(self.target_directory):
            # 限制搜索深度
            if root.count(os.sep) - self.target_directory.count(os.sep) > 4:
                del dirs[:]
                continue
                
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        self.modify_json_file(file_path)
                        modified_count += 1
                    except Exception as e:
                        pass
                        
        print(Color.GREEN + f"[+] 共处理 {modified_count} 个配置文件" + Color.END)
        return modified_count > 0
        
    def modify_json_file(self, file_path):
        """修改单个JSON文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 备份原文件
            backup_path = file_path + '.backup'
            if not os.path.exists(backup_path):
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
            # 字符串替换
            original_content = content
            replacements = [
                ('"debug": false', '"debug": true'),
                ('"debug":false', '"debug":true'),
                ('"enable_vconsole": false', '"enable_vconsole": true'),
                ('"enable_vconsole":false', '"enable_vconsole":true'),
                ('"devtools": false', '"devtools": true'),
                ('"devtools":false', '"devtools":true'),
                ('"inspect": false', '"inspect": true'),
                ('"inspect":false', '"inspect":true'),
                ('"show_devtools": false', '"show_devtools": true'),
                ('"show_devtools":false', '"show_devtools":true'),
            ]
            
            for old, new in replacements:
                content = content.replace(old, new)
                
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(Color.GREEN + f"[+] 修改配置文件: {file_path}" + Color.END)
                return True
                
        except Exception as e:
            pass
            
        return False
        
    def create_manual_instructions(self):
        """创建手动操作说明"""
        instructions = f"""
微信4.1.0小程序调试终极解决方案
============================

重要提示：
微信4.1.0版本加强了安全机制，传统的调试方法可能已失效。
请按以下步骤操作：

步骤1：准备工作
1. 完全关闭微信（可通过任务管理器确认）
2. 确保已创建调试配置文件在目录：
   {self.target_directory}

步骤2：启动微信并测试
1. 启动微信客户端
2. 打开任意小程序
3. 尝试以下调试方法：
   a) 按 F12 键
   b) 右键点击小程序界面
   c) 查看是否有"检查"、"调试"等相关选项

步骤3：使用微信官方开发者工具（推荐）
如果上述方法无效，请使用官方工具：
1. 下载微信开发者工具：
   https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
2. 使用USB调试连接手机微信
3. 在开发者工具中调试小程序

步骤4：替代调试方法
1. 在微信中打开小程序
2. 选择"更多" -> "在浏览器中打开"
3. 使用浏览器开发者工具(F12)进行调试

注意事项：
- 本方案仅供学习交流使用
- 微信4.1.0可能已禁用传统调试方法
- 建议使用官方开发者工具获得最佳体验
- 使用过程中可能导致微信功能异常
"""
        
        instruction_path = os.path.join(self.target_directory, "终极调试指南.txt")
        try:
            with open(instruction_path, 'w', encoding='utf-8') as f:
                f.write(instructions)
            print(Color.GREEN + f"[+] 创建操作指南: {instruction_path}" + Color.END)
            return True
        except Exception as e:
            print(Color.RED + f"[-] 创建指南失败: {e}" + Color.END)
            return False
            
    def run_complete_solution(self):
        """运行完整解决方案"""
        print(Color.GREEN + """
===============================
微信4.1.0小程序调试终极解决方案
===============================
        """ + Color.END)
        
        # 1. 关闭微信进程
        self.kill_all_wechat_processes()
        
        # 2. 创建调试配置文件
        print(Color.YELLOW + "\n[*] 正在创建调试配置文件..." + Color.END)
        if self.create_debug_files():
            print(Color.GREEN + "[+] 调试配置文件创建成功" + Color.END)
        else:
            print(Color.RED + "[-] 调试配置文件创建失败" + Color.END)
            
        # 3. 修改现有配置文件
        print(Color.YELLOW + "\n[*] 正在修改现有配置文件..." + Color.END)
        self.modify_existing_configs()
        
        # 4. 创建操作指南
        print(Color.YELLOW + "\n[*] 正在创建操作指南..." + Color.END)
        self.create_manual_instructions()
        
        # 5. 启动微信
        print(Color.YELLOW + "\n[*] 正在启动微信..." + Color.END)
        if self.start_wechat():
            print(Color.GREEN + "[+] 微信启动成功，请按指南操作" + Color.END)
        else:
            print(Color.RED + "[-] 微信启动失败，请手动启动" + Color.END)
            
        print(Color.GREEN + """
===============================
操作完成
===============================

请查看以下文件确认调试设置已生效：
1. C:\\Users\\ThinkPad\\Documents\\xwechat_files\\debug_config.json
2. C:\\Users\\ThinkPad\\Documents\\xwechat_files\\终极调试指南.txt

按照指南操作，如仍有问题建议使用微信官方开发者工具。
        """ + Color.END)

def main():
    try:
        debugger = UltimateWeChatDebugger()
        debugger.run_complete_solution()
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n[!] 用户中断程序" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 程序运行出错: {e}" + Color.END)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()