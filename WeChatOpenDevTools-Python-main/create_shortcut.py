import os
import sys
import shutil
from pathlib import Path

def create_desktop_shortcut():
    """在桌面创建 WechatOpenDevTools 的快捷方式"""
    try:
        # 获取桌面路径
        desktop = Path.home() / "Desktop"
        
        # 获取可执行文件路径
        exe_path = Path("F:/PythonProject/WeChatOpenDevTools-Python-main/dist/WechatOpenDevTools.exe")
        
        # 检查 exe 文件是否存在
        if not exe_path.exists():
            print("错误：未找到 WechatOpenDevTools.exe 文件")
            print(f"请确保文件存在于: {exe_path}")
            return False
            
        # 创建 .lnk 快捷方式文件的路径
        shortcut_path = desktop / "WechatOpenDevTools.lnk"
        
        # 使用 Windows 的 mklink 命令创建快捷方式
        # 实际上，我们将创建一个批处理文件作为替代方案
        
        # 创建批处理文件
        bat_content = f"""@echo off
cd /d "{exe_path.parent}"
"{exe_path.name}" %*
"""
        
        bat_path = desktop / "WechatOpenDevTools.bat"
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write(bat_content)
        
        print(f"已在桌面创建快捷方式: {bat_path}")
        print("双击桌面上的 WechatOpenDevTools.bat 即可运行程序")
        print("\n使用方法:")
        print("- 双击运行程序（显示帮助信息）")
        print("- 右键编辑批处理文件可以添加默认参数")
        
        return True
        
    except Exception as e:
        print(f"创建快捷方式时出错: {e}")
        return False

if __name__ == "__main__":
    create_desktop_shortcut()