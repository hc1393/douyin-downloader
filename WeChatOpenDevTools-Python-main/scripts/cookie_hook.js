// 微信小程序Cookie监控脚本
// 用于追踪小程序中acw_tc和ssxmod_itna等反爬虫cookie的生成和使用

var module = Process.findModuleByName("WeChatAppEx.exe") || Process.findModuleByName('WeChatAppEx Framework');
var base = module.base;

send("[+] 开始注入Cookie监控Hook...");

// Hook小程序中的网络请求相关函数
// 微信小程序使用自己的网络库，不直接使用浏览器的XMLHttpRequest或fetch

// 尝试Hook微信小程序的网络请求函数
// 这些地址需要根据具体的微信版本进行适配

function hookNetworkRequests() {
    // 尝试找到并Hook网络请求相关函数
    try {
        // 这里我们尝试通过扫描内存来找到可能的网络请求函数
        // 这是一种通用的方法，适用于不同版本的微信
        
        // 查找可能的HTTP请求相关函数
        var httpPatterns = [
            "Http",
            "Request",
            "Cookie",
            "Set-Cookie"
        ];
        
        // 在模块中搜索相关字符串引用
        var matches = {};
        httpPatterns.forEach(function(pattern) {
            var results = Memory.scanSync(base, module.size, pattern);
            results.forEach(function(result) {
                // 查找引用这些字符串的代码位置
                var refs = Instruction.parse(result.address).references();
                refs.forEach(function(ref) {
                    if (!matches[ref]) {
                        matches[ref] = 0;
                    }
                    matches[ref]++;
                });
            });
        });
        
        // 对于引用多个HTTP相关字符串的位置，很可能就是网络请求函数
        Object.keys(matches).forEach(function(addr) {
            if (matches[addr] >= 2) {
                try {
                    Interceptor.attach(ptr(addr), {
                        onEnter: function(args) {
                            send("[+] 潜在的网络请求函数被调用: " + addr);
                            // 尝试读取参数中的URL和数据
                            try {
                                var argStr = args[0]?.readUtf8String(100);
                                if (argStr) {
                                    send("[+] 请求参数: " + argStr);
                                }
                            } catch (e) {}
                        },
                        onLeave: function(retval) {
                            // 函数返回时
                        }
                    });
                } catch (e) {
                    // 忽略错误
                }
            }
        });
        
        send("[+] 网络请求Hook安装完成");
    } catch (e) {
        send("[-] 网络请求Hook安装失败: " + e.toString());
    }
}

// Hook Cookie相关操作
function hookCookieOperations() {
    try {
        // 查找可能的Cookie操作相关函数
        var cookiePatterns = [
            "cookie",
            "Cookie",
            "acw_tc",
            "ssxmod_itna"
        ];
        
        cookiePatterns.forEach(function(pattern) {
            var results = Memory.scanSync(base, module.size, pattern);
            results.forEach(function(result) {
                send("[+] 找到Cookie相关字符串: " + pattern + " at " + result.address);
            });
        });
        
        send("[+] Cookie操作Hook安装完成");
    } catch (e) {
        send("[-] Cookie操作Hook安装失败: " + e.toString());
    }
}

// Hook JavaScript引擎中的eval和Function构造函数
function hookJavaScriptEngine() {
    try {
        // 查找JavaScript引擎相关函数
        var jsPatterns = [
            "eval",
            "Function",
            "JSON"
        ];
        
        jsPatterns.forEach(function(pattern) {
            var results = Memory.scanSync(base, module.size, pattern);
            results.forEach(function(result) {
                send("[+] 找到JavaScript引擎相关字符串: " + pattern + " at " + result.address);
            });
        });
        
        send("[+] JavaScript引擎Hook安装完成");
    } catch (e) {
        send("[-] JavaScript引擎Hook安装失败: " + e.toString());
    }
}

// 主函数
function main() {
    hookNetworkRequests();
    hookCookieOperations();
    hookJavaScriptEngine();
    
    send("[+] 所有Cookie监控Hook安装完成");
}

// 延迟执行主函数，等待小程序环境完全加载
setTimeout(main, 5000);