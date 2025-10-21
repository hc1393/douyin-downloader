// 混淆的 hv 函数
function hv(e, t) {
    const n = Fn
      , a = {
        daDYt: function(s, c) {
            return s - c
        },
        pHRMA: function(s, c) {
            return s + c
        },
        mjnpX: function(s, c) {
            return s < c
        },
        ixQeb: function(s, c) {
            return s(c)
        },
        doHrL: function(s, c) {
            return s(c)
        },
        TEyRB: function(s, c) {
            return s === c
        },
        DKObb: function(s, c, u) {
            return s(c, u)
        },
        OAlyr: "RSA",
        sDglT: n(167),
        zMPlD: function(s, c) {
            return s(c)
        },
        tPXPh: function(s, c) {
            return s === c
        }
    };
    if (e = a[n(201)](t == null ? void 0 : t[n(215)], ![]) ? e : Js(a.DKObb(lv, e, (t == null ? void 0 : t[n(192)]) || (t == null ? void 0 : t.key))),
    (t == null ? void 0 : t.type) === a.OAlyr) {
        if (a[n(201)](a[n(170)], a[n(170)]))
            return a[n(204)](m8, e, t.key);
        {
            if (!_0x993272)
                return "";
            const s = new _0x9c7fe2;
            s.setPublicKey(_0x55617a(_0x17cfdb));
            const c = s.getKey()
              , u = c.n[n(194)]()
              , d = a[n(203)](a.pHRMA(u, 658 + -7 * 1195 + 2 * 3857) >> -6 * -827 + -2972 + -1987, -1405 + 929 * -5 + 319 * 19);
            let f = ""
              , _ = -5877 * 1 + -2215 + 8092
              , l = 9493 + 6597 + 1 * -16090;
            for (let h = 2658 + 151 * -65 + 7157, p = _0x1e2632[n(176)]; a[n(208)](h, p); h++) {
                const g = a[n(183)](_0x5e4342, _0x600d20[h]);
                l += g,
                l > d && (f += c[n(212)](_0x5b705a[n(177)](_, h)),
                _ = h,
                l = g)
            }
            return f += c[n(212)](_0xb28bfa[n(177)](_, _0x57713a[n(176)])),
            a[n(210)](_0x442baa, _0x3a9ec6[n(171)](_0x55d60d[n(181)](f)))[n(173)](/\+/g, "-")[n(173)](/\//g, "_").replace(/=+$/, "")
        }
    }
    const r = a[n(175)](fv, t)
      , i = ev[n(212)](e, Mr.parse(t[n(213)]), r);
    return a[n(180)](t == null ? void 0 : t[n(165)], ![]) ? a[n(183)](Js, LP[n(171)](i[n(200)])) : Ep.stringify(i[n(200)])
}

// 占位符函数和变量（实际使用时需要替换为真实实现）
function Fn(index) {
    // 这应该是一个字符串解密函数
    // 根据记忆，这可能与函数R类似，返回预定义的加密字符串数组中的元素
    return "string_" + index;
}

function Js(data) {
    // 未知的处理函数
    return data;
}

function lv(data, key) {
    // 未知的处理函数
    return data;
}

function m8(data, key) {
    // 未知的处理函数
    return data;
}

function fv(data) {
    // 未知的处理函数
    return data;
}

function ev(data) {
    // 未知的处理函数
    return {
        encrypt: function() { return data; }
    };
}

const Mr = {
    parse: function(data) {
        return data;
    }
};

const Ep = {
    stringify: function(data) {
        return JSON.stringify(data);
    }
};

const LP = {
    encrypt: function(data) {
        return data;
    }
};

// 测试用例
// const result = hv("test_data", {type: "RSA", key: "public_key"});
// console.log(result);