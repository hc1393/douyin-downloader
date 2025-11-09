import os
import json
import sqlite3
import base64
from pathlib import Path

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class UltimateDebugEnabler:
    """
    终极微信调试功能启用工具
    通过多种方式尝试启用微信小程序调试功能
    """
    
    def __init__(self):
        self.wechat_data_paths = self.find_wechat_data_paths()
        
    def find_wechat_data_paths(self):
        """
        查找所有可能的微信数据路径
        """
        possible_paths = [
            os.path.expanduser("~\\Documents\\WeChat Files"),
            os.path.expanduser("~\\AppData\\Roaming\\Tencent\\WeChat"),
            os.path.expanduser("~\\AppData\\Local\\Tencent\\WeChat"),
            os.path.expanduser("~\\AppData\\Roaming\\Tencent\\WeChatStudio"),
        ]
        
        found_paths = []
        for path in possible_paths:
            if os.path.exists(path):
                found_paths.append(path)
                print(Color.GREEN + f"[+] 找到微信数据路径: {path}" + Color.END)
                
        if not found_paths:
            print(Color.RED + "[-] 未找到任何微信数据路径" + Color.END)
            
        return found_paths
        
    def search_all_json_files(self):
        """
        搜索所有JSON文件以查找调试配置
        """
        print(Color.GREEN + "[*] 开始搜索所有JSON文件..." + Color.END)
        
        modified_files = []
        
        for data_path in self.wechat_data_paths:
            print(Color.YELLOW + f"[*] 搜索目录: {data_path}" + Color.END)
            
            for root, dirs, files in os.walk(data_path):
                # 限制搜索深度以避免过多输出
                if root.count(os.sep) - data_path.count(os.sep) > 5:
                    del dirs[:]
                    continue
                    
                for file in files:
                    if file.endswith('.json'):
                        file_path = os.path.join(root, file)
                        try:
                            if self.modify_json_file_for_debug(file_path):
                                modified_files.append(file_path)
                                print(Color.GREEN + f"[+] 已修改文件: {file_path}" + Color.END)
                        except Exception as e:
                            # 忽略单个文件的错误
                            pass
                            
        print(Color.GREEN + f"[+] 共修改了 {len(modified_files)} 个文件" + Color.END)
        return modified_files
        
    def modify_json_file_for_debug(self, file_path):
        """
        修改JSON文件以启用调试功能
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 检查是否可能是小程序相关文件
            if not any(keyword in content.lower() for keyword in [
                'miniprogram', 'wechatapp', 'debug', 'console', 'devtool', 'vconsole'
            ]):
                return False
                
            # 备份原文件
            backup_path = file_path + '.backup'
            if not os.path.exists(backup_path):
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
            # 尝试解析JSON
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                # 如果不是有效的JSON，使用字符串替换
                return self.string_replace_debug_settings(file_path, content)
                
            # 递归修改数据
            modified = self.recursive_modify_debug_settings(data)
            
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                return True
                
        except Exception as e:
            pass
            
        return False
        
    def recursive_modify_debug_settings(self, data):
        """
        递归修改调试设置
        """
        modified = False
        
        if isinstance(data, dict):
            debug_keys = ['debug', 'enable_vconsole', 'devtools', 'inspect', 'show_devtools', 'developer_mode']
            for key, value in data.items():
                if any(debug_key in key.lower() for debug_key in debug_keys):
                    if value is False or (isinstance(value, str) and value.lower() == 'false'):
                        data[key] = True
                        modified = True
                        print(Color.GREEN + f"[+] 启用 {key}" + Color.END)
                elif isinstance(value, (dict, list)):
                    if self.recursive_modify_debug_settings(value):
                        modified = True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)) and self.recursive_modify_debug_settings(item):
                    modified = True
                    
        return modified
        
    def string_replace_debug_settings(self, file_path, content):
        """
        字符串替换调试设置
        """
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
            ('"developer_mode": false', '"developer_mode": true'),
            ('"developer_mode":false', '"developer_mode":true'),
        ]
        
        for old, new in replacements:
            content = content.replace(old, new)
            
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
            
        return False
        
    def search_database_files(self):
        """
        搜索数据库文件以查找调试配置
        """
        print(Color.GREEN + "[*] 开始搜索数据库文件..." + Color.END)
        
        modified_dbs = []
        
        for data_path in self.wechat_data_paths:
            for root, dirs, files in os.walk(data_path):
                if root.count(os.sep) - data_path.count(os.sep) > 5:
                    del dirs[:]
                    continue
                    
                for file in files:
                    if file.endswith('.db') or file.endswith('.sqlite') or file.endswith('.sqlite3'):
                        file_path = os.path.join(root, file)
                        try:
                            if self.modify_database_for_debug(file_path):
                                modified_dbs.append(file_path)
                                print(Color.GREEN + f"[+] 已修改数据库: {file_path}" + Color.END)
                        except Exception as e:
                            pass
                            
        print(Color.GREEN + f"[+] 共修改了 {len(modified_dbs)} 个数据库文件" + Color.END)
        return modified_dbs
        
    def modify_database_for_debug(self, db_path):
        """
        修改数据库以启用调试功能
        """
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # 获取所有表名
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            
            modified = False
            for table in tables:
                table_name = table[0]
                try:
                    # 尝试查询表结构
                    cursor.execute(f"PRAGMA table_info({table_name})")
                    columns = cursor.fetchall()
                    
                    # 查找可能包含配置的列
                    config_columns = [col[1] for col in columns if any(keyword in col[1].lower() for keyword in [
                        'config', 'setting', 'debug', 'dev'
                    ])]
                    
                    if config_columns:
                        # 尝试查询数据
                        cursor.execute(f"SELECT * FROM {table_name}")
                        rows = cursor.fetchall()
                        
                        for row in rows:
                            # 检查每一行数据
                            for i, value in enumerate(row):
                                if isinstance(value, str) and any(keyword in value.lower() for keyword in [
                                    'debug', 'vconsole', 'devtool'
                                ]):
                                    print(Color.YELLOW + f"[*] 在表 {table_name} 中找到可能的配置数据" + Color.END)
                                    
                except Exception as e:
                    pass
                    
            conn.close()
            return modified
            
        except Exception as e:
            return False
            
    def create_debug_files(self):
        """
        创建调试配置文件
        """
        print(Color.GREEN + "[*] 创建调试配置文件..." + Color.END)
        
        debug_config = {
            "debug": True,
            "enable_vconsole": True,
            "devtools": True,
            "inspect": True,
            "show_devtools": True,
            "developer_mode": True,
            "enable_inspector": True,
            "enable_debug_mode": True
        }
        
        created_files = []
        
        for data_path in self.wechat_data_paths:
            # 在多个位置创建配置文件
            config_paths = [
                os.path.join(data_path, "debug_config.json"),
                os.path.join(data_path, "wechat_debug.json"),
                os.path.join(data_path, "miniprogram_debug.json"),
                os.path.join(data_path, "devtools_config.json"),
            ]
            
            for config_path in config_paths:
                try:
                    with open(config_path, 'w', encoding='utf-8') as f:
                        json.dump(debug_config, f, ensure_ascii=False, indent=2)
                    created_files.append(config_path)
                    print(Color.GREEN + f"[+] 创建配置文件: {config_path}" + Color.END)
                except Exception as e:
                    print(Color.YELLOW + f"[-] 创建配置文件失败: {config_path}" + Color.END)
                    
        return created_files
        
    def print_manual_instructions(self):
        """
        打印详细的手动操作说明
        """
        instructions = """
