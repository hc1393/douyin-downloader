// ==UserScript==
// @name         Request Monitor Hook
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  监控网页中的fetch和XHR请求，特别关注猫眼电影API等接口
// @author       You
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // 保存原始函数
    const originalFetch = window.fetch;
    const originalXHR = window.XMLHttpRequest;

    // 监控fetch请求
    window.fetch = function(...args) {
        const url = args[0] instanceof Request ? args[0].url : args[0];
        const options = args[1] || {};

        // 检查是否为目标API
        if (url && url.includes('maoyan.com')) {
            console.log('🔍 拦截到猫眼电影API请求:');
            console.log('URL:', url);
            console.log('Options:', options);
            
            // 记录headers
            if (options.headers) {
                console.log('Headers:', options.headers);
            }
            
            // 记录请求体
            if (options.body) {
                console.log('Body:', options.body);
            }
        }

        // 执行原始fetch并监控响应
        return originalFetch.apply(this, args).then(response => {
            // 如果是目标API，记录响应
            if (url && url.includes('maoyan.com')) {
                const clonedResponse = response.clone();
                clonedResponse.json().then(data => {
                    console.log('🐱 猫眼电影API响应数据:');
                    console.log(JSON.stringify(data, null, 2));
                }).catch(err => {
                    console.log('🐱 猫眼电影API响应(非JSON):', clonedResponse);
                });
            }
            return response;
        }).catch(error => {
            if (url && url.includes('maoyan.com')) {
                console.log('❌ 猫眼电影API请求错误:', error);
            }
            throw error;
        });
    };

    // 监控XMLHttpRequest请求
    const originalOpen = window.XMLHttpRequest.prototype.open;
    const originalSend = window.XMLHttpRequest.prototype.send;
    const originalSetRequestHeader = window.XMLHttpRequest.prototype.setRequestHeader;

    window.XMLHttpRequest.prototype.open = function(method, url, ...args) {
        this._method = method;
        this._url = url;
        return originalOpen.apply(this, [method, url, ...args]);
    };

    window.XMLHttpRequest.prototype.setRequestHeader = function(header, value) {
        this._headers = this._headers || {};
        this._headers[header] = value;
        return originalSetRequestHeader.apply(this, [header, value]);
    };

    window.XMLHttpRequest.prototype.send = function(body) {
        // 检查是否为目标API
        if (this._url && this._url.includes('maoyan.com')) {
            console.log('📡 拦截到猫眼电影XHR请求:');
            console.log('Method:', this._method);
            console.log('URL:', this._url);
            console.log('Headers:', this._headers);
            console.log('Body:', body);
            
            // 监控响应
            const originalOnReadyStateChange = this.onreadystatechange;
            this.onreadystatechange = function(...args) {
                if (this.readyState === 4) {
                    console.log('📥 猫眼电影XHR响应状态:', this.status);
                    console.log('📥 猫眼电影XHR响应头:', this.getAllResponseHeaders());
                    try {
                        const data = JSON.parse(this.responseText);
                        console.log('📥 猫眼电影XHR响应数据:', JSON.stringify(data, null, 2));
                    } catch (e) {
                        console.log('📥 猫眼电影XHR响应文本:', this.responseText);
                    }
                }
                if (originalOnReadyStateChange) {
                    return originalOnReadyStateChange.apply(this, args);
                }
            };
        }
        
        return originalSend.apply(this, [body]);
    };

    // 监控Cookie变化
    const originalCookie = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie');
    Object.defineProperty(document, 'cookie', {
        get() {
            const value = originalCookie.get.call(this);
            // 只记录包含关键字段的cookie
            if (value && (value.includes('mtgsig') || value.includes('openid') || value.includes('token'))) {
                console.log('🍪 敏感Cookie读取:', value);
            }
            return value;
        },
        set(value) {
            // 记录设置敏感cookie的操作
            if (value && (value.includes('mtgsig') || value.includes('openid') || value.includes('token'))) {
                console.log('🍪 敏感Cookie设置:', value);
                console.trace('Cookie设置调用栈:');
            }
            return originalCookie.set.call(this, value);
        }
    });

    // 监控localStorage操作
    const originalSetItem = Storage.prototype.setItem;
    Storage.prototype.setItem = function(key, value) {
        // 记录包含关键字段的localStorage操作
        if (key && (key.includes('token') || key.includes('openid') || key.includes('mtgsig'))) {
            console.log('💾 敏感LocalStorage设置:');
            console.log('Key:', key);
            console.log('Value:', value);
            console.trace('LocalStorage设置调用栈:');
        }
        return originalSetItem.apply(this, [key, value]);
    };

    // 监控Headers append/set操作
    const originalHeadersAppend = Headers.prototype.append;
    const originalHeadersSet = Headers.prototype.set;
    
    Headers.prototype.append = function(name, value) {
        if (name && (name.includes('token') || name.includes('auth') || name.includes('sign'))) {
            console.log('🏷️ 敏感Headers追加:');
            console.log('Name:', name);
            console.log('Value:', value);
        }
        return originalHeadersAppend.apply(this, [name, value]);
    };
    
    Headers.prototype.set = function(name, value) {
        if (name && (name.includes('token') || name.includes('auth') || name.includes('sign'))) {
            console.log('🏷️ 敏感Headers设置:');
            console.log('Name:', name);
            console.log('Value:', value);
        }
        return originalHeadersSet.apply(this, [name, value]);
    };

    console.log('🚀 Request Monitor Hook 已启动');
    console.log('📝 正在监控猫眼电影API请求、敏感Cookie和localStorage操作...');
})();