import os
import json

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def enable_debug_in_directory(target_directory):
    """
    在指定目录中启用调试功能
    """
    if not os.path.exists(target_directory):
        print(Color.RED + f"[-] 目录不存在: {target_directory}" + Color.END)
        return False
        
    print(Color.GREEN + f"[+] 处理目录: {target_directory}" + Color.END)
    
    debug_settings = {
        "debug": True,
        "enable_vconsole": True,
        "devtools": True,
        "inspect": True,
        "show_devtools": True,
        "developer_mode": True
    }
    
    # 创建调试配置文件
    config_path = os.path.join(target_directory, "debug_config.json")
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(debug_settings, f, ensure_ascii=False, indent=2)
        print(Color.GREEN + f"[+] 创建调试配置文件: {config_path}" + Color.END)
    except Exception as e:
        print(Color.RED + f"[-] 创建配置文件失败: {e}" + Color.END)
        return False
    
    # 搜索并修改现有配置文件
    modified_count = 0
    for root, dirs, files in os.walk(target_directory):
        # 限制搜索深度
        if root.count(os.sep) - target_directory.count(os.sep) > 5:
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
                        ('"inspect": false', '"inspect": true'),
                        ('"inspect":false', '"inspect":true'),
                        ('"show_devtools": false', '"show_devtools": true'),
                        ('"show_devtools":false', '"show_devtools":true'),
                    ]
                    
                    original_content = content
                    for old, new in replacements:
                        content = content.replace(old, new)
                        
                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(Color.GREEN + f"[+] 修改配置文件: {file_path}" + Color.END)
                        modified_count += 1
                        
                except Exception as e:
                    pass
    
    print(Color.GREEN + f"[+] 共修改了 {modified_count} 个文件" + Color.END)
    return True

def create_instructions(target_directory):
    """
    创建操作说明
    """
    instructions = f"""
微信小程序调试设置
================

已对以下目录进行了调试设置：
{target_directory}

操作步骤：
1. 完全关闭微信客户端
2. 重新启动微信
3. 打开任意小程序
4. 查看是否出现调试功能（通常通过右键菜单或F12键访问）

如果仍然无法看到调试界面：

方法一：检查文件是否生效
- 打开 {target_directory} 目录
- 查看是否存在 debug_config.json 文件
- 用文本编辑器打开该文件，确认内容包含：
  {{
    "debug": true,
    "enable_vconsole": true,
    "devtools": true
  }}

方法二：使用微信官方开发者工具
1. 下载微信开发者工具：
   https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
2. 使用USB调试连接手机微信
3. 在开发者工具中调试小程序

注意事项：
- 微信4.1.0版本可能已禁用传统调试方法
- 本工具仅供学习交流使用
- 建议使用官方开发者工具进行调试
"""
    
    instruction_path = os.path.join(target_directory, "调试说明.txt")
    with open(instruction_path, 'w', encoding='utf-8') as f:
        f.write(instructions)
    print(Color.GREEN + f"[+] 创建说明文件: {instruction_path}" + Color.END)
    
    return instruction_path

def main():
    # 指定的微信文件目录
    target_directory = r"C:\Users\ThinkPad\Documents\xwechat_files"
    
    print(Color.GREEN + """
===============================
微信小程序调试专用解决方案
===============================
    """ + Color.END)
    
    # 启用调试
    if enable_debug_in_directory(target_directory):
        # 创建说明文件
        create_instructions(target_directory)
        
        print(Color.GREEN + """
===============================
操作完成
===============================

请按以下步骤操作：
1. 完全关闭微信客户端
2. 重新启动微信
3. 打开小程序查看调试功能

注意事项：
- 微信4.1.0可能已禁用传统调试方法
- 如无效建议使用官方开发者工具
        """ + Color.END)
    else:
        print(Color.RED + "[-] 操作失败" + Color.END)

if __name__ == "__main__":
    main()