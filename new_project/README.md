# douyin_downloader

抖音视频无水印高清下载插件，支持自动检测链接并下载。

## 功能

- 自动检测消息中的抖音链接（短链接/长链接）
- 下载无水印高清视频
- 显示视频详细信息（标题、作者、分辨率、时长、大小）

## 使用方式

### 命令模式
```
/douyin <抖音链接>
```

### 自动检测
直接发送包含抖音链接的消息，插件会自动识别并下载。

## 支持的链接格式

- `https://v.douyin.com/xxxxx/` (短链接)
- `https://www.douyin.com/video/xxxxx` (长链接)
- `https://www.iesdouyin.com/share/video/xxxxx` (分享链接)

## 依赖

- requests

## 安装

1. 将此文件夹复制到 AstrBot 的 `data/plugins/` 目录
2. 重启 AstrBot
3. 在聊天中使用 `/douyin` 命令或直接发送抖音链接
