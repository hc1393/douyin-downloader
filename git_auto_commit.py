import subprocess
import sys
import os
from datetime import datetime, timedelta
import time
import argparse

def run_command(command, cwd=None, timeout=30):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd,
            capture_output=True, 
            text=True,
            encoding='utf-8',
            timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -2, "", f"命令执行超时 ({timeout}秒)"
    except Exception as e:
        return -1, "", str(e)

def check_git_status():
    """检查Git状态"""
    print("检查Git仓库状态...")
    code, stdout, stderr = run_command("git status", timeout=10)
    
    if code != 0:
        if "not a git repository" in stderr:
            print("错误: 当前目录不是Git仓库")
            return False
        else:
            print(f"错误: 无法检查Git状态 - {stderr}")
            return False
    
    print("Git仓库状态检查完成")
    return True

def check_git_config():
    """检查Git配置"""
    print("检查Git配置...")
    code, stdout, stderr = run_command("git config --list", timeout=10)
    
    if code != 0:
        print(f"警告: 无法获取Git配置 - {stderr}")
        return False
    
    # 检查必要的配置
    has_user_name = "user.name" in stdout
    has_user_email = "user.email" in stdout
    
    if not has_user_name:
        print("警告: 未设置Git用户名")
    if not has_user_email:
        print("警告: 未设置Git邮箱")
        
    return has_user_name and has_user_email

def add_files():
    """添加文件到暂存区"""
    print("添加文件到暂存区...")
    code, stdout, stderr = run_command("git add .", timeout=20)
    
    if code != 0:
        print(f"错误: 添加文件失败 - {stderr}")
        return False
    
    print("文件添加完成")
    return True

def check_changes_to_commit():
    """检查是否有更改需要提交"""
    print("检查是否有更改需要提交...")
    code, stdout, stderr = run_command("git diff --cached --name-only", timeout=10)
    
    if code != 0:
        print(f"错误: 无法检查暂存区更改 - {stderr}")
        return False
    
    files_to_commit = stdout.strip().split('\n') if stdout.strip() else []
    
    if not files_to_commit or (len(files_to_commit) == 1 and files_to_commit[0] == ''):
        print("没有文件需要提交")
        return False
    
    print(f"以下文件将被提交:")
    for file in files_to_commit:
        if file:  # 避免打印空行
            print(f"  {file}")
    return True

def commit_changes(message=None):
    """提交更改"""
    if not message:
        commit_message = f"Auto commit at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    else:
        commit_message = message
    print(f"提交更改: {commit_message}")
    
    code, stdout, stderr = run_command(f'git commit -m "{commit_message}"', timeout=20)
    
    if code != 0:
        if "nothing to commit" in stderr or "nothing added to commit" in stderr:
            print("没有更改需要提交")
            return False
        elif "Please tell me who you are" in stderr:
            print("错误: 请配置Git用户信息")
            print("运行以下命令配置:")
            print('  git config --global user.name "Your Name"')
            print('  git config --global user.email "your.email@example.com"')
            return False
        else:
            print(f"错误: 提交失败 - {stderr}")
            return False
    
    print("提交成功")
    print(stdout)
    return True

def push_changes():
    """推送更改到远程仓库"""
    print("推送更改到远程仓库... (超时时间: 60秒)")
    code, stdout, stderr = run_command("git push", timeout=60)
    
    if code != 0:
        if code == -2:  # 超时
            print("错误: 推送超时，可能是网络连接问题")
            return False
        elif "fatal: No configured push destination" in stderr:
            print("警告: 未设置远程仓库，跳过推送")
            return True
        elif "Permission denied" in stderr or "Authentication failed" in stderr:
            print("错误: 推送权限不足，请检查您的Git凭据")
            print("您可能需要配置SSH密钥或使用个人访问令牌")
            return False
        else:
            print(f"错误: 推送失败 - {stderr}")
            return False
    
    print("推送完成")
    print(stdout)
    return True

def schedule_commit(target_time):
    """定时提交"""
    print(f"设置定时提交任务，目标时间: {target_time}")
    
    # 解析目标时间
    try:
        target_datetime = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("错误: 时间格式不正确，请使用 YYYY-MM-DD HH:MM:SS 格式")
        return False
    
    # 计算等待时间
    now = datetime.now()
    if target_datetime <= now:
        print("错误: 目标时间必须晚于当前时间")
        return False
    
    wait_seconds = (target_datetime - now).total_seconds()
    print(f"将在 {wait_seconds} 秒后执行提交 ({target_datetime.strftime('%Y-%m-%d %H:%M:%S')})")
    
    # 等待到指定时间
    while datetime.now() < target_datetime:
        time.sleep(1)
    
    print("到达指定时间，开始执行提交...")
    return True

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="Git自动提交工具")
    parser.add_argument("-m", "--message", help="提交信息")
    parser.add_argument("-t", "--time", help="定时提交时间 (格式: YYYY-MM-DD HH:MM:SS)")
    
    args = parser.parse_args()
    
    print(f"开始Git自动提交流程: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 如果指定了定时提交时间
    if args.time:
        if not schedule_commit(args.time):
            sys.exit(1)
    
    # 检查是否在Git仓库中
    if not check_git_status():
        sys.exit(1)
    
    # 检查Git配置
    check_git_config()
    
    # 添加文件
    if not add_files():
        sys.exit(1)
    
    # 检查是否有更改需要提交
    if not check_changes_to_commit():
        print("没有更改需要提交，流程结束")
        return
    
    # 提交更改
    if not commit_changes(args.message):
        sys.exit(1)
    
    # 推送更改
    if not push_changes():
        print("推送失败，但本地提交已完成")
        sys.exit(1)
    
    print("自动提交流程完成")

if __name__ == "__main__":
    main()