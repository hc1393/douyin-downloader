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
        exe_path = Path(__file__).parent / "dist" / "WechatOpenDevTools.exe"
        
        # 检查 exe 文件是否存在
        if not exe_path.exists():
            print("错误：未找到 WechatOpenDevTools.exe 文件")
            print(f"请确保文件存在于: {exe_path}")
            return False
            
        # 创建批处理文件
        bat_content = f"""@echo off
REM WechatOpenDevTools 快捷启动脚本
cd /d "{exe_path.parent}"
"{exe_path.name}" %*
"""
        
        bat_path = desktop / "WechatOpenDevTools.bat"
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write(bat_content)
        
        print(f"已在桌面创建快捷方式: {bat_path}")
        print("双击桌面上的 WechatOpenDevTools.bat 即可运行程序")
        print("\n使用方法:")
        print("1. 双击运行程序（显示帮助信息）")
        print("2. 右键编辑批处理文件可以添加默认参数")
        print("3. 以管理员身份运行以获得完整功能")
        
        return True
        
    except Exception as e:
        print(f"创建快捷方式时出错: {e}")
        return False

if __name__ == "__main__":
    create_desktop_shortcut()
    input("\n按回车键退出...")