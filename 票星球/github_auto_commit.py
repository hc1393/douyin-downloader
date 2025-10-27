#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitHub自动提交工具
用于自动化执行Git add、commit和push操作
"""

import os
import sys
import subprocess
import argparse
from datetime import datetime

class GitHubAutoCommit:
    def __init__(self, repo_path=None):
        """
        初始化GitHub自动提交工具
        
        :param repo_path: Git仓库路径，默认为当前目录
        """
        self.repo_path = repo_path or os.getcwd()
        
    def run_command(self, command, cwd=None):
        """
        执行命令并返回结果
        
        :param command: 要执行的命令
        :param cwd: 工作目录
        :return: 命令执行结果
        """
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                cwd=cwd or self.repo_path,
                capture_output=True, 
                text=True,
                encoding='utf-8'
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", str(e)
    
    def check_git_status(self):
        """
        检查Git仓库状态
        
        :return: 状态信息
        """
        code, stdout, stderr = self.run_command("git status")
        if code != 0:
            raise Exception(f"无法检查Git状态: {stderr}")
        return stdout
    
    def add_files(self, files=None):
        """
        添加文件到暂存区
        
        :param files: 要添加的文件列表，如果为None则添加所有文件
        """
        if files is None:
            command = "git add ."
        else:
            # 转义文件名中的特殊字符
            escaped_files = [f'"{file}"' for file in files]
            command = f"git add {' '.join(escaped_files)}"
        
        code, stdout, stderr = self.run_command(command)
        if code != 0:
            raise Exception(f"添加文件失败: {stderr}")
        return stdout
    
    def commit_changes(self, message):
        """
        提交更改
        
        :param message: 提交信息
        """
        # 转义提交信息中的特殊字符
        escaped_message = message.replace('"', '\\"')
        command = f'git commit -m "{escaped_message}"'
        
        code, stdout, stderr = self.run_command(command)
        if code != 0:
            # 检查是否是因为没有更改而失败
            if "nothing to commit" in stderr or "nothing added to commit" in stderr:
                return "没有需要提交的更改"
            raise Exception(f"提交失败: {stderr}")
        return stdout
    
    def push_changes(self, remote="origin", branch="main"):
        """
        推送更改到远程仓库
        
        :param remote: 远程仓库名称
        :param branch: 分支名称
        """
        command = f"git push {remote} {branch}"
        
        code, stdout, stderr = self.run_command(command)
        if code != 0:
            raise Exception(f"推送失败: {stderr}")
        return stdout
    
    def get_current_branch(self):
        """
        获取当前分支名称
        
        :return: 当前分支名称
        """
        code, stdout, stderr = self.run_command("git branch --show-current")
        if code != 0:
            raise Exception(f"无法获取当前分支: {stderr}")
        return stdout.strip()
    
    def auto_commit(self, message=None, files=None, remote="origin", branch=None):
        """
        自动执行完整的提交流程
        
        :param message: 提交信息
        :param files: 要提交的文件列表
        :param remote: 远程仓库名称
        :param branch: 分支名称
        """
        try:
            print("🔍 检查Git仓库状态...")
            status = self.check_git_status()
            print("✅ Git仓库状态检查完成")
            
            # 如果没有提供提交信息，则生成默认信息
            if not message:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = f"Auto commit at {timestamp}"
            
            print("➕ 添加文件到暂存区...")
            self.add_files(files)
            print("✅ 文件添加完成")
            
            print(f"📝 提交更改: {message}")
            commit_result = self.commit_changes(message)
            print(f"✅ 提交完成: {commit_result}")
            
            # 如果没有需要提交的更改，则直接返回
            if commit_result == "没有需要提交的更改":
                return commit_result
            
            # 如果没有指定分支，则使用当前分支
            if not branch:
                branch = self.get_current_branch()
            
            print(f"🚀 推送更改到 {remote}/{branch}...")
            push_result = self.push_changes(remote, branch)
            print("✅ 推送完成")
            
            return "提交成功完成"
            
        except Exception as e:
            raise Exception(f"自动提交过程中发生错误: {str(e)}")

def main():
    """
    主函数
    """
    parser = argparse.ArgumentParser(description="GitHub自动提交工具")
    parser.add_argument("-m", "--message", help="提交信息")
    parser.add_argument("-f", "--files", nargs="*", help="要提交的文件列表")
    parser.add_argument("-r", "--remote", default="origin", help="远程仓库名称 (默认: origin)")
    parser.add_argument("-b", "--branch", help="分支名称 (默认: 当前分支)")
    parser.add_argument("-p", "--path", help="Git仓库路径 (默认: 当前目录)")
    
    args = parser.parse_args()
    
    try:
        # 创建自动提交工具实例
        auto_commit = GitHubAutoCommit(args.path)
        
        # 执行自动提交
        result = auto_commit.auto_commit(
            message=args.message,
            files=args.files,
            remote=args.remote,
            branch=args.branch
        )
        
        print(f"\n🎉 {result}")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()