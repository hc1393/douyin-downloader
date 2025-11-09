# 微信小程序调试工具设计方案 (支持最新版本)

## 1. 现状分析

当前工具支持的最新版本为11275，根据配置文件分析，主要通过Hook特定地址实现功能：
- LaunchAppletBegin: 小程序启动时Hook点
- MenuItemDevToolsString: 开发者工具菜单项
- SwitchVersion: 版本切换相关函数
- Version: 版本号

## 2. 设计目标

1. 支持自动识别和适配最新微信版本
2. 提供更友好的用户界面
3. 增强错误处理和调试信息
4. 实现版本自动更新机制
5. 支持更多调试功能

## 3. 核心功能模块设计

### 3.1 版本检测模块
```python
class VersionDetector:
    def __init__(self):
        self.supported_versions = self.load_supported_versions()
    
    def detect_wechat_version(self):
        # 检测当前运行的微信版本
        pass
    
    def detect_miniprogram_version(self):
        # 检测当前运行的小程序版本
        pass
    
    def is_version_supported(self, version):
        # 检查版本是否被支持
        pass
```

### 3.2 Hook地址管理模块
```python
class HookAddressManager:
    def __init__(self):
        self.address_configs = {}
        self.load_address_configs()
    
    def load_address_configs(self):
        # 从configs目录加载所有版本的地址配置
        pass
    
    def get_address_config(self, version):
        # 获取指定版本的地址配置
        pass
    
    def auto_generate_config(self, version):
        # 尝试自动生成新版本的地址配置
        pass
```

### 3.3 注入器模块
```python
class Injector:
    def __init__(self):
        self.frida_device = frida.get_local_device()
    
    def inject_to_process(self, pid, script):
        # 注入脚本到指定进程
        pass
    
    def spawn_and_inject(self, executable_path, script):
        # 启动进程并注入脚本
        pass
```

### 3.4 脚本生成器模块
```python
class ScriptGenerator:
    def generate_hook_script(self, address_config):
        # 根据地址配置生成Hook脚本
        pass
    
    def generate_devtools_script(self):
        # 生成开发者工具启用脚本
        pass
```

## 4. 新增功能设计

### 4.1 自动版本适配
- 实现基于模式匹配的地址自动查找
- 提供半自动配置生成功能
- 支持用户提交新版本配置

### 4.2 图形化界面
```python
class MainWindow:
    def __init__(self):
        # 初始化主窗口
        pass
    
    def create_ui(self):
        # 创建用户界面
        # 1. 版本信息显示
        # 2. 功能按钮（开启F12、开启网络面板等）
        # 3. 日志显示区域
        # 4. 设置选项
        pass
```

### 4.3 网络请求监控
- 拦截并记录小程序网络请求
- 显示请求详情（URL、headers、body等）
- 支持请求重放功能

### 4.4 数据存储查看器
- 查看小程序本地存储数据
- 支持查看和编辑localStorage、sessionStorage
- 支持查看小程序的文件系统

## 5. 技术实现方案

### 5.1 使用的技术栈
- Python 3.x 作为主程序语言
- Frida 用于Hook注入
- PyQt5/PySide2 用于图形界面
- Requests 用于网络功能
- psutil 用于进程管理

### 5.2 目录结构调整
```
WeChatOpenDevTools-v2/
├── configs/                 # 版本地址配置文件
├── core/                    # 核心模块
│   ├── detector.py          # 版本检测模块
│   ├── injector.py          # 注入器模块
│   ├── script_generator.py  # 脚本生成器模块
│   └── address_manager.py   # 地址管理模块
├── gui/                     # 图形界面模块
│   ├── main_window.py       # 主窗口
│   ├── logger_panel.py      # 日志面板
│   └── settings_dialog.py   # 设置对话框
├── utils/                   # 工具模块
├── scripts/                 # 注入脚本模板
├── templates/               # 界面模板
├── main.py                  # 程序入口
└── requirements.txt         # 依赖列表
```

## 6. 使用流程设计

1. 用户启动程序
2. 自动检测当前微信和小程序版本
3. 检查版本是否支持
4. 如果支持，则直接注入；如果不支持，尝试自动适配或提示用户
5. 提供图形界面供用户操作各种调试功能
6. 实时显示调试信息和日志

## 7. 扩展性考虑

1. 插件化架构设计，便于添加新功能
2. 支持在线更新地址配置
3. 提供API供第三方工具集成
4. 支持多平台（Windows、Mac）

## 8. 安全与合规

1. 仅用于学习和开发目的
2. 不修改微信核心功能
3. 不收集用户隐私信息
4. 提供明确的免责声明