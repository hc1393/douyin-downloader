import frida
import json
import os

# 重新定义颜色类，避免依赖
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

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
            
    def on_message(self, message, data):
        """
        处理来自Frida脚本的消息
        """
        try:
            if message['type'] == 'send':
                payload = message['payload']
                print(Color.GREEN + f"[Frida] {payload}" + Color.END)
            elif message['type'] == 'error':
                print(Color.RED + f"[Frida Error] {message['description']}" + Color.END)
                print(Color.RED + f"  Line: {message['lineNumber']}" + Color.END)
                print(Color.RED + f"  Stack: {message['stack']}" + Color.END)
        except Exception as e:
            print(Color.RED + f"[!] 消息处理出错: {e}" + Color.END)
            
    def attach_to_process(self, pid, script_content):
        """
        附加到指定进程并执行脚本
        """
        try:
            session = self.device.attach(pid)
            script = session.create_script(script_content)
            script.on('message', self.on_message)
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
        processes = self.version_detector.detect_wechat_processes()
        miniprogram_processes = processes['miniprogram']
        
        if not miniprogram_processes:
            print(Color.RED + "[-] 未检测到小程序进程，请确保微信已运行并打开了小程序" + Color.END)
            return False
            
        # 选择一个进程进行调试（选择第一个）
        target_process = miniprogram_processes[0]
        print(Color.GREEN + f"[+] 检测到小程序进程，PID: {target_process['pid']}" + Color.END)
        
        # 尝试加载最新版本的配置
        versions_to_try = [13080813, 11275, 11253, 11205, 11159]  # 按优先级排序
        config = None
        
        for version in versions_to_try:
            config = self.load_config(version)
            if config:
                print(Color.GREEN + f"[+] 使用配置文件版本: {config['Version']}" + Color.END)
                break
                
        if not config:
            print(Color.RED + "[-] 未找到任何可用的配置文件" + Color.END)
            return False
        
        # 生成Hook脚本
        script_content = self.generate_hook_script(config)
        if not script_content:
            return False
            
        # 附加到进程
        session, script = self.attach_to_process(target_process['pid'], script_content)
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