===============================
终极手动启用微信小程序调试功能指南
===============================

如果自动方法都无效，请按以下详细步骤手动操作：

步骤1：完全关闭微信
   - 确保微信完全退出，包括后台进程
   - 可通过任务管理器确认没有WeChat相关进程

步骤2：导航到微信数据目录
   """
        for path in self.wechat_data_paths:
            instructions += f"   - {path}\n"
            
        instructions += """
步骤3：深入搜索配置文件
   - 使用Windows搜索功能，在微信数据目录中搜索以下文件：
     * 文件名包含：config, setting, storage, debug, preference
     * 文件扩展名：.json, .db, .sqlite, .ini
   - 特别关注最近修改的文件

步骤4：编辑找到的配置文件
   - 使用文本编辑器（如Notepad++）打开JSON文件
   - 查找并修改以下所有配置项为true：
     {
       "debug": true,
       "enable_vconsole": true,
       "devtools": true,
       "inspect": true,
       "show_devtools": true,
       "developer_mode": true,
       "enable_inspector": true,
       "enable_debug_mode": true
     }

步骤5：处理数据库文件（高级用户）
   - 使用DB Browser for SQLite等工具打开.db文件
   - 查找包含"config"或"setting"的表
   - 查找包含"debug"关键字的字段并修改为true

步骤6：设置文件为只读
   - 右键点击修改后的文件
   - 选择"属性"
   - 勾选"只读"以防止微信覆盖

步骤7：重新启动微信
   - 启动微信并登录
   - 打开任意小程序
   - 查看是否有调试相关按钮出现

步骤8：使用微信官方开发者工具（推荐备选方案）
   - 下载微信开发者工具：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
   - 通过USB调试连接手机微信
   - 在开发者工具中调试小程序

注意事项：
   - 操作前务必备份原文件
   - 不同版本微信配置文件可能不同
   - 如果问题持续存在，可能是微信版本不支持或安全机制阻止
        """
        
        print(Color.GREEN + instructions + Color.END)

def main():
    print(Color.GREEN + """
===============================
终极微信调试功能启用工具
===============================
    """ + Color.END)
    
    enabler = UltimateDebugEnabler()
    
    if not enabler.wechat_data_paths:
        print(Color.RED + "[-] 未找到微信数据路径，无法继续" + Color.END)
        return
        
    # 尝试所有方法
    print(Color.GREEN + "[*] 尝试方法1：搜索并修改JSON配置文件..." + Color.END)
    json_files = enabler.search_all_json_files()
    
    print(Color.GREEN + "[*] 尝试方法2：搜索并修改数据库文件..." + Color.END)
    db_files = enabler.search_database_files()
    
    print(Color.GREEN + "[*] 尝试方法3：创建新的调试配置文件..." + Color.END)
    config_files = enabler.create_debug_files()
    
    print(Color.GREEN + """
===============================
处理完成
===============================
    """ + Color.END)
    
    if json_files or db_files or config_files:
        print(Color.GREEN + "[+] 已成功处理相关文件，现在请：" + Color.END)
        print(Color.YELLOW + "1. 完全关闭微信客户端" + Color.END)
        print(Color.YELLOW + "2. 重新启动微信" + Color.END)
        print(Color.YELLOW + "3. 打开小程序查看是否出现调试界面" + Color.END)
    else:
        print(Color.YELLOW + "[-] 未找到可处理的文件" + Color.END)
        
    # 显示详细手动操作说明
    enabler.print_manual_instructions()

if __name__ == "__main__":
    main()