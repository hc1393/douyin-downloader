// 用于运行加密.js文件的包装器
// 解决 define is not defined 错误

// 引入必要的模块
const fs = require('fs');
const vm = require('vm');
const path = require('path');

// 创建一个模拟的 AMD define 函数
global.define = function(name, deps, callback) {
    if (typeof name !== 'string') {
        callback = deps;
        deps = name;
        name = null;
    }
    
    if (!Array.isArray(deps)) {
        callback = deps;
        deps = [];
    }
    
    // 解析依赖项
    const resolvedDeps = deps.map(dep => {
        if (dep === 'require') return require;
        if (dep === 'module') return module;
        if (dep === 'exports') return exports;
        // 对于浏览器全局对象，提供模拟实现
        if (dep === 'window') return global;
        if (dep === 'document') return createMockDocument();
        return require(dep);
    });
    
    // 执行回调函数
    const result = callback.apply(null, resolvedDeps);
    
    // 如果有模块名，将其存储在全局对象中
    if (name) {
        global[name] = result;
    }
    
    return result;
};

// 模拟浏览器环境的一些全局对象
global.window = global;
global.document = createMockDocument();
global.frames = global;
global.self = global;
global.location = {
    href: 'http://localhost',
    protocol: 'http:',
    host: 'localhost',
    hostname: 'localhost',
    port: '',
    pathname: '/',
    search: '',
    hash: '',
    origin: 'http://localhost'
};
global.navigator = {
    userAgent: 'Node.js Environment',
    platform: process.platform,
    language: 'zh-CN'
};
global.localStorage = {
    getItem: function(key) { return this[key]; },
    setItem: function(key, value) { this[key] = String(value); },
    removeItem: function(key) { delete this[key]; }
};
global.history = {};
global.screen = {};
global.alert = function() {};
global.confirm = function() { return true; };
global.prompt = function() { return ''; };
global.XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;
global.WebSocket = require('ws');

// 创建一个模拟的 document 对象
function createMockDocument() {
    return {
        createElement: function(tagName) {
            return {
                tagName: tagName.toUpperCase(),
                style: {},
                setAttribute: function(name, value) {
                    this[name] = value;
                },
                getAttribute: function(name) {
                    return this[name];
                }
            };
        },
        getElementById: function() { return null; },
        getElementsByTagName: function() { return []; },
        addEventListener: function() {},
        removeEventListener: function() {},
        cookie: '',
        location: global.location
    };
}

// 读取并执行加密.js文件
try {
    const filePath = path.resolve(__dirname, '霸王茶姬/加密.js');
    const code = fs.readFileSync(filePath, 'utf8');
    
    // 创建一个沙箱环境来执行代码
    const sandbox = {
        global: global,
        process: process,
        console: console,
        setTimeout: setTimeout,
        setInterval: setInterval,
        clearTimeout: clearTimeout,
        clearInterval: clearInterval,
        Buffer: Buffer,
        require: require,
        __dirname: __dirname,
        __filename: __filename,
        module: module,
        exports: exports
    };
    
    // 将全局变量添加到沙箱中
    Object.keys(global).forEach(key => {
        sandbox[key] = global[key];
    });
    
    // 在沙箱环境中执行代码
    vm.createContext(sandbox);
    vm.runInContext(code, sandbox);
    
    console.log('加密.js 文件执行完成');
} catch (error) {
    console.error('执行加密.js文件时出错:', error);
}