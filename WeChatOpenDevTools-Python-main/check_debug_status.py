import os
import json
from pathlib import Path

def check_debug_files():
    """检查调试文件是否存在及内容"""
    target_directory = r"C:\Users\ThinkPad\Documents\xwechat_files"
    
    if not os.path.exists(target_directory):
        print("❌ 调试目录不存在:", target_directory)
        return False
    
    debug_files = [
        "debug_config.json",
        "wechat_debug.json", 
        "devtools_config.json"
    ]
    
    print("🔍 检查调试配置文件:")
    for file_name in debug_files:
        file_path = os.path.join(target_directory, file_name)
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    print(f"✅ {file_name}:")
                    for key, value in content.items():
                        print(f"   {key}: {value}")
            except Exception as e:
                print(f"❌ 读取 {file_name} 失败: {e}")
        else:
            print(f"❌ 文件不存在: {file_name}")
    
    return True

def check_wechat_version():
    """检查微信版本（模拟）"""
    # 在实际应用中，这将需要复杂的检测方法
    print("\n🔍 微信版本检查:")
    print("⚠️  注意：微信4.1.0版本增强了安全机制")
    print("💡 传统的F12调试方式可能已被禁用")
    print("💡 小程序调试需要通过官方开发者工具")

def show_alternative_solutions():
    """显示替代解决方案"""
    print("\n🔧 替代调试方案:")
    print("1. 使用微信官方开发者工具:")
    print("   📍 https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html")
    print("   ✅ 官方支持，功能完整")
    print("   ✅ 可以真机调试")
    print("   ✅ 提供完整的调试功能")
    
    print("\n2. 浏览器调试法:")
    print("   📍 在微信中选择\"在浏览器中打开\"")
    print("   📍 使用浏览器的开发者工具(F12)进行调试")
    print("   ⚠️ 功能受限，仅供参考")
    
    print("\n3. vConsole集成:")
    print("   📍 在小程序代码中引入vConsole")
    print("   📍 代码示例:")
    print("      const vConsole = new VConsole();")
    print("   ⚠️ 需要修改小程序源码")

def main():
    print("=== 微信小程序调试状态检查 ===\n")
    
    check_debug_files()
    check_wechat_version()
    show_alternative_solutions()
    
    print("\n💡 总结:")
    print("   微信4.1.0版本加强了安全限制，传统的调试方法可能无法工作")
    print("   推荐使用官方开发者工具获取最佳调试体验")

if __name__ == "__main__":
    main()