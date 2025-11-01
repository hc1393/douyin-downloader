// ==UserScript==
// @name         mtgsig Generator Monitor
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  专门监控mtgsig生成过程的hook脚本
// @author       You
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    console.log('🔍 mtgsig监控脚本已启动');

    // 监控JSON.stringify，很多mtgsig生成过程中会使用
    const originalStringify = JSON.stringify;
    JSON.stringify = function(...args) {
        const result = originalStringify.apply(this, args);
        
        // 检查是否包含mtgsig相关字段
        if (result && result.includes('mtgsig')) {
            console.log('🔧 检测到JSON.stringify包含mtgsig:');
            console.log('数据:', args[0]);
            console.log('结果:', result);
            console.trace('调用栈:');
        }
        
        return result;
    };

    // 监控JSON.parse
    const originalParse = JSON.parse;
    JSON.parse = function(...args) {
        const result = originalParse.apply(this, args);
        
        // 检查解析结果是否包含mtgsig
        try {
            const str = JSON.stringify(result);
            if (str.includes('mtgsig')) {
                console.log('🔧 检测到JSON.parse包含mtgsig:');
                console.log('数据:', args[0]);
                console.log('结果:', str);
                console.trace('调用栈:');
            }
        } catch (e) {
            // 忽略无法序列化的对象
        }
        
        return result;
    };

    // 监控btoa (Base64编码)
    const originalBtoa = window.btoa;
    if (originalBtoa) {
        window.btoa = function(...args) {
            const result = originalBtoa.apply(this, args);
            
            // 检查是否可能与mtgsig相关
            if (args[0] && (args[0].includes('mtgsig') || args[0].length > 50)) {
                console.log('🔧 检测到btoa调用:');
                console.log('输入:', args[0]);
                console.log('输出:', result);
                console.trace('调用栈:');
            }
            
            return result;
        };
    }

    // 监控atob (Base64解码)
    const originalAtob = window.atob;
    if (originalAtob) {
        window.atob = function(...args) {
            const result = originalAtob.apply(this, args);
            
            // 检查结果是否包含关键字段
            if (result && (result.includes('mtgsig') || result.includes('a1') || result.includes('a2'))) {
                console.log('🔧 检测到atob调用:');
                console.log('输入:', args[0]);
                console.log('输出:', result);
                console.trace('调用栈:');
            }
            
            return result;
        };
    }

    // 监控Crypto相关API
    if (window.crypto && window.crypto.subtle) {
        const originalEncrypt = crypto.subtle.encrypt;
        crypto.subtle.encrypt = function(...args) {
            console.log('🔧 检测到crypto.subtle.encrypt调用:');
            console.log('算法:', args[0]);
            console.log('密钥:', args[1]);
            console.log('数据:', args[2]);
            console.trace('调用栈:');
            return originalEncrypt.apply(this, args);
        };

        const originalDigest = crypto.subtle.digest;
        crypto.subtle.digest = function(...args) {
            console.log('🔧 检测到crypto.subtle.digest调用:');
            console.log('算法:', args[0]);
            console.log('数据:', args[1]);
            console.trace('调用栈:');
            return originalDigest.apply(this, args);
        };
    }

    // 监控localStorage.getItem
    const originalGetItem = Storage.prototype.getItem;
    Storage.prototype.getItem = function(key) {
        const result = originalGetItem.apply(this, [key]);
        
        if (key && (key.includes('mtgsig') || key.includes('sig') || key.includes('token')) && result) {
            console.log('🔧 检测到localStorage.getItem调用:');
            console.log('键名:', key);
            console.log('值:', result);
            console.trace('调用栈:');
        }
        
        return result;
    };

    // 监控sessionStorage
    const originalSessionGetItem = Storage.prototype.getItem;
    Storage.prototype.getItem = function(key) {
        const result = originalSessionGetItem.apply(this, [key]);
        
        if (key && (key.includes('mtgsig') || key.includes('sig') || key.includes('token')) && result) {
            console.log('🔧 检测到sessionStorage.getItem调用:');
            console.log('键名:', key);
            console.log('值:', result);
            console.trace('调用栈:');
        }
        
        return result;
    };

    // 监控Date相关操作
    const originalDate = window.Date;
    const originalNow = Date.now;
    Date.now = function() {
        const result = originalNow.apply(this);
        // 可以在这里添加对时间戳的监控逻辑
        return result;
    };

    // 监控Math.random
    const originalRandom = Math.random;
    Math.random = function() {
        const result = originalRandom.apply(this);
        // mtgsig生成可能使用随机数
        return result;
    };

    // 监控eval
    const originalEval = window.eval;
    window.eval = function(...args) {
        if (args[0] && args[0].includes('mtgsig')) {
            console.log('🔧 检测到eval调用:');
            console.log('代码:', args[0]);
            console.trace('调用栈:');
        }
        return originalEval.apply(this, args);
    };

    // 监控Function构造函数
    const originalFunction = window.Function;
    window.Function = function(...args) {
        if (args.length > 0 && args[args.length - 1].includes('mtgsig')) {
            console.log('🔧 检测到动态函数创建:');
            console.log('参数:', args);
            console.trace('调用栈:');
        }
        return originalFunction.apply(this, args);
    };

    // 监控document.createElement，有些网站通过动态创建script标签加载签名逻辑
    const originalCreateElement = document.createElement;
    document.createElement = function(...args) {
        const element = originalCreateElement.apply(this, args);
        
        if (args[0] && args[0].toLowerCase() === 'script') {
            const originalSetAttribute = element.setAttribute;
            element.setAttribute = function(name, value) {
                if (name === 'src' && value && value.includes('sig')) {
                    console.log('🔧 检测到动态脚本加载:');
                    console.log('URL:', value);
                    console.trace('调用栈:');
                }
                return originalSetAttribute.apply(this, [name, value]);
            };
        }
        
        return element;
    };

    // 监控headers操作
    const originalHeadersConstructor = window.Headers;
    if (originalHeadersConstructor) {
        window.Headers = function(...args) {
            if (args[0]) {
                try {
                    const headersStr = JSON.stringify(args[0]);
                    if (headersStr.includes('mtgsig')) {
                        console.log('🔧 检测到Headers构造函数调用:');
                        console.log('参数:', args[0]);
                        console.trace('调用栈:');
                    }
                } catch (e) {}
            }
            return new originalHeadersConstructor(...args);
        };
        window.Headers.prototype = originalHeadersConstructor.prototype;
    }

    console.log('✅ mtgsig监控已就绪，正在等待相关操作...');
})();