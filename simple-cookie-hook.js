(function() {
    console.log('开始安装Cookie监控hook...');
    
    // Hook Cookie操作
    function hookCookies() {
        try {
            const cookieDesc = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie') || 
                              Object.getOwnPropertyDescriptor(HTMLDocument.prototype, 'cookie');
            
            if (!cookieDesc) {
                console.warn('无法获取cookie属性描述符');
                return;
            }
            
            const originalCookieSetter = cookieDesc.set;
            const originalCookieGetter = cookieDesc.get;
            
            Object.defineProperty(document, 'cookie', {
                set: function(value) {
                    console.log('[Cookie Set]:', value);
                    // 特别关注反爬虫相关的cookie
                    if (value.includes('acw_tc') || value.includes('ssxmod_itna')) {
                        console.log('[Anti-spider Cookie Detected!]:', value);
                        // 根据历史经验，acw_tc和ssxmod_itna是常见的反爬虫cookie
                        console.log('[调用栈]:', new Error().stack);
                        debugger;
                    }
                    return originalCookieSetter.call(this, value);
                },
                get: function() {
                    const cookie = originalCookieGetter.call(this);
                    console.log('[Cookie Get]:', cookie);
                    // 分析获取到的cookie中是否包含反爬虫相关字段
                    if (cookie && (cookie.includes('acw_tc') || cookie.includes('ssxmod_itna'))) {
                        console.log('[Anti-spider Cookie Found!]:', cookie);
                        console.log('[调用栈]:', new Error().stack);
                        debugger;
                    }
                    return cookie;
                },
                configurable: true
            });
            
            console.log('Cookie hook安装成功');
        } catch (e) {
            console.error('Cookie hook安装失败:', e);
        }
    }
    
    // Hook document.cookie直接赋值
    function hookDocumentCookie() {
        try {
            let cookieValue = '';
            Object.defineProperty(document, 'cookie', {
                set: function(value) {
                    console.log('[Document.Cookie Set]:', value);
                    // 特别关注反爬虫相关的cookie
                    if (value.includes('acw_tc') || value.includes('ssxmod_itna')) {
                        console.log('[Anti-spider Cookie Detected!]:', value);
                        console.log('[调用栈]:', new Error().stack);
                        // 为了更好地追踪cookie生成位置，我们在这里暂停执行
                        debugger;
                    }
                    cookieValue = value;
                },
                get: function() {
                    console.log('[Document.Cookie Get]:', cookieValue);
                    // 分析获取到的cookie中是否包含反爬虫相关字段
                    if (cookieValue && (cookieValue.includes('acw_tc') || cookieValue.includes('ssxmod_itna'))) {
                        console.log('[Anti-spider Cookie Found!]:', cookieValue);
                        console.log('[调用栈]:', new Error().stack);
                        // 为了更好地追踪cookie使用位置，我们在这里暂停执行
                        debugger;
                    }
                    return cookieValue;
                },
                configurable: true
            });
            console.log('Document.cookie hook安装成功');
        } catch (e) {
            console.error('Document.cookie hook安装失败:', e);
        }
    }
    
    // 主函数
    function main() {
        hookCookies();
        hookDocumentCookie();
        
        console.log('Cookie hook安装完成！');
        console.log('现在可以进行调试了。');
        // 显示当前页面的cookie信息
        console.log('当前页面cookie信息:', document.cookie);
        // 特别检查反爬虫cookie
        if (document.cookie.includes('acw_tc') || document.cookie.includes('ssxmod_itna')) {
            console.log('[Warning] 检测到反爬虫cookie:', document.cookie);
        }
    }
    
    // 页面加载完成后执行
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', main);
    } else {
        main();
    }
})();