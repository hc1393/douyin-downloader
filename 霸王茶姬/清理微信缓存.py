import os
import shutil
import sys
from pathlib import Path

def clean_wechat_cache():
    """
    清理微信相关缓存目录
    """
    # 获取AppData目录
    appdata_path = os.getenv('APPDATA')
    if not appdata_path:
        print("无法获取APPDATA路径")
        return False
    
    # 定义需要删除的目录路径
    paths_to_clean = [
        os.path.join(appdata_path, 'Tencent', 'WeChat', 'radium', 'WmpfCache'),
        os.path.join(appdata_path, 'Tencent', 'WeChat', 'XPlugin', 'Plugins', 'RadiumWMPF')
    ]
    
    success_count = 0
    for path in paths_to_clean:
        try:
            # 检查路径是否存在
            if os.path.exists(path):
                # 如果是目录，删除整个目录
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print(f"已删除目录: {path}")
                # 如果是文件，删除文件
                elif os.path.isfile(path):
                    os.remove(path)
                    print(f"已删除文件: {path}")
                success_count += 1
            else:
                print(f"路径不存在: {path}")
        except Exception as e:
            print(f"删除 {path} 时出错: {e}")
    
    print(f"\n清理完成，成功处理 {success_count}/{len(paths_to_clean)} 个路径")
    return success_count > 0

if __name__ == "__main__":
    print("微信缓存清理工具")
    print("=" * 30)
    
    # 确认操作
    confirm = input("确定要删除微信相关缓存文件吗？(y/N): ")
    if confirm.lower() not in ['y', 'yes', '是']:
        print("操作已取消")
        sys.exit(0)
    
    # 执行清理
    clean_wechat_cache()
    
    input("\n按回车键退出...")