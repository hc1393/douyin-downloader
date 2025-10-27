# GitHub自动提交工具

## 简介

这是一个用于自动化执行Git提交流程的Python脚本，可以自动完成`git add`、`git commit`和`git push`操作。

## 功能特点

- 自动添加文件到暂存区
- 自动生成提交信息
- 自动推送到远程仓库
- 支持自定义提交信息和文件列表
- 支持指定远程仓库和分支
- 错误处理和用户友好的输出

## 使用方法

### 基本使用

```bash
# 在当前目录执行自动提交
python github_auto_commit.py

# 指定提交信息
python github_auto_commit.py -m "提交信息"

# 提交特定文件
python github_auto_commit.py -f file1.py file2.py

# 指定远程仓库和分支
python github_auto_commit.py -r origin -b main
```

### 详细参数说明

```bash
usage: github_auto_commit.py [-h] [-m MESSAGE] [-f [FILES ...]] [-r REMOTE] [-b BRANCH] [-p PATH]

GitHub自动提交工具

optional arguments:
  -h, --help            显示帮助信息并退出
  -m MESSAGE, --message MESSAGE
                        提交信息
  -f [FILES ...], --files [FILES ...]
                        要提交的文件列表
  -r REMOTE, --remote REMOTE
                        远程仓库名称 (默认: origin)
  -b BRANCH, --branch BRANCH
                        分支名称 (默认: 当前分支)
  -p PATH, --path PATH  Git仓库路径 (默认: 当前目录)
```

### 使用示例

1. **基本自动提交**：
   ```bash
   python github_auto_commit.py
   ```

2. **带提交信息的提交**：
   ```bash
   python github_auto_commit.py -m "更新README文件"
   ```

3. **提交特定文件**：
   ```bash
   python github_auto_commit.py -f src/main.py docs/readme.md
   ```

4. **指定远程仓库和分支**：
   ```bash
   python github_auto_commit.py -r upstream -b develop
   ```

5. **在特定目录执行**：
   ```bash
   python github_auto_commit.py -p /path/to/repo -m "更新配置文件"
   ```

## 代码说明

### 主要类和方法

- `GitHubAutoCommit`: 主要的提交工具类
  - `__init__(repo_path)`: 初始化工具
  - `run_command(command)`: 执行系统命令
  - `check_git_status()`: 检查Git状态
  - `add_files(files)`: 添加文件到暂存区
  - `commit_changes(message)`: 提交更改
  - `push_changes(remote, branch)`: 推送更改
  - `get_current_branch()`: 获取当前分支
  - `auto_commit(message, files, remote, branch)`: 自动执行完整提交流程

## 注意事项

1. 确保已经在目标目录初始化了Git仓库
2. 确保有网络连接以推送更改
3. 确保有正确的权限访问远程仓库
4. 如果使用SSH密钥认证，确保已正确配置SSH密钥
5. 如果使用HTTPS认证，可能需要输入用户名和密码或个人访问令牌

## 常见问题

### 1. 推送时要求输入用户名和密码
这是正常的，如果使用HTTPS方式访问GitHub，需要输入凭据。可以考虑配置SSH密钥或使用Git凭据存储。

### 2. 提示"没有需要提交的更改"
这表示工作目录是干净的，没有需要提交的更改。

### 3. 权限被拒绝
确保您有权限推送到指定的远程仓库和分支。

## 扩展功能

可以根据需要扩展此工具，例如：
- 添加标签支持
- 支持提交前运行测试
- 添加更详细的日志记录
- 支持配置文件
- 添加回滚功能