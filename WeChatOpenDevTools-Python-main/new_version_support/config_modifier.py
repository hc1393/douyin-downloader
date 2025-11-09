import os
import json
import base64
import sqlite3
from pathlib import Path

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class WeChatConfigModifier:
    """
    微信配置修改工具
    通过直接修改微信配置文件来启用调试功能
    """
    
    def __init__(self):
        self.wechat_path = self.find_wechat_path()
        
    def find_wechat_path(self):
        """
        查找微信安装路径
        """
        # 常见的微信安装路径
        possible_paths = [
            os.path.expanduser("~\\AppData\\Roaming\\Tencent\\WeChat"),
            "C:\\Program Files (x86)\\Tencent\\WeChat",
            "C:\\Program Files\\Tencent\\WeChat",
            os.path.expanduser("~\\AppData\\Local\\WeChat"),
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                print(Color.GREEN + f"[+] 找到微信路径: {path}" + Color.END)
                return path
                
        # 通过注册表查找
        try:
            import winreg
            reg_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
            
            for i in range(1024):
                try:
                    sub_key_name = winreg.EnumKey(reg_key, i)
                    sub_key = winreg.OpenKey(reg_key, sub_key_name)
                    display_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
                    if "微信" in display_name or "WeChat" in display_name:
                        install_location = winreg.QueryValueEx(sub_key, "InstallLocation")[0].strip('"')
                        print(Color.GREEN + f"[+] 通过注册表找到微信路径: {install_location}" + Color.END)
                        return install_location
                except WindowsError:
                    pass
        except Exception as e:
            print(Color.YELLOW + f"[-] 通过注册表查找微信路径失败: {e}" + Color.END)
            
        print(Color.RED + "[-] 未找到微信安装路径" + Color.END)
        return None
        
    def find_wechat_data_path(self):
        """
        查找微信数据路径
        """
        data_paths = [
            os.path.expanduser("~\\Documents\\WeChat Files"),
            os.path.expanduser("~\\AppData\\Roaming\\Tencent\\WeChat"),
        ]
        
        for path in data_paths:
            if os.path.exists(path):
                print(Color.GREEN + f"[+] 找到微信数据路径: {path}" + Color.END)
                return path
                
        print(Color.RED + "[-] 未找到微信数据路径" + Color.END)
        return None
        
    def enable_devtools_in_storage(self):
        """
        尝试通过修改本地存储来启用调试工具
        """
        data_path = self.find_wechat_data_path()
        if not data_path:
            return False
            
        # 查找可能包含配置的小程序目录
        try:
            for root, dirs, files in os.walk(data_path):
                # 查找微信小程序相关的本地存储文件
                if "WeChatApp" in root and ("storage" in root.lower() or "local" in root.lower()):
                    print(Color.GREEN + f"[+] 检查存储目录: {root}" + Color.END)
                    
                    # 查找可能的配置文件
                    for file in files:
                        if file.endswith(".json") or file.endswith(".db") or file.endswith(".dat"):
                            file_path = os.path.join(root, file)
                            try:
                                if file.endswith(".json"):
                                    self.modify_json_config(file_path)
                                elif file.endswith(".db"):
                                    self.modify_database_config(file_path)
                            except Exception as e:
                                print(Color.YELLOW + f"[-] 处理文件 {file_path} 时出错: {e}" + Color.END)
                                
        except Exception as e:
            print(Color.RED + f"[-] 扫描微信数据目录时出错: {e}" + Color.END)
            return False
            
        return True
        
    def modify_json_config(self, file_path):
        """
        修改JSON配置文件
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 尝试查找并替换调试相关的配置
            if "enable_vconsole" in content or "devtools" in content or "debug" in content:
                print(Color.GREEN + f"[+] 在JSON文件中找到可能的配置: {file_path}" + Color.END)
                
                # 备份原文件
                backup_path = file_path + ".backup"
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(Color.YELLOW + f"[*] 已备份原文件到: {backup_path}" + Color.END)
                
                # 尝试解析JSON
                try:
                    config = json.loads(content)
                    modified = self.update_config_dict(config)
                    if modified:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(config, f, ensure_ascii=False, indent=2)
                        print(Color.GREEN + f"[+] 已修改配置文件: {file_path}" + Color.END)
                except json.JSONDecodeError:
                    # 如果不是有效的JSON，尝试字符串替换
                    modified_content = content.replace('"enable_vconsole":false', '"enable_vconsole":true')
                    modified_content = modified_content.replace('"enable_vconsole": false', '"enable_vconsole": true')
                    modified_content = modified_content.replace('"debug":false', '"debug":true')
                    modified_content = modified_content.replace('"debug": false', '"debug": true')
                    
                    if modified_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(modified_content)
                        print(Color.GREEN + f"[+] 已通过字符串替换修改配置文件: {file_path}" + Color.END)
                        
        except Exception as e:
            print(Color.YELLOW + f"[-] 处理JSON文件 {file_path} 时出错: {e}" + Color.END)
            
    def update_config_dict(self, config):
        """
        递归更新配置字典中的调试选项
        """
        modified = False
        if isinstance(config, dict):
            for key, value in config.items():
                if key in ["enable_vconsole", "debug", "devtools"]:
                    if value is False:
                        config[key] = True
                        modified = True
                        print(Color.GREEN + f"[+] 已启用 {key}" + Color.END)
                elif isinstance(value, (dict, list)):
                    if self.update_config_dict(value):
                        modified = True
        elif isinstance(config, list):
            for item in config:
                if self.update_config_dict(item):
                    modified = True
        return modified
        
    def modify_database_config(self, file_path):
        """
        修改数据库配置文件
        """
        try:
            # 尝试作为SQLite数据库打开
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            
            # 获取所有表名
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            
            for table in tables:
                table_name = table[0]
                print(Color.YELLOW + f"[*] 检查表: {table_name}" + Color.END)
                
                # 尝试查询表结构
                try:
                    cursor.execute(f"PRAGMA table_info({table_name})")
                    columns = cursor.fetchall()
                    
                    # 查找可能包含配置的列
                    config_columns = [col[1] for col in columns if 'config' in col[1].lower() or 'setting' in col[1].lower()]
                    if config_columns:
                        print(Color.GREEN + f"[+] 在表 {table_name} 中找到配置列: {config_columns}" + Color.END)
                        
                        # 查询数据
                        cursor.execute(f"SELECT * FROM {table_name}")
                        rows = cursor.fetchall()
                        
                        for row in rows:
                            print(Color.YELLOW + f"[*] 行数据: {row}" + Color.END)
                            
                except Exception as e:
                    print(Color.YELLOW + f"[-] 查询表 {table_name} 时出错: {e}" + Color.END)
                    
            conn.close()
            
        except Exception as e:
            # 可能不是SQLite数据库
            print(Color.YELLOW + f"[-] {file_path} 可能不是数据库文件: {e}" + Color.END)
            
    def create_manual_instructions(self):
        """
        创建手动操作说明
        """
        instructions = """
===============================
微信调试功能手动启用指南
===============================

由于微信4.1.0增强了安全机制，自动化工具可能无法正常工作。
请按照以下步骤手动启用调试功能：

1. 关闭微信客户端

2. 找到微信数据目录：
   - 通常位于: C:\\Users\\[用户名]\\Documents\\WeChat Files\\
   - 或者: C:\\Users\\[用户名]\\AppData\\Roaming\\Tencent\\WeChat\\

3. 查找小程序相关配置文件：
   - 查找包含 "WeChatApp" 的目录
   - 寻找 .json 或 .db 格式的配置文件

4. 编辑配置文件：
   - 使用文本编辑器打开找到的JSON文件
   - 查找以下配置项并修改为true：
     {
       "enable_vconsole": true,
       "debug": true,
       "devtools": true
     }
   - 保存文件

5. 重新启动微信
   - 打开微信并进入小程序
   - 应该能看到调试选项

注意事项：
- 操作前请备份原配置文件
- 修改后如果出现问题，可以使用备份文件恢复
- 不同版本的微信配置文件可能不同
        """
        
        print(Color.GREEN + instructions + Color.END)
        return instructions

def main():
    print(Color.GREEN + """
===============================
微信配置修改工具
===============================
    """ + Color.END)
    
    modifier = WeChatConfigModifier()
    
    if not modifier.wechat_path:
        print(Color.RED + "[-] 未找到微信安装路径，无法继续" + Color.END)
        return
        
    print(Color.GREEN + "[*] 尝试通过修改配置文件启用调试功能..." + Color.END)
    
    # 尝试修改存储配置
    if modifier.enable_devtools_in_storage():
        print(Color.GREEN + "[+] 配置修改完成，请重启微信查看效果" + Color.END)
    else:
        print(Color.YELLOW + "[-] 自动修改配置失败，生成手动操作说明..." + Color.END)
        modifier.create_manual_instructions()

if __name__ == "__main__":
    main()