#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WeChat Open DevTools 完整设置脚本
此脚本将执行以下操作：
1. 使用PyInstaller将项目打包成exe文件
2. 重命名生成的exe文件
3. 在桌面创建快捷方式
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_executable():
    """使用PyInstaller打包项目"""
    print("开始打包 WeChatOpenDevTools...")
    
    # 构建PyInstaller命令
    cmd = [
        "pyinstaller",
        "--onefile",
        "--console",
        "--add-data", "configs;configs",
        "--add-data", "scripts;scripts",
        "--add-data", "utils;utils",
        "--add-data", "WechatOpenDevTools;WechatOpenDevTools",
        "--add-data", "F:\\PythonProject\\.venv\\Lib\\site-packages\\pyfiglet\\fonts;pyfiglet\\fonts",
        "--hidden-import", "frida",
        "--hidden-import", "psutil",
        "--hidden-import", "pyfiglet",
        "main.py"
    ]
    
    try:
        print("执行PyInstaller命令...")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            print("打包成功完成!")
            return True
        else:
            print("打包过程中出现错误:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"执行PyInstaller时出错: {e}")
        return False

def rename_executable():
    """重命名生成的exe文件"""
    try:
        dist_path = Path("dist")
        main_exe = dist_path / "main.exe"
        target_exe = dist_path / "WechatOpenDevTools.exe"
        
        if main_exe.exists():
            if target_exe.exists():
                target_exe.unlink()  # 删除已存在的文件
            main_exe.rename(target_exe)
            print(f"已将 {main_exe.name} 重命名为 {target_exe.name}")
            return True
        else:
            print("未找到生成的exe文件")
            return False
    except Exception as e:
        print(f"重命名exe文件时出错: {e}")
        return False

def create_desktop_shortcut():
    """在桌面创建快捷方式"""
    try:
        # 获取桌面路径
        desktop = Path.home() / "Desktop"
        exe_path = Path(__file__).parent / "dist" / "WechatOpenDevTools.exe"
        
        # 创建批处理文件内容
        bat_content = f"""@echo off
title WechatOpenDevTools
echo WechatOpenDevTools - 微信小程序开发工具增强
echo.

REM 检查文件是否存在
if not exist "{exe_path}" (
    echo 错误：未找到 WechatOpenDevTools.exe
    echo 请确保文件存在于: {exe_path}
    echo.
    pause
    exit /b
)

echo 选择运行模式：
echo 1. 显示帮助信息
echo 2. 开启小程序F12调试
echo 3. 开启内置浏览器F12调试
echo 4. 开启所有F12调试
echo 5. 跟踪小程序Cookie
echo 6. 清理微信缓存文件
echo.
echo 0. 退出
echo.

choice /c 0123456 /m "请选择"
if errorlevel 7 goto :clean
if errorlevel 6 goto :cookie
if errorlevel 5 goto :all
if errorlevel 4 goto :browser
if errorlevel 3 goto :x
if errorlevel 2 goto :help
if errorlevel 1 goto :exit

:help
"{exe_path}" -h
goto :end

:x
"{exe_path}" -x
goto :end

:browser
"{exe_path}" -c
goto :end

:all
"{exe_path}" -all
goto :end

:cookie
"{exe_path}" -cookie
goto :end

:clean
"{exe_path}" -clean
goto :end

:exit
exit /b

:end
echo.
echo 程序已退出
pause
"""
        
        # 写入批处理文件到桌面
        bat_file = desktop / "WechatOpenDevTools.bat"
        with open(bat_file, "w", encoding="utf-8") as f:
            f.write(bat_content)
        
        print(f"已在桌面创建快捷方式: {bat_file}")
        return True
        
    except Exception as e:
        print(f"创建桌面快捷方式时出错: {e}")
        return False

def main():
    """主函数"""
    print("WeChatOpenDevTools 完整设置脚本")
    print("=" * 50)
    
    # 切换到项目目录
    project_dir = Path("F:/PythonProject/WeChatOpenDevTools-Python-main")
    os.chdir(project_dir)
    print(f"当前工作目录: {os.getcwd()}")
    
    # 1. 打包exe文件
    print("\n步骤1: 打包exe文件")
    if not build_executable():
        print("打包失败，脚本退出")
        return
    
    # 2. 重命名exe文件
    print("\n步骤2: 重命名exe文件")
    if not rename_executable():
        print("重命名失败，脚本退出")
        return
    
    # 3. 创建桌面快捷方式
    print("\n步骤3: 创建桌面快捷方式")
    if not create_desktop_shortcut():
        print("创建桌面快捷方式失败")
        return
    
    print("\n所有步骤已完成!")
    print("您现在可以双击桌面上的 WechatOpenDevTools.bat 来运行程序")

if __name__ == "__main__":
    main()
    input("\n按回车键退出...")