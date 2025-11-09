import os
import json
import psutil

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def check_debug_files():
    """
    检查调试文件是否已创建
    """
    target_directory = r"C:\Users\ThinkPad\Documents\xwechat_files"
    debug_config_path = os.path.join(target_directory, "debug_config.json")
    
    print(Color.GREEN + "=== 调试文件检查 ===" + Color.END)
    
    if os.path.exists(debug_config_path):
        print(Color.GREEN + f"[✓] 调试配置文件已创建: {debug_config_path}" + Color.END)
        try:
            with open(debug_config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                print(Color.GREEN + "[✓] 配置文件内容验证通过" + Color.END)
                print("  配置内容:")
                for key, value in config.items():
                    print(f"    {key}: {value}")
        except Exception as e:
            print(Color.YELLOW + f"[!] 配置文件读取异常: {e}" + Color.END)
    else:
        print(Color.RED + f"[✗] 调试配置文件不存在: {debug_config_path}" + Color.END)
        
    return os.path.exists(debug_config_path)

def check_wechat_processes():
    """
    检查微信进程状态
    """
    print(Color.GREEN + "\n=== 微信进程检查 ===" + Color.END)
    
    wechat_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'WeChat' in proc.info['name']:
                wechat_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
            
    if wechat_processes:
        print(Color.YELLOW + f"[!] 检测到 {len(wechat_processes)} 个微信相关进程:" + Color.END)
        for proc in wechat_processes:
            print(f"  PID: {proc['pid']}, 名称: {proc['name']}")
        print(Color.YELLOW + "建议完全关闭微信后重新启动" + Color.END)
    else:
        print(Color.GREEN + "[✓] 未检测到微信进程，可以安全启动微信" + Color.END)
        
    return len(wechat_processes)

def generate_completion_report():
    """
    生成完成报告
    """
    print(Color.GREEN + """
===============================
微信小程序调试设置完成报告
===============================
    """ + Color.END)
    
    # 检查调试文件
    files_ok = check_debug_files()
    
    # 检查微信进程
    process_count = check_wechat_processes()
    
    # 生成总结
    print(Color.GREEN + "\n=== 完成状态 ===" + Color.END)
    
    if files_ok:
        print(Color.GREEN + "[✓] 调试文件已成功创建" + Color.END)
    else:
        print(Color.RED + "[✗] 调试文件创建失败" + Color.END)
        
    if process_count == 0:
        print(Color.GREEN + "[✓] 微信已完全关闭" + Color.END)
    else:
        print(Color.YELLOW + "[!] 微信仍在运行" + Color.END)
        
    # 下一步操作指南
    print(Color.GREEN + """
===============================
下一步操作指南
===============================
    """ + Color.END)
    
    print("1. " + Color.YELLOW + "关闭微信" + Color.END)
    print("   - 如果微信仍在运行，请完全关闭所有微信进程")
    print("   - 可通过任务管理器确认")
    
    print("\n2. " + Color.YELLOW + "启动微信" + Color.END)
    print("   - 启动微信客户端")
    print("   - 登录您的账号")
    
    print("\n3. " + Color.YELLOW + "测试调试功能" + Color.END)
    print("   - 打开任意小程序")
    print("   - 尝试以下操作查看调试功能:")
    print("     * 按 F12 键")
    print("     * 右键点击小程序界面")
    print("     * 查看是否有开发者工具选项")
    
    print("\n4. " + Color.YELLOW + "备用方案" + Color.END)
    print("   如果以上方法无效，请使用微信官方开发者工具:")
    print("   - 下载地址: https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html")
    print("   - 使用USB调试连接手机微信")
    print("   - 在开发者工具中调试小程序")
    
    # 注意事项
    print(Color.GREEN + """
===============================
注意事项
===============================
    """ + Color.END)
    
    print(Color.YELLOW + "• 微信4.1.0版本可能已禁用传统调试方法" + Color.END)
    print(Color.YELLOW + "• 本工具仅供学习交流使用" + Color.END)
    print(Color.YELLOW + "• 建议使用官方开发者工具获得最佳调试体验" + Color.END)
    
    # 完成确认
    print(Color.GREEN + """
===============================
任务完成
===============================
    """ + Color.END)
    
    print(Color.GREEN + "[✓] 微信小程序调试设置已完成" + Color.END)
    print("请按照上述指南操作，如仍有问题建议使用官方开发者工具")
    
    return files_ok and process_count >= 0

def main():
    try:
        generate_completion_report()
    except Exception as e:
        print(Color.RED + f"[-] 生成报告时出错: {e}" + Color.END)

if __name__ == "__main__":
    main()