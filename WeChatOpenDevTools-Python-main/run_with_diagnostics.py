import subprocess
import sys
import os
import time

def run_with_diagnostics():
    """以诊断模式运行 WechatOpenDevTools"""
    try:
        # 获取可执行文件路径
        exe_path = os.path.join(os.path.dirname(__file__), "dist", "WechatOpenDevTools.exe")
        
        if not os.path.exists(exe_path):
            print("错误: 未找到 WechatOpenDevTools.exe")
            print(f"请确认文件存在于: {exe_path}")
            input("按回车键退出...")
            return
            
        print("WechatOpenDevTools 诊断运行器")
        print("=" * 40)
        print("1. 确保以管理员身份运行此程序")
        print("2. 确保微信正在运行")
        print("3. 选择要执行的功能:")
        print("   a) 显示帮助 (-h)")
        print("   b) 开启小程序F12 (-x)")
        print("   c) 开启内置浏览器F12 (-c)")
        print("   d) 开启所有F12 (-all)")
        print("   e) 跟踪小程序Cookie (-cookie)")
        print("   f) 清理微信缓存 (-clean)")
        print("")
        
        choice = input("请输入选项 (a-f) 或按回车显示帮助: ").strip().lower()
        
        args_map = {
            'a': ['-h'],
            'b': ['-x'],
            'c': ['-c'],
            'd': ['-all'],
            'e': ['-cookie'],
            'f': ['-clean'],
            '': ['-h']
        }
        
        args = args_map.get(choice, ['-h'])
        
        print(f"\n正在运行: {exe_path} {' '.join(args)}")
        print("如果程序立即退出，请检查:")
        print("1. 是否以管理员身份运行")
        print("2. 微信是否正在运行")
        print("3. 控制台是否有错误信息")
        print("-" * 40)
        
        # 运行程序
        process = subprocess.Popen([exe_path] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # 实时输出
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
                
        # 获取剩余输出
        stderr_output = process.stderr.read()
        if stderr_output:
            print("错误输出:")
            print(stderr_output)
            
        rc = process.poll()
        print(f"\n程序退出，返回码: {rc}")
        
    except Exception as e:
        print(f"运行时发生错误: {e}")
        
    input("\n按回车键退出...")

if __name__ == "__main__":
    run_with_diagnostics()