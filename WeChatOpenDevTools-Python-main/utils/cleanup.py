import os
import shutil
import sys
from utils.colors import Color

class CleanupUtils:
    def __init__(self):
        # 微信相关路径列表
        self.wechat_paths = [
            os.path.expanduser(r"~\AppData\Roaming\Tencent\WeChat\radium\WmpfCache"),
            os.path.expanduser(r"~\AppData\Roaming\Tencent\WeChat\XPlugin\Plugins\RadiumWMPF")
        ]

    def force_remove_readonly(self, func, path, excinfo):
        """
        强制删除只读文件的错误处理函数
        """
        try:
            os.chmod(path, 0o777)  # 添加所有权限
            func(path)
        except Exception as e:
            print(Color.RED + f"[-] 无法删除 {path}: {e}" + Color.END)

    def clean_path(self, path):
        """
        清理指定路径
        """
        if not os.path.exists(path):
            print(Color.YELLOW + f"[!] 路径不存在: {path}" + Color.END)
            return False

        try:
            if os.path.isfile(path):
                os.chmod(path, 0o777)  # 确保有写权限
                os.remove(path)
                print(Color.GREEN + f"[+] 成功删除文件: {path}" + Color.END)
            elif os.path.isdir(path):
                shutil.rmtree(path, onerror=self.force_remove_readonly)
                print(Color.GREEN + f"[+] 成功删除目录: {path}" + Color.END)
            return True
        except PermissionError:
            print(Color.RED + f"[-] 权限被拒绝: {path}" + Color.END)
            # 尝试使用Windows工具强制删除
            try:
                # 在Windows上尝试使用takeown和icacls获取所有权和权限
                os.system(f'takeown /f "{path}" /r /d y > nul 2>&1')
                os.system(f'icacls "{path}" /grant administrators:F /t > nul 2>&1')
                if os.path.isdir(path):
                    shutil.rmtree(path, onerror=self.force_remove_readonly)
                else:
                    os.chmod(path, 0o777)
                    os.remove(path)
                print(Color.GREEN + f"[+] 强制删除成功: {path}" + Color.END)
                return True
            except Exception as e:
                print(Color.RED + f"[-] 强制删除失败 {path}: {e}" + Color.END)
                return False
        except Exception as e:
            print(Color.RED + f"[-] 删除失败 {path}: {e}" + Color.END)
            return False

    def clean_wechat_cache(self):
        """
        清理微信缓存
        """
        print(Color.GREEN + "[*] 开始清理微信缓存..." + Color.END)
        success_count = 0
        total_count = len(self.wechat_paths)

        for path in self.wechat_paths:
            print(f"正在处理: {path}")
            if self.clean_path(path):
                success_count += 1

        print(Color.GREEN + f"[+] 清理完成，成功处理 {success_count}/{total_count} 个路径" + Color.END)
        return success_count, total_count

if __name__ == "__main__":
    cleanup = CleanupUtils()
    cleanup.clean_wechat_cache()