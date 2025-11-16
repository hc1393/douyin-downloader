;
//获取WeChatAppEx.exe的基址
var module = Process.findModuleByName("WeChatAppEx.exe") || Process.findModuleByName('WeChatAppEx Framework')
var base = module.base;
// console.log("模块名称:",module.name);
// console.log("模块地址:",module.base);
// console.log("大小:",module.size);


Object.keys(address).forEach(key => {
    key != "Version" ? address[key] = base.add(address[key]) : false
});

send("[+] WeChatAppEx 注入成功!");
send("[+] 当前小程序版本: " + address.Version);
send("[+] 等待小程序加载...");

function readStdString(s) {
    var flag = s.add(23).readU8()
    if (flag == 0x80) {
        // 从堆中读取
        var size = s.add(8).readUInt()
        return s.readPointer().readUtf8String(size)
    } else {
        // 从栈中读取
        return s.readUtf8String(flag)
    }
}
function writeStdString(s, content) {
    var flag = s.add(23).readU8()
    if (flag == 0x80) {
        // 从堆中写入
        var orisize = s.add(8).readUInt()
        if (content.length > orisize) {
            throw "must below orisize!"
        }
        s.readPointer().writeUtf8String(content)
        s.add(8).writeUInt(content.length)
    } else {
        // 从栈中写入
        if (content.length > 22) {
            throw "max 23 for stack str"
        }
        s.writeUtf8String(content)
        s.add(23).writeU8(content.length)
    }
}
function sendMessage(msg) {
    msg === null || undefined ? send(msg) : send("[+] 已还原完整F12")
    // send("[+] 已还原完整F12")
}


function replaceParams() {
    try {
        Interceptor.attach(address.LaunchAppletBegin, {
            onEnter(args) {
                send("[+] HOOK到小程序加载! " + readStdString(args[1]))
                for (var i = 0; i < 0x1000; i += 8) {
                    try {
                        var s = readStdString(args[2].add(i))
                        var s1 = s.replaceAll('"enable_vconsole":false', '"enable_vconsole": true')
                        // .replaceAll("md5", "md6")
                        // .replaceAll('"frameset":false', '"frameset": true')
                        //"frameset":false
                        if (s !== s1) {
                            writeStdString(args[2].add(i), s1)
                        }
                    } catch (a) {
                    }
                }
            }
        })
    } catch (e) {
        console.log("replaceParams error: " + e);
    }
}

// 过新版8555检测
if (address.MenuItemDevToolsString) {
    try {
        var menuItemDevToolsStringCr = new Uint8Array(address.MenuItemDevToolsString.readByteArray(7));
        var intptr_ = (menuItemDevToolsStringCr[3] & 0xFF) | ((menuItemDevToolsStringCr[4] & 0xFF) << 8) | ((menuItemDevToolsStringCr[5] & 0xFF) << 16) | ((menuItemDevToolsStringCr[6] & 0xFF) << 24);
        var menuItemDevToolsStringPtrData = address.MenuItemDevToolsString.add(intptr_ + 7);
        Memory.protect(menuItemDevToolsStringPtrData, 8, 'rw-')
        menuItemDevToolsStringPtrData.writeUtf8String("DevTools");
    } catch (e) {
        // 忽略内存访问错误
        console.log("内存访问错误已忽略: " + e);
    }
    replaceParams()
    setupInterceptor()
}


function setupInterceptor() {

    /**
     * 
     */

    switch (address.Version) {

        case 8555:
            try {
                Interceptor.attach(address.WechatAppHtml, {
                    onEnter(args) {
                        this.context.rdx = address.WechatWebHtml;
                        sendMessage()
                    }
                });
            } catch (e) {
                console.log("Interceptor error for version 8555: " + e);
            }

            break;


        case 9105:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 9105: " + e);
            }
            break;

        case 9079:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 9079: " + e);
            }
            break;

        case 9115:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 9115: " + e);
            }
            break;

        case 9129:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 9129: " + e);
            }
            break;
        case 11159:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 11159: " + e);
            }
            break;          

        case 13080811:
            try {
                Interceptor.attach(address.WechatAppHtml, {
                    onEnter(args) {
                        this.context.rsi = address.WechatWebHtml
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 13080811: " + e);
            }
            break;
            
        case 13080812:
            try {
                Interceptor.attach(address.WechatAppHtml, {
                    onEnter(args) {
                        this.context.rsi = address.WechatWebHtml
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 13080812: " + e);
            }
            break;
            
        case 9193:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 9193: " + e);
            }
            break;
        case 11205:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 11205: " + e);
            }
            break;
        case 11275:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 11275: " + e);
            }
            break;
        case 11253:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 11253: " + e);
            }
            break;
        // 支持微信4.1.0版本
        case 13080813:
            try {
                Interceptor.attach(address.SwitchVersion, {
                    onEnter(args) {
                        this.context.r8 = this.context.rax
                        sendMessage()
                    }
                })
            } catch (e) {
                console.log("Interceptor error for version 13080813: " + e);
            }
            break;
        default:
            console.log("Unknown version: " + address.Version);
            try {
                Interceptor.attach(address.WechatAppHtml, {
                    onEnter(args) {
                        this.context.rdx = address.WechatWebHtml;
                        sendMessage()
                    }
                });
            } catch (e) {
                console.log("Default interceptor error: " + e);
            }
            break;
    }
}
