import frida
import json
import os
from utils.colors import Color
from new_version_support.version_detector import VersionDetector

class DebugTool:
    """
    微信小程序调试工具
    """
    
    def __init__(self):
        self.device = frida.get_local_device()
        self.version_detector = VersionDetector()
        self.configs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs')
        
    def load_config(self, version):
        """
        加载指定版本的配置文件
        """
        config_file = os.path.join(self.configs_path, f'address_{version}_x64.json')
        if not os.path.exists(config_file):
            print(Color.RED + f"[-] 未找到版本 {version} 的配置文件" + Color.END)
            return None
            
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(Color.RED + f"[-] 加载配置文件失败: {e}" + Color.END)
            return None
            
    def generate_hook_script(self, config):
        """
        生成Hook脚本
        """
        try:
            script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scripts', 'hook.js')
            with open(script_path, 'r', encoding='utf-8') as f:
                script_content = f.read()
                
            # 将配置转换为JSON字符串并插入到脚本中
            config_json = json.dumps(config)
            script_content = f"var address = {config_json};\n" + script_content
            
            return script_content
        except Exception as e:
            print(Color.RED + f"[-] 生成Hook脚本失败: {e}" + Color.END)
            return None
            
    def attach_to_process(self, pid, script_content):
        """
        附加到指定进程并执行脚本
        """
        try:
            session = self.device.attach(pid)
            script = session.create_script(script_content)
            script.load()
            print(Color.GREEN + f"[+] 成功附加到进程 {pid}" + Color.END)
            return session, script
        except Exception as e:
            print(Color.RED + f"[-] 附加到进程失败: {e}" + Color.END)
            return None, None
            
    def start_debug(self):
        """
        启动调试
        """
        print(Color.GREEN + "[*] 正在检测微信小程序进程..." + Color.END)
        
        # 检测小程序进程
        process_info, version = self.version_detector.get_latest_miniprogram_process()
        if not process_info:
            print(Color.RED + "[-] 未检测到小程序进程，请确保微信已运行并打开了小程序" + Color.END)
            return False
            
        print(Color.GREEN + f"[+] 检测到小程序进程，PID: {process_info['pid']}, 版本: {version}" + Color.END)
        
        # 加载配置
        config = self.load_config(version)
        if not config:
            # 尝试使用最新版本的配置
            config = self.load_config(13080813)  # 微信4.1.0假设版本
            if not config:
                print(Color.RED + "[-] 未找到匹配的配置文件，请确认版本支持" + Color.END)
                return False
                
        print(Color.GREEN + f"[+] 使用配置文件版本: {config['Version']}" + Color.END)
        
        # 生成Hook脚本
        script_content = self.generate_hook_script(config)
        if not script_content:
            return False
            
        # 附加到进程
        session, script = self.attach_to_process(process_info['pid'], script_content)
        if not session:
            return False
            
        print(Color.GREEN + "[+] 小程序F12调试功能已启用" + Color.END)
        print(Color.YELLOW + "[*] 按 Ctrl+C 停止调试" + Color.END)
        
        try:
            # 保持脚本运行
            input()
        except KeyboardInterrupt:
            print(Color.YELLOW + "\n[!] 调试已停止" + Color.END)
            
        return True