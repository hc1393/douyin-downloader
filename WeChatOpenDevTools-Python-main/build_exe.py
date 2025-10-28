import os
import sys
from pathlib import Path

def create_executable():
    """Create executable using PyInstaller"""
    print("开始打包 WeChatOpenDevTools...")
    
    # 获取当前目录
    current_dir = Path(__file__).parent.absolute()
    os.chdir(current_dir)
    
    # 安装 PyInstaller（如果尚未安装）
    try:
        import PyInstaller
    except ImportError:
        print("正在安装 PyInstaller...")
        os.system(f"{sys.executable} -m pip install pyinstaller")
    
    # 创建 spec 文件
    spec_content = '''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('configs/*', 'configs'),
        ('scripts/*', 'scripts'),
        ('utils/*', 'utils'),
    ],
    hiddenimports=[
        'argparse',
        'frida',
        'psutil',
        'pyfiglet',
        'utils.commons',
        'utils.banner',
        'utils.colors',
        'utils.cleanup',
        'utils.wechatutils'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='WechatOpenDevTools',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    # 写入 spec 文件
    with open('WechatOpenDevTools.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    # 运行 PyInstaller
    print("正在打包 exe 文件...")
    result = os.system('pyinstaller WechatOpenDevTools.spec')
    
    if result == 0:
        print("打包完成！")
        print("可执行文件位置: dist/WechatOpenDevTools.exe")
    else:
        print("打包失败，请检查错误信息")

if __name__ == "__main__":
    create_executable()