import psutil
import re
from utils.colors import Color

class VersionDetector:
    """
    微信版本检测器
    """
    
    def __init__(self):
        self.wechat_processes = []
        self.miniprogram_processes = []
        
    def detect_wechat_processes(self):
        """
        检测所有微信相关进程
        """
        self.wechat_processes = []
        self.miniprogram_processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'] == 'WeChat.exe':
                    self.wechat_processes.append(proc.info)
                elif proc.info['name'] == 'WeChatAppEx.exe' or 'WeChatAppEx' in (proc.info['cmdline'] or []):
                    self.miniprogram_processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
                
        return {
            'wechat': self.wechat_processes,
            'miniprogram': self.miniprogram_processes
        }
        
    def extract_miniprogram_version(self, cmdline):
        """
        从命令行参数中提取小程序版本号
        """
        if not cmdline:
            return None
            
        cmdline_str = ' '.join(cmdline)
        version_match = re.search(r'"version":(\d+)', cmdline_str)
        return int(version_match.group(1)) if version_match else None
        
    def print_process_info(self):
        """
        打印进程信息
        """
        processes = self.detect_wechat_processes()
        
        print(Color.GREEN + "[+] 检测到以下微信进程:" + Color.END)
        for proc in processes['wechat']:
            print(f"  PID: {proc['pid']}, Name: {proc['name']}")
            
        print(Color.GREEN + "[+] 检测到以下小程序进程:" + Color.END)
        for proc in processes['miniprogram']:
            version = self.extract_miniprogram_version(proc['cmdline'])
            print(f"  PID: {proc['pid']}, Name: {proc['name']}, Version: {version}")
            
        if not processes['wechat'] and not processes['miniprogram']:
            print(Color.RED + "[-] 未检测到任何微信相关进程" + Color.END)
            
    def get_latest_miniprogram_process(self):
        """
        获取最新版本的小程序进程
        """
        processes = self.detect_wechat_processes()
        if not processes['miniprogram']:
            return None
            
        latest_process = None
        latest_version = 0
        
        for proc in processes['miniprogram']:
            version = self.extract_miniprogram_version(proc['cmdline'])
            if version and version > latest_version:
                latest_version = version
                latest_process = proc
                
        return latest_process, latest_version