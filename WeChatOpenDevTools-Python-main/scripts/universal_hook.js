// 通用Hook脚本，适用于不同版本的微信
var isWeChatAppEx = Process.findModuleByName("WeChatAppEx.exe") || Process.findModuleByName("WeChatAppEx Framework");

if (isWeChatAppEx) {
    console.log("[+] 检测到微信小程序进程");
    
    // 尝试多种方式启用调试
    try {
        // 方式1: 通过修改内存中的字符串
        var modules = Process.enumerateModules();
        for (var i = 0; i < modules.length; i++) {
            var module = modules[i];
            if (module.name.indexOf("WeChatAppEx") !== -1) {
                console.log("[+] 扫描模块: " + module.name);
                
                // 在模块内存中搜索相关字符串
                var ranges = module.enumerateRanges('r--');
                for (var j = 0; j < ranges.length; j++) {
                    var range = ranges[j];
                    try {
                        // 查找 "enable_vconsole" 字符串
                        var scanResults = Memory.scanSync(range.base, range.size, "65 6e 61 62 6c 65 5f 76 63 6f 6e 73 6f 6c 65");
                        if (scanResults.length > 0) {
                            console.log("[+] 找到 enable_vconsole 字符串位置: " + scanResults[0].address);
                            // 尝试修改附近的值
                            var falseAddr = scanResults[0].address.add(17); // "false" 通常在字符串后
                            // 检查是否为false
                            var falseBytes = falseAddr.readUtf8String(5);
                            if (falseBytes === "false") {
                                console.log("[+] 修改 enable_vconsole 为 true");
                                falseAddr.writeUtf8String("true ");
                            }
                        }
                        
                        // 查找 "frameset" 字符串
                        var framesetResults = Memory.scanSync(range.base, range.size, "66 72 61 6d 65 73 65 74");
                        if (framesetResults.length > 0) {
                            console.log("[+] 找到 frameset 字符串位置: " + framesetResults[0].address);
                            var falseAddr = framesetResults[0].address.add(10);
                            var falseBytes = falseAddr.readUtf8String(5);
                            if (falseBytes === "false") {
                                console.log("[+] 修改 frameset 为 true");
                                falseAddr.writeUtf8String("true ");
                            }
                        }
                    } catch (e) {
                        // 忽略扫描错误
                    }
                }
            }
        }
        
        console.log("[+] 通用Hook执行完成");
    } catch (e) {
        console.log("[-] 通用Hook执行出错: " + e.toString());
    }
} else {
    console.log("[-] 未检测到微信小程序进程");
}

// 尝试Hook一些通用的函数来启用调试
try {
    var baseAddr = (Process.findModuleByName("WeChatAppEx.exe") || Process.findModuleByName("WeChatAppEx Framework")).base;
    
    // 尝试拦截一些可能与调试相关的函数
    var functionsToHook = [
        // 这些是可能的函数地址，需要根据实际版本调整
    ];
    
    console.log("[*] 尝试通用调试启用方法...");
    
    // 发送消息表示脚本已加载
    send({
        type: "debug",
        message: "通用Hook脚本已加载，尝试启用调试功能"
    });
    
} catch (e) {
    send({
        type: "error",
        message: "加载通用Hook脚本时出错: " + e.toString()
    });
}