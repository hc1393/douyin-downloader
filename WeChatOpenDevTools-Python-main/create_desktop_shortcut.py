import os
from pathlib import Path

# 获取桌面路径
desktop = Path.home() / "Desktop"
exe_path = Path("F:/PythonProject/WeChatOpenDevTools-Python-main/dist/WechatOpenDevTools.exe")

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
print("双击桌面上的 WechatOpenDevTools.bat 即可运行程序")