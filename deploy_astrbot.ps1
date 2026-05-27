# AstrBot 自动部署脚本
# 使用方法：在 PowerShell 中运行 .\deploy_astrbot.ps1

$serverIP = "183.66.27.21"
$serverPort = "34921"
$username = "root"
$password = "ybMZpJyOAo0qABW7"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  AstrBot 自动部署脚本" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查是否安装了 sshpass（Windows 通常没有）
Write-Host "正在连接到服务器..." -ForegroundColor Yellow

# 由于 Windows PowerShell 不支持自动输入 SSH 密码
# 我们将使用 Plink（PuTTY 的工具）或手动方式

Write-Host ""
Write-Host "由于安全限制，SSH 需要手动输入密码。" -ForegroundColor Red
Write-Host ""
Write-Host "请按照以下步骤操作：" -ForegroundColor Green
Write-Host ""
Write-Host "1. 打开 PowerShell，运行以下命令连接服务器：" -ForegroundColor White
Write-Host "   ssh -p $serverPort ${username}@${serverIP}" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. 输入密码：$password" -ForegroundColor Yellow
Write-Host ""
Write-Host "3. 连接成功后，复制粘贴以下所有命令并执行：" -ForegroundColor White
Write-Host ""

$commands = @'
# 更新系统
apt update && apt upgrade -y

# 安装必要工具
apt install -y curl wget git vim

# 安装 Docker
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

# 启动 Docker
systemctl start docker
systemctl enable docker

# 验证 Docker 安装
docker --version

# 创建项目目录
mkdir -p ~/astrbot && cd ~/astrbot

# 创建 docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  astrbot:
    image: soulter/astrbot:latest
    container_name: astrbot
    restart: always
    security_opt:
      - no-new-privileges:true
    ports:
      - "6185:6185"
      - "6199:6199"
    environment:
      - TZ=Asia/Shanghai
    volumes:
      - ./data:/AstrBot/data
      - /etc/localtime:/etc/localtime:ro
EOF

# 启动 AstrBot
docker-compose up -d

# 等待服务启动
sleep 15

# 查看日志获取初始密码
docker-compose logs astrbot | grep -A 15 "WebUI is ready"
'@

Write-Host $commands -ForegroundColor Cyan
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "部署完成后，访问：" -ForegroundColor Green
Write-Host "http://${serverIP}:6185" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 提供一键复制功能
Set-Clipboard -Value $commands
Write-Host "✅ 部署命令已复制到剪贴板！" -ForegroundColor Green
Write-Host ""
Write-Host "按任意键退出..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
