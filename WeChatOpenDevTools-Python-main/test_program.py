import subprocess
import time
import os

# 测试程序是否能正常运行并退出
def test_program():
    exe_path = r"F:\PythonProject\WeChatOpenDevTools-Python-main\dist\WechatOpenDevTools.exe"
    
    if not os.path.exists(exe_path):
        print("错误: 找不到可执行文件")
        return False
    
    try:
        # 运行程序并传递 -h 参数
        print("正在测试程序...")
        process = subprocess.Popen(
            [exe_path, "-h"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 等待程序运行几秒钟
        time.sleep(3)
        
        # 检查程序是否仍在运行
        if process.poll() is None:
            # 程序仍在运行，尝试终止它
            process.terminate()
            time.sleep(1)
            
            # 如果仍然运行，强制终止
            if process.poll() is None:
                process.kill()
        
        # 获取输出
        stdout, stderr = process.communicate()
        
        print("程序输出:")
        print(stdout)
        
        if stderr:
            print("错误输出:")
            print(stderr)
            
        print(f"程序退出码: {process.returncode}")
        return True
        
    except Exception as e:
        print(f"测试过程中出错: {e}")
        return False

if __name__ == "__main__":
    test_program()