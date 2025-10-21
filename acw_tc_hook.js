// acw_tc Cookie监控Hook脚本
(function() {
    console.log('[ACW_TC HOOK] 已加载acw_tc监控脚本');
    
    // 保存原始的Cookie设置方法
    const originalCookieSetter = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie') || 
                               Object.getOwnPropertyDescriptor(HTMLDocument.prototype, 'cookie');
    
    if (originalCookieSetter && originalCookieSetter.set) {
        // Hook Cookie设置
        Object.defineProperty(document, 'cookie', {
            set: function(cookie) {
                if (cookie.indexOf('acw_tc=') !== -1) {
                    console.log('[ACW_TC HOOK] 检测到acw_tc Cookie设置:', cookie);
                    // 提取acw_tc值
                    const match = cookie.match(/acw_tc=([^;]+)/);
                    if (match) {
                        const acwTcValue = match[1];
                        console.log('[ACW_TC HOOK] acw_tc值:', acwTcValue);
                        // 可以在这里添加更多处理逻辑，比如存储到全局变量
                        window._acw_tc_value = acwTcValue;
                    }
                }
                return originalCookieSetter.set.call(this, cookie);
            },
            get: function() {
                return originalCookieSetter.get.call(this);
            }
        });
    }
    
    // Hook XMLHttpRequest
    const originalXHR = window.XMLHttpRequest;
    function hookXHR() {
        const hookedXHR = function() {
            const xhrInstance = new originalXHR();
            const originalSetRequestHeader = xhrInstance.setRequestHeader;
            const originalOpen = xhrInstance.open;
            
            // 监听请求头设置
            xhrInstance.setRequestHeader = function(name, value) {
                if (name.toLowerCase() === 'cookie' && value.indexOf('acw_tc') !== -1) {
                    console.log('[ACW_TC HOOK] XHR请求中携带acw_tc Cookie:', value);
                }
                return originalSetRequestHeader.apply(this, arguments);
            };
            
            // 监听响应
            const originalOnReadyStateChange = xhrInstance.onreadystatechange;
            xhrInstance.onreadystatechange = function() {
                if (xhrInstance.readyState === 4) {
                    // 检查响应头中的Set-Cookie
                    const setCookie = xhrInstance.getResponseHeader('Set-Cookie') || 
                                     xhrInstance.getResponseHeader('set-cookie');
                    if (setCookie && setCookie.indexOf('acw_tc=') !== -1) {
                        console.log('[ACW_TC HOOK] XHR响应中包含acw_tc:', setCookie);
                        const match = setCookie.match(/acw_tc=([^;]+)/);
                        if (match) {
                            const acwTcValue = match[1];
                            console.log('[ACW_TC HOOK] 响应中的acw_tc值:', acwTcValue);
                            window._acw_tc_value = acwTcValue;
                        }
                    }
                }
                if (originalOnReadyStateChange) {
                    return originalOnReadyStateChange.apply(this, arguments);
                }
            };
            
            return xhrInstance;
        };
        
        // 复制原始XHR的属性
        Object.keys(originalXHR).forEach(key => {
            hookedXHR[key] = originalXHR[key];
        });
        
        hookedXHR.prototype = originalXHR.prototype;
        return hookedXHR;
    }
    
    window.XMLHttpRequest = hookXHR();
    
    // Hook fetch API
    const originalFetch = window.fetch;
    if (originalFetch) {
        window.fetch = function() {
            const args = arguments;
            const url = args[0];
            const options = args[1] || {};
            
            // 检查请求中是否携带了acw_tc
            if (options.headers) {
                const headers = new Headers(options.headers);
                const cookieHeader = headers.get('Cookie') || headers.get('cookie');
                if (cookieHeader && cookieHeader.indexOf('acw_tc') !== -1) {
                    console.log('[ACW_TC HOOK] Fetch请求中携带acw_tc Cookie:', cookieHeader);
                }
            }
            
            // 执行原始fetch
            return originalFetch.apply(this, arguments).then(response => {
                // 检查响应中的Set-Cookie
                const setCookie = response.headers.get('Set-Cookie') || 
                                 response.headers.get('set-cookie');
                if (setCookie && setCookie.indexOf('acw_tc=') !== -1) {
                    console.log('[ACW_TC HOOK] Fetch响应中包含acw_tc:', setCookie);
                    const match = setCookie.match(/acw_tc=([^;]+)/);
                    if (match) {
                        const acwTcValue = match[1];
                        console.log('[ACW_TC HOOK] 响应中的acw_tc值:', acwTcValue);
                        window._acw_tc_value = acwTcValue;
                    }
                }
                return response;
            });
        };
    }
    
    console.log('[ACW_TC HOOK] acw_tc监控已启动');
})();