// 微信4.1.0版本综合hook脚本
var module = Process.findModuleByName("WeChatAppEx.exe") || Process.findModuleByName('WeChatAppEx Framework');
if (!module) {
    send("[-] 未找到WeChatAppEx模块");
} else {
    var base = module.base;
    send("[+] WeChatAppEx模块基址: " + base);

    // 为所有地址添加基址
    Object.keys(address).forEach(key => {
        if (key !== "Version" && address[key]) {
            try {
                address[key] = base.add(address[key]);
            } catch (e) {
                send("[-] 地址转换失败 " + key + ": " + e);
            }
        }
    });
}

send("[+] WeChatAppEx 注入成功!");
send("[+] 当前小程序版本: " + address.Version);

// 安全读取StdString
function readStdString(s) {
    try {
        var flag = s.add(23).readU8();
        if (flag === 0x80) {
            // 从堆中读取
            var size = s.add(8).readUInt();
            return s.readPointer().readUtf8String(size);
        } else {
            // 从栈中读取
            return s.readUtf8String(flag);
        }
    } catch (e) {
        return "";
    }
}

// 安全写入StdString
function writeStdString(s, content) {
    try {
        var flag = s.add(23).readU8();
        if (flag === 0x80) {
            // 从堆中写入
            var orisize = s.add(8).readUInt();
            if (content.length > orisize) {
                return false;
            }
            s.readPointer().writeUtf8String(content);
            s.add(8).writeUInt(content.length);
        } else {
            // 从栈中写入
            if (content.length > 22) {
                return false;
            }
            s.writeUtf8String(content);
            s.add(23).writeU8(content.length);
        }
        return true;
    } catch (e) {
        return false;
    }
}

// 发送消息的封装
function sendMessage(msg) {
    try {
        if (msg === null || msg === undefined) {
            send("[+] 调试功能已启用");
        } else {
            send(msg);
        }
    } catch (e) {
        // 忽略发送消息时的错误
    }
}

// 替换参数以启用调试功能 - 方法1: 拦截小程序启动
function hookLaunchApplet() {
    if (!address.LaunchAppletBegin) {
        send("[-] LaunchAppletBegin地址未定义");
        return;
    }

    try {
        Interceptor.attach(address.LaunchAppletBegin, {
            onEnter: function(args) {
                try {
                    var appName = readStdString(args[1]);
                    send("[+] HOOK到小程序启动: " + appName);
                    
                    // 遍历参数查找并替换调试相关配置
                    for (var i = 0; i < 0x1000; i += 8) {
                        try {
                            var s = readStdString(args[2].add(i));
                            if (s && s.length > 0) {
                                // 启用各种调试选项
                                var modified = false;
                                var replacements = [
                                    ['"debug":false', '"debug":true'],
                                    ['"debug": false', '"debug": true'],
                                    ['"enable_vconsole":false', '"enable_vconsole":true'],
                                    ['"enable_vconsole": false', '"enable_vconsole": true'],
                                    ['"devtools":false', '"devtools":true'],
                                    ['"devtools": false', '"devtools": true'],
                                    ['"inspect":false', '"inspect":true'],
                                    ['"inspect": false', '"inspect": true'],
                                    ['"show_devtools":false', '"show_devtools":true'],
                                    ['"show_devtools": false', '"show_devtools": true'],
                                    ['"developer_mode":false', '"developer_mode":true'],
                                    ['"developer_mode": false', '"developer_mode": true'],
                                    ['"remote_debugging":false', '"remote_debugging":true'],
                                    ['"remote_debugging": false', '"remote_debugging": true']
                                ];
                                
                                var s1 = s;
                                for (var j = 0; j < replacements.length; j++) {
                                    s1 = s1.replace(new RegExp(replacements[j][0], 'g'), replacements[j][1]);
                                }
                                
                                if (s !== s1) {
                                    if (writeStdString(args[2].add(i), s1)) {
                                        modified = true;
                                    }
                                }
                                
                                if (modified) {
                                    send("[+] 已修改小程序启动参数");
                                }
                            }
                        } catch (e) {
                            // 忽略单个参数处理错误
                        }
                    }
                } catch (e) {
                    send("[-] 小程序启动HOOK错误: " + e);
                }
            }
        });
        send("[+] 成功HOOK小程序启动函数");
    } catch (e) {
        send("[-] HOOK小程序启动函数失败: " + e);
    }
}

// 替换参数以启用调试功能 - 方法2: 内存扫描修改
function scanAndModifyMemory() {
    send("[*] 开始扫描内存中的调试配置...");
    
    try {
        // 扫描内存中的配置字符串
        var ranges = Process.enumerateRanges({protection: 'r--'});
        var foundCount = 0;
        
        ranges.forEach(function (range) {
            try {
                var rangeSize = range.size;
                if (rangeSize > 0x100000) { // 跳过过大的区域
                    return;
                }
                
                var data = range.base.readByteArray(rangeSize);
                if (data) {
                    var dataView = new DataView(data);
                    var buffer = new Uint8Array(data);
                    
                    // 查找调试相关的配置字符串
                    var patterns = [
                        '"debug":false',
                        '"enable_vconsole":false',
                        '"devtools":false',
                        '"inspect":false'
                    ];
                    
                    patterns.forEach(function(pattern) {
                        var patternBytes = [];
                        for (var i = 0; i < pattern.length; i++) {
                            patternBytes.push(pattern.charCodeAt(i));
                        }
                        
                        // 简单的字符串匹配
                        for (var i = 0; i <= buffer.length - patternBytes.length; i++) {
                            var match = true;
                            for (var j = 0; j < patternBytes.length; j++) {
                                if (buffer[i + j] !== patternBytes[j]) {
                                    match = false;
                                    break;
                                }
                            }
                            
                            if (match) {
                                try {
                                    var replacement = pattern.replace('false', 'true');
                                    range.base.add(i).writeUtf8String(replacement);
                                    foundCount++;
                                    send("[+] 在内存中修改配置: " + pattern + " -> " + replacement);
                                } catch (e) {
                                    // 内存写入可能失败，忽略错误
                                }
                            }
                        }
                    });
                }
            } catch (e) {
                // 忽略单个内存区域扫描错误
            }
        });
        
        send("[+] 内存扫描完成，共修改 " + foundCount + " 处配置");
    } catch (e) {
        send("[-] 内存扫描失败: " + e);
    }
}

// 替换参数以启用调试功能 - 方法3: 定时扫描修改
function setupPeriodicScan() {
    send("[*] 设置周期性配置扫描...");
    
    // 每5秒扫描一次内存配置
    setInterval(function() {
        try {
            scanAndModifyMemory();
        } catch (e) {
            // 忽略定时任务错误
        }
    }, 5000);
}

// 主处理流程
function main() {
    send("[*] 开始执行微信4.1.0综合调试注入...");
    
    // 方法1: HOOK小程序启动
    hookLaunchApplet();
    
    // 方法2: 立即扫描内存
    scanAndModifyMemory();
    
    // 方法3: 设置周期性扫描
    setupPeriodicScan();
    
    send("[+] 微信4.1.0综合调试注入完成");
}

// 执行主函数
try {
    main();
} catch (e) {
    send("[-] 注入过程发生错误: " + e);
}