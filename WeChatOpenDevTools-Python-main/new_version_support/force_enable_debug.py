import os
import json
import glob
from pathlib import Path

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class WeChatDebugEnabler:
    """
    微信调试功能强制启用工具
    通过直接修改微信本地存储数据来启用调试功能
    """
    
    def __init__(self):
        self.wechat_data_path = self.find_wechat_data_path()
        
    def find_wechat_data_path(self):
        """
        查找微信数据路径
        """
        possible_paths = [
            os.path.expanduser("~\\Documents\\WeChat Files"),
            os.path.expanduser("~\\AppData\\Roaming\\Tencent\\WeChat"),
            os.path.expanduser("~\\AppData\\Local\\Tencent\\WeChat"),
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                print(Color.GREEN + f"[+] 找到微信数据路径: {path}" + Color.END)
                return path
                
        print(Color.RED + "[-] 未找到微信数据路径" + Color.END)
        return None
        
    def find_miniprogram_storage(self):
        """
        查找小程序存储目录
        """
        if not self.wechat_data_path:
            return []
            
        miniprogram_paths = []
        
        # 在微信数据目录中查找小程序相关目录
        try:
            for root, dirs, files in os.walk(self.wechat_data_path):
                for dir_name in dirs:
                    # 查找可能的小程序存储目录
                    if any(keyword in dir_name.lower() for keyword in [
                        'miniprogram', 'wechatapp', 'storage', 'localstorage'
                    ]):
                        full_path = os.path.join(root, dir_name)
                        miniprogram_paths.append(full_path)
                        print(Color.YELLOW + f"[*] 找到可能的小程序存储目录: {full_path}" + Color.END)
                        
                # 限制搜索深度避免过多输出
                if root.count(os.sep) - self.wechat_data_path.count(os.sep) > 3:
                    del dirs[:]
                    
        except Exception as e:
            print(Color.RED + f"[-] 搜索小程序存储目录时出错: {e}" + Color.END)
            
        return miniprogram_paths
        
    def force_enable_debug_in_files(self):
        """
        在找到的文件中强制启用调试
        """
        if not self.wechat_data_path:
            return False
            
        miniprogram_paths = self.find_miniprogram_storage()
        if not miniprogram_paths:
            print(Color.YELLOW + "[-] 未找到明确的小程序存储目录，尝试在整个微信数据目录中搜索" + Color.END)
            miniprogram_paths = [self.wechat_data_path]
            
        modified_count = 0
        
        # 在所有找到的目录中搜索配置文件
        for path in miniprogram_paths:
            if not os.path.exists(path):
                continue
                
            print(Color.GREEN + f"[*] 搜索目录: {path}" + Color.END)
            
            # 递归搜索JSON文件
            for root, dirs, files in os.walk(path):
                # 限制搜索深度
                if root.count(os.sep) - path.count(os.sep) > 4:
                    del dirs[:]
                    continue
                    
                for file in files:
                    if file.endswith('.json'):
                        file_path = os.path.join(root, file)
                        try:
                            modified = self.modify_json_file(file_path)
                            if modified:
                                modified_count += 1
                                print(Color.GREEN + f"[+] 已修改文件: {file_path}" + Color.END)
                        except Exception as e:
                            # 忽略单个文件的错误
                            pass
                            
        print(Color.GREEN + f"[+] 共修改了 {modified_count} 个文件" + Color.END)
        return modified_count > 0
        
    def modify_json_file(self, file_path):
        """
        修改JSON文件以启用调试
        """
        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 检查是否包含调试相关的关键字
            if not any(keyword in content.lower() for keyword in [
                'debug', 'console', 'devtool', 'inspect', 'vconsole'
            ]):
                # 如果不包含关键字，跳过此文件
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
                # 如果不是有效的JSON，尝试字符串替换
                return self.string_replace_in_file(file_path, content)
                
            # 递归修改数据
            modified = self.modify_json_data(data)
            
            if modified:
                # 写回修改后的内容
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                return True
                
        except Exception as e:
            # 忽略处理错误
            pass
            
        return False
        
    def modify_json_data(self, data):
        """
        递归修改JSON数据以启用调试
        """
        modified = False
        
        if isinstance(data, dict):
            for key, value in data.items():
                # 检查是否是调试相关的键
                if any(debug_key in key.lower() for debug_key in [
                    'debug', 'console', 'devtool', 'inspect', 'vconsole'
                ]):
                    if value is False or (isinstance(value, str) and value.lower() == 'false'):
                        data[key] = True
                        modified = True
                        print(Color.GREEN + f"[+] 启用 {key}" + Color.END)
                    elif value is True or (isinstance(value, str) and value.lower() == 'true'):
                        # 已经是启用状态
                        pass
                elif isinstance(value, (dict, list)):
                    # 递归处理嵌套结构
                    if self.modify_json_data(value):
                        modified = True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)) and self.modify_json_data(item):
                    modified = True
                    
        return modified
        
    def string_replace_in_file(self, file_path, content):
        """
        在文件中进行字符串替换
        """
        original_content = content
        # 替换常见的调试配置
        replacements = [
            ('"debug": false', '"debug": true'),
            ('"debug":false', '"debug":true'),
            ('"enable_vconsole": false', '"enable_vconsole": true'),
            ('"enable_vconsole":false', '"enable_vconsole":true'),
            ('"devtools": false', '"devtools": true'),
            ('"devtools":false', '"devtools":true'),
            ('"inspect": false', '"inspect": true'),
            ('"inspect":false', '"inspect":true'),
        ]
        
        for old, new in replacements:
            content = content.replace(old, new)
            
        # 如果内容发生了变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
            
        return False
        
    def create_debug_config_file(self):
        """
        创建一个新的调试配置文件
        """
        if not self.wechat_data_path:
            return False
            
        # 尝试在几个可能的位置创建配置文件
        config_content = {
            "debug": True,
            "enable_vconsole": True,
            "devtools": True,
            "inspect": True,
            "enable_debug_mode": True,
            "show_devtools": True
        }
        
        config_paths = [
            os.path.join(self.wechat_data_path, "debug_config.json"),
            os.path.join(self.wechat_data_path, "wechat_debug.json"),
        ]
        
        for config_path in config_paths:
            try:
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(config_content, f, ensure_ascii=False, indent=2)
                print(Color.GREEN + f"[+] 创建调试配置文件: {config_path}" + Color.END)
                return True
            except Exception as e:
                print(Color.YELLOW + f"[-] 创建配置文件 {config_path} 失败: {e}" + Color.END)
                
        return False
        
    def print_manual_instructions(self):
        """
        打印手动操作说明
        """
        instructions = f"""
===============================
手动启用微信小程序调试功能
===============================

如果自动修改无效，请按以下步骤手动操作：

1. 完全关闭微信客户端

2. 导航到微信数据目录：
   {self.wechat_data_path or '未找到微信数据目录'}

3. 查找小程序配置文件：
   - 查找文件名包含 "storage"、"config"、"setting" 的.json文件
   - 特别注意文件内容包含 "debug"、"vconsole"、"devtools" 的文件

4. 使用文本编辑器打开这些文件

5. 查找并修改以下配置项：
   {{
     "debug": true,
     "enable_vconsole": true,
     "devtools": true,
     "inspect": true
   }}

6. 保存文件并设置为只读（防止微信自动覆盖）

7. 重新启动微信并打开小程序

注意事项：
- 操作前请备份原文件
- 如果微信自动恢复设置，可尝试设置文件为只读
- 不同版本微信配置文件可能不同
        """
        
        print(Color.GREEN + instructions + Color.END)

def main():
    print(Color.GREEN + """
===============================
微信调试功能强制启用工具
===============================
    """ + Color.END)
    
    enabler = WeChatDebugEnabler()
    
    if not enabler.wechat_data_path:
        print(Color.RED + "[-] 未找到微信数据路径，无法继续" + Color.END)
        return
        
    print(Color.GREEN + "[*] 开始强制启用调试功能..." + Color.END)
    
    # 尝试修改现有配置文件
    if enabler.force_enable_debug_in_files():
        print(Color.GREEN + "[+] 调试功能启用完成！" + Color.END)
        print(Color.YELLOW + "[*] 请完全关闭微信后重新启动" + Color.END)
    else:
        print(Color.YELLOW + "[-] 未找到可修改的配置文件" + Color.END)
        # 尝试创建新的配置文件
        if enabler.create_debug_config_file():
            print(Color.GREEN + "[+] 已创建新的调试配置文件" + Color.END)
        else:
            print(Color.RED + "[-] 创建调试配置文件失败" + Color.END)
            
    # 显示手动操作说明
    enabler.print_manual_instructions()

if __name__ == "__main__":
    main()