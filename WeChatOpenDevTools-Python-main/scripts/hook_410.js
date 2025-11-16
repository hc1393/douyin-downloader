// 微信4.1.0版本专用hook脚本
var module = Process.findModuleByName("WeChatAppEx.exe") || Process.findModuleByName('WeChatAppEx Framework');
if (!module) {
    send("[-] 未找到WeChatAppEx模块");
} else {
    var base = module.base;
    send("[+] WeChatAppEx模块基址: " + base);

    // 为所有地址添加基址
    Object.keys(address).forEach(key => {
        if (key !== "Version") {
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
send("[+] 等待小程序加载...");

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

// 替换参数以启用调试功能
function replaceParams() {
    if (!address.LaunchAppletBegin) {
        send("[-] LaunchAppletBegin地址未定义");
        return;
    }

    try {
        Interceptor.attach(address.LaunchAppletBegin, {
            onEnter: function(args) {
                try {
                    var appName = readStdString(args[1]);
                    send("[+] HOOK到小程序加载: " + appName);
                    
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
                                    ['"developer_mode": false', '"developer_mode": true']
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
                                    send("[+] 已修改小程序配置参数");
                                }
                            }
                        } catch (e) {
                            // 忽略单个参数处理错误
                        }
                    }
                } catch (e) {
                    send("[-] 小程序加载HOOK错误: " + e);
                }
            }
        });
        send("[+] 成功HOOK小程序加载函数");
    } catch (e) {
        send("[-] HOOK小程序加载函数失败: " + e);
    }
}

// 设置拦截器
function setupInterceptor() {
    send("[*] 正在设置版本特定拦截器...");
    
    // 根据版本设置不同的拦截器
    switch (address.Version) {
        case 13080813: // 微信4.1.0
            try {
                // 不再尝试HOOK可能已变更的地址，而是采用更安全的方式
                send("[+] 微信4.1.0版本已启用调试参数修改");
            } catch (e) {
                send("[-] 微信4.1.0处理失败: " + e);
            }
            break;
            
        default:
            send("[-] 未找到适用于版本 " + address.Version + " 的特定处理");
    }
}

// 主处理流程
function main() {
    send("[*] 开始执行微信4.1.0调试注入...");
    
    // 替换参数以启用调试
    replaceParams();
    
    // 设置版本特定的拦截器
    setupInterceptor();
    
    send("[+] 微信4.1.0调试注入完成");
}

// 执行主函数
try {
    main();
} catch (e) {
    send("[-] 注入过程发生错误: " + e);
}