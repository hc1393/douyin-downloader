// ==UserScript==
// @name         mtgsig Capture Hook for WeChat Mini Program
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  专门捕获微信小程序中mtgsig参数的hook脚本
// @author       You
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // 检查是否在微信小程序环境
    const isWeChatMiniProgram = (typeof wx !== 'undefined') && (typeof window === 'undefined' || !window.document);
    
    // 检查是否在浏览器环境
    const isBrowser = typeof window !== 'undefined' && typeof window.document !== 'undefined';
    
    if (!isWeChatMiniProgram && !isBrowser) {
        console.log('🔍 当前环境不是浏览器或微信小程序环境，跳过mtgsig捕获脚本');
        return;
    }
    
    if (isWeChatMiniProgram) {
        console.log('🔍 mtgsig捕获脚本已启动 (微信小程序环境)');
    } else {
        console.log('🔍 mtgsig捕获脚本已启动 (浏览器环境)');
    }

    // 添加一个通用的监控函数，用于检查对象中是否包含mtgsig
    function checkForMtgsig(obj, source) {
        try {
            const str = typeof obj === 'object' ? JSON.stringify(obj) : String(obj);
            if (str.includes('mtgsig')) {
                console.log(`🎯 在${source}中检测到mtgsig:`, str);
                if (typeof console.trace === 'function') {
                    console.trace('调用栈:');
                }
                return true;
            }
            
            // 检查是否包含mtgsig的关键字段
            if (str.includes('a1') && str.includes('a2') && str.includes('a3')) {
                console.log(`🔍 在${source}中检测到可能的mtgsig结构:`, str);
                if (typeof console.trace === 'function') {
                    console.trace('调用栈:');
                }
                return true;
            }
        } catch (e) {
            // 忽略序列化错误
        }
        return false;
    }

    // 微信小程序环境的特殊处理
    if (isWeChatMiniProgram) {
        // 监控微信小程序的request API
        if (wx.request) {
            const originalRequest = wx.request;
            wx.request = function(options) {
                // 检查请求参数中是否包含mtgsig
                checkForMtgsig(options, 'wx.request options');
                if (options.header) {
                    checkForMtgsig(options.header, 'wx.request header');
                }
                if (options.data) {
                    checkForMtgsig(options.data, 'wx.request data');
                }
                
                // 监控响应
                const originalSuccess = options.success;
                options.success = function(res) {
                    checkForMtgsig(res, 'wx.request response');
                    if (res.data) {
                        checkForMtgsig(res.data, 'wx.request response data');
                    }
                    if (res.header) {
                        checkForMtgsig(res.header, 'wx.request response header');
                    }
                    if (originalSuccess) {
                        originalSuccess(res);
                    }
                };
                
                const originalFail = options.fail;
                options.fail = function(err) {
                    checkForMtgsig(err, 'wx.request error');
                    if (originalFail) {
                        originalFail(err);
                    }
                };
                
                return originalRequest.call(this, options);
            };
        }
        
        // 监控本地存储
        if (wx.setStorage) {
            const originalSetStorage = wx.setStorage;
            wx.setStorage = function(options) {
                checkForMtgsig(options, 'wx.setStorage options');
                if (options.key) {
                    checkForMtgsig(options.key, 'wx.setStorage key');
                }
                if (options.data) {
                    checkForMtgsig(options.data, 'wx.setStorage data');
                }
                return originalSetStorage.call(this, options);
            };
        }
        
        if (wx.setStorageSync) {
            const originalSetStorageSync = wx.setStorageSync;
            wx.setStorageSync = function(key, data) {
                checkForMtgsig(key, 'wx.setStorageSync key');
                checkForMtgsig(data, 'wx.setStorageSync data');
                return originalSetStorageSync.call(this, key, data);
            };
        }
        
        if (wx.getStorage) {
            const originalGetStorage = wx.getStorage;
            wx.getStorage = function(options) {
                checkForMtgsig(options, 'wx.getStorage options');
                if (options.key) {
                    checkForMtgsig(options.key, 'wx.getStorage key');
                }
                
                const originalSuccess = options.success;
                options.success = function(res) {
                    checkForMtgsig(res, 'wx.getStorage response');
                    if (res.data) {
                        checkForMtgsig(res.data, 'wx.getStorage response data');
                    }
                    if (originalSuccess) {
                        originalSuccess(res);
                    }
                };
                
                return originalGetStorage.call(this, options);
            };
        }
        
        if (wx.getStorageSync) {
            const originalGetStorageSync = wx.getStorageSync;
            wx.getStorageSync = function(key) {
                checkForMtgsig(key, 'wx.getStorageSync key');
                const result = originalGetStorageSync.call(this, key);
                checkForMtgsig(result, 'wx.getStorageSync result');
                return result;
            };
        }
    }
    
    // 浏览器环境的处理
    if (isBrowser) {
        // 重写XMLHttpRequest以捕获请求中的mtgsig
        if (window.XMLHttpRequest) {
            const originalXHR = window.XMLHttpRequest;
            const originalOpen = originalXHR.prototype.open;
            const originalSend = originalXHR.prototype.send;
            const originalSetRequestHeader = originalXHR.prototype.setRequestHeader;

            originalXHR.prototype.open = function(method, url) {
                this._method = method;
                this._url = url;
                // 检查URL中是否包含mtgsig
                checkForMtgsig(url, 'XMLHttpRequest URL');
                return originalOpen.apply(this, arguments);
            };

            originalXHR.prototype.setRequestHeader = function(header, value) {
                // 检查请求头中是否包含mtgsig
                checkForMtgsig(header, 'XMLHttpRequest header name');
                checkForMtgsig(value, 'XMLHttpRequest header value');
                return originalSetRequestHeader.apply(this, arguments);
            };

            originalXHR.prototype.send = function(body) {
                // 检查请求体中是否包含mtgsig
                if (body) {
                    checkForMtgsig(body, 'XMLHttpRequest body');
                }

                // 监听响应
                const xhr = this;
                const originalOnReadyStateChange = xhr.onreadystatechange;
                xhr.onreadystatechange = function() {
                    if (xhr.readyState === 4) {
                        try {
                            // 检查响应中是否包含mtgsig
                            checkForMtgsig(xhr.responseText, 'XMLHttpRequest responseText');
                            checkForMtgsig(xhr.response, 'XMLHttpRequest response');
                        } catch (e) {
                            // 忽略错误
                        }
                    }

                    if (originalOnReadyStateChange) {
                        originalOnReadyStateChange.apply(this, arguments);
                    }
                };

                return originalSend.apply(this, arguments);
            };
        }

        // 重写fetch API以捕获请求中的mtgsig
        if (window.fetch) {
            const originalFetch = window.fetch;
            window.fetch = function(input, init) {
                // 检查URL和请求体中是否包含mtgsig
                checkForMtgsig(input, 'fetch URL');
                if (init) {
                    checkForMtgsig(init, 'fetch init');
                    if (init.headers) {
                        checkForMtgsig(init.headers, 'fetch headers');
                    }
                    if (init.body) {
                        checkForMtgsig(init.body, 'fetch body');
                    }
                }

                return originalFetch(input, init).then(response => {
                    // 克隆响应以便可以读取内容
                    const clonedResponse = response.clone();
                    
                    // 检查响应头
                    try {
                        for (let entry of clonedResponse.headers.entries()) {
                            checkForMtgsig(entry[0], 'fetch response header key');
                            checkForMtgsig(entry[1], 'fetch response header value');
                        }
                    } catch (e) {
                        // 忽略错误
                    }
                    
                    // 检查响应体
                    clonedResponse.text().then(text => {
                        checkForMtgsig(text, 'fetch response text');
                    }).catch(e => {
                        // 忽略错误
                    });

                    return response;
                }).catch(error => {
                    checkForMtgsig(error, 'fetch error');
                    throw error;
                });
            };
        }

        // 监控localStorage和sessionStorage
        function enhanceStorage(storage, storageName) {
            if (!storage) return;
            
            const originalSetItem = storage.setItem;
            const originalGetItem = storage.getItem;
            
            storage.setItem = function(key, value) {
                checkForMtgsig(key, `${storageName} setItem key`);
                checkForMtgsig(value, `${storageName} setItem value`);
                return originalSetItem.apply(this, arguments);
            };
            
            storage.getItem = function(key) {
                const result = originalGetItem.apply(this, arguments);
                checkForMtgsig(key, `${storageName} getItem key`);
                checkForMtgsig(result, `${storageName} getItem result`);
                return result;
            };
        }
        
        // 增强localStorage和sessionStorage
        try {
            enhanceStorage(window.localStorage, 'localStorage');
        } catch (e) {
            // 在某些环境下访问localStorage可能会抛出异常
        }
        
        try {
            enhanceStorage(window.sessionStorage, 'sessionStorage');
        } catch (e) {
            // 在某些环境下访问sessionStorage可能会抛出异常
        }

        // 监控Headers构造函数
        if (window.Headers) {
            const originalHeadersConstructor = window.Headers;
            window.Headers = function(...args) {
                if (args[0]) {
                    checkForMtgsig(args[0], 'Headers constructor');
                }
                return new originalHeadersConstructor(...args);
            };
            window.Headers.prototype = originalHeadersConstructor.prototype;
        }

        // 监控eval函数
        if (window.eval) {
            const originalEval = window.eval;
            window.eval = function(...args) {
                checkForMtgsig(args[0], 'eval input');
                return originalEval.apply(this, args);
            };
        }

        // 监控Function构造函数
        if (window.Function) {
            const originalFunction = window.Function;
            window.Function = function(...args) {
                if (args.length > 0) {
                    checkForMtgsig(args[args.length - 1], 'Function constructor');
                }
                return originalFunction.apply(this, args);
            };
        }
    }
    
    // 通用监控 - JSON相关操作
    if (typeof JSON !== 'undefined') {
        const originalStringify = JSON.stringify;
        JSON.stringify = function(...args) {
            const result = originalStringify.apply(this, args);
            checkForMtgsig(args[0], 'JSON.stringify input');
            checkForMtgsig(result, 'JSON.stringify output');
            return result;
        };

        const originalParse = JSON.parse;
        JSON.parse = function(...args) {
            const result = originalParse.apply(this, args);
            checkForMtgsig(args[0], 'JSON.parse input');
            checkForMtgsig(result, 'JSON.parse output');
            return result;
        };
    }

    // 通用监控 - Base64相关操作
    if (typeof btoa !== 'undefined') {
        const originalBtoa = btoa;
        btoa = function(...args) {
            const result = originalBtoa.apply(this, args);
            checkForMtgsig(args[0], 'btoa input');
            checkForMtgsig(result, 'btoa output');
            return result;
        };
    }

    if (typeof atob !== 'undefined') {
        const originalAtob = atob;
        atob = function(...args) {
            const result = originalAtob.apply(this, args);
            checkForMtgsig(args[0], 'atob input');
            checkForMtgsig(result, 'atob output');
            return result;
        };
    }

    console.log('✅ mtgsig捕获脚本已就绪');
})();