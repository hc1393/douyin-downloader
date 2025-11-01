// 微信小程序mtgsig监控脚本
console.log('🔍 微信小程序mtgsig监控脚本已启动');

// 保存原始函数
const originalConsoleLog = console.log;
const originalConsoleError = console.error;
const originalConsoleWarn = console.warn;

// 重写console.log以捕获可能包含mtgsig的日志
console.log = function(...args) {
    args.forEach((arg, index) => {
        try {
            const str = typeof arg === 'object' ? JSON.stringify(arg) : String(arg);
            if (str.includes('mtgsig')) {
                console.warn('🎯 在console.log中检测到mtgsig:', arg);
                console.trace('调用栈:');
            }
            
            // 检查是否包含mtgsig的关键字段
            if (str.includes('a1') && str.includes('a2') && str.includes('a3') && str.includes('a4')) {
                console.warn('🔍 在console.log中检测到可能的mtgsig结构:', arg);
                console.trace('调用栈:');
            }
        } catch (e) {
            // 忽略序列化错误
        }
    });
    
    return originalConsoleLog.apply(this, args);
};

// 重写console.error
console.error = function(...args) {
    args.forEach((arg, index) => {
        try {
            const str = typeof arg === 'object' ? JSON.stringify(arg) : String(arg);
            if (str.includes('mtgsig')) {
                console.warn('🎯 在console.error中检测到mtgsig:', arg);
                console.trace('调用栈:');
            }
        } catch (e) {
            // 忽略序列化错误
        }
    });
    
    return originalConsoleError.apply(this, args);
};

// 重写console.warn
console.warn = function(...args) {
    args.forEach((arg, index) => {
        try {
            const str = typeof arg === 'object' ? JSON.stringify(arg) : String(arg);
            if (str.includes('mtgsig')) {
                console.warn('🎯 在console.warn中检测到mtgsig:', arg);
                console.trace('调用栈:');
            }
        } catch (e) {
            // 忽略序列化错误
        }
    });
    
    return originalConsoleWarn.apply(this, args);
};

// 监控微信小程序的request API
if (typeof wx !== 'undefined' && wx.request) {
    const originalRequest = wx.request;
    wx.request = function(options) {
        // 检查请求参数中是否包含mtgsig
        try {
            const optionsStr = JSON.stringify(options);
            if (optionsStr.includes('mtgsig')) {
                console.warn('📡 在wx.request参数中检测到mtgsig:', options);
                console.trace('调用栈:');
            }
        } catch (e) {
            // 忽略序列化错误
        }
        
        // 监控响应
        const originalSuccess = options.success;
        options.success = function(res) {
            try {
                const resStr = JSON.stringify(res);
                if (resStr.includes('mtgsig')) {
                    console.warn('📥 在wx.request响应中检测到mtgsig:', res);
                    console.trace('调用栈:');
                }
            } catch (e) {
                // 忽略序列化错误
            }
            
            if (originalSuccess) {
                originalSuccess(res);
            }
        };
        
        const originalFail = options.fail;
        options.fail = function(err) {
            try {
                const errStr = JSON.stringify(err);
                if (errStr.includes('mtgsig')) {
                    console.warn('📥 在wx.request错误中检测到mtgsig:', err);
                    console.trace('调用栈:');
                }
            } catch (e) {
                // 忽略序列化错误
            }
            
            if (originalFail) {
                originalFail(err);
            }
        };
        
        return originalRequest.call(this, options);
    };
}

// 监控本地存储
if (typeof wx !== 'undefined') {
    if (wx.setStorage) {
        const originalSetStorage = wx.setStorage;
        wx.setStorage = function(options) {
            try {
                const dataStr = typeof options.data === 'object' ? JSON.stringify(options.data) : String(options.data);
                if (dataStr.includes('mtgsig')) {
                    console.warn('💾 在wx.setStorage中检测到mtgsig:', options);
                    console.trace('调用栈:');
                }
            } catch (e) {
                // 忽略序列化错误
            }
            return originalSetStorage.call(this, options);
        };
    }
    
    if (wx.setStorageSync) {
        const originalSetStorageSync = wx.setStorageSync;
        wx.setStorageSync = function(key, data) {
            try {
                const dataStr = typeof data === 'object' ? JSON.stringify(data) : String(data);
                if (dataStr.includes('mtgsig')) {
                    console.warn('💾 在wx.setStorageSync中检测到mtgsig:', {key, data});
                    console.trace('调用栈:');
                }
            } catch (e) {
                // 忽略序列化错误
            }
            return originalSetStorageSync.call(this, key, data);
        };
    }
    
    if (wx.getStorage) {
        const originalGetStorage = wx.getStorage;
        wx.getStorage = function(options) {
            try {
                const keyStr = String(options.key);
                if (keyStr.includes('mtgsig')) {
                    console.warn('💾 在wx.getStorage key中检测到mtgsig:', options);
                    console.trace('调用栈:');
                }
            } catch (e) {
                // 忽略错误
            }
            
            const originalSuccess = options.success;
            options.success = function(res) {
                try {
                    const resStr = typeof res.data === 'object' ? JSON.stringify(res.data) : String(res.data);
                    if (resStr.includes('mtgsig')) {
                        console.warn('💾 在wx.getStorage响应中检测到mtgsig:', res);
                        console.trace('调用栈:');
                    }
                } catch (e) {
                    // 忽略序列化错误
                }
                
                if (originalSuccess) {
                    originalSuccess(res);
                }
            };
            
            return originalGetStorage.call(this, options);
        };
    }
}

// 监控JSON相关操作
if (typeof JSON !== 'undefined') {
    const originalStringify = JSON.stringify;
    JSON.stringify = function(...args) {
        const result = originalStringify.apply(this, args);
        
        try {
            if (result && result.includes('mtgsig')) {
                console.warn('🧾 在JSON.stringify结果中检测到mtgsig:', args[0]);
                console.trace('调用栈:');
            }
        } catch (e) {
            // 忽略错误
        }
        
        return result;
    };

    const originalParse = JSON.parse;
    JSON.parse = function(...args) {
        const result = originalParse.apply(this, args);
        
        try {
            const resultStr = typeof result === 'object' ? JSON.stringify(result) : String(result);
            if (resultStr.includes('mtgsig')) {
                console.warn('🧾 在JSON.parse结果中检测到mtgsig:', args[0]);
                console.trace('调用栈:');
            }
        } catch (e) {
            // 忽略序列化错误
        }
        
        return result;
    };
}

// 监控字符串相关操作
if (typeof String !== 'undefined') {
    const originalToString = String.prototype.toString;
    String.prototype.toString = function() {
        const result = originalToString.apply(this, arguments);
        if (result.includes('mtgsig')) {
            console.warn('🔤 在String.toString中检测到mtgsig:', result);
            console.trace('调用栈:');
        }
        return result;
    };
}

console.log('✅ 微信小程序mtgsig监控脚本已就绪');