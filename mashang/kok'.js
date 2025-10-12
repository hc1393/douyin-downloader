const P = {
    init: function(words, sigBytes) {
        return new WordArray(words, sigBytes);
    }
};

// l 对象将指向 WordArray 的构造函数
const l = {
    init: function(words, sigBytes) {
        return new WordArray(words, sigBytes);
    }
};

// 3. 保存原始 init 方法
const s = P.init;

// 4. 覆盖 P.init 方法 - 处理多种数据格式
P.init = function(t) {
    // 处理不同类型的输入
    t = t instanceof ArrayBuffer ? new Uint8Array(t) : t;

    // 检查 TypedArray 类型
    const isTypedArray = t instanceof Int8Array ||
        (typeof Uint8ClampedArray !== 'undefined' && t instanceof Uint8ClampedArray) ||
        t instanceof Int16Array ||
        t instanceof Uint16Array ||
        t instanceof Int32Array ||
        t instanceof Uint32Array ||
        t instanceof Float32Array ||
        t instanceof Float64Array;

    if (isTypedArray) {
        t = new Uint8Array(t.buffer, t.byteOffset, t.byteLength);
    }

    if (t instanceof Uint8Array) {
        const e = t.byteLength;
        const r = [];

        // 将字节转换为32位整数（大端序）
        for (let i = 0; i < e; i++) {
            const wordIndex = i >>> 2;  // Math.floor(i/4)
            const shift = 24 - (i % 4) * 8;

            if (!r[wordIndex]) r[wordIndex] = 0;
            r[wordIndex] |= t[i] << shift;
        }

        // 调用原始方法处理转换后的数据
        return s.call(this, r, e);
    } else {
        // 直接处理非二进制数据
        return s.apply(this, arguments);
    }
};

// 5. 设置原型链
P.init.prototype = WordArray.prototype;

// 6. 定义字符串转换函数 a()
function a(t) {
    const e = t.length;
    const r = [];

    for (let i = 0; i < e; i++) {
        const wordIndex = i >>> 2;
        const shift = 24 - (i % 4) * 8;
        const charCode = t.charCodeAt(i) & 0xFF;

        if (!r[wordIndex]) r[wordIndex] = 0;
        r[wordIndex] |= charCode << shift;
    }

    // 直接使用 P.init 创建对象
    return new P.init(r, e);
}

function parse(t) {
                return a(unescape(encodeURIComponent(t)))
            }
var t="jo8j9wGw%6HbxfFn"
console.log(parse(t))
