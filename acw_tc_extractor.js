(function(){
// 定义缺失的变量和函数
var On = {
    getItem: function(key) { return localStorage.getItem(key); },
    setItem: function(key, value) { localStorage.setItem(key, value); }
};

var Wa = function(key) { return key; };

var Rt = null; // 全局变量

var Up = function() {
    return Math.random().toString(16).substring(2, 10);
};

var ui = function(data, options) {
    // 简单的加密函数，实际应该使用AES
    return btoa(JSON.stringify(data));
};

var li = function(data, options) {
    // 简单的解密函数，实际应该使用AES
    try {
        return JSON.parse(atob(data));
    } catch (e) {
        return data;
    }
};

var Vp = function(data) {
    return data.split(':');
};

var Mr = function(data) {
    return data;
};

var Ro = function(data) {
    return data;
};

var Fn = function(index) {
    const strings = ["replace", "join", "parse"];
    return strings[index] || "replace";
};

var Js = function(data) {
    return data.replace(/={1,2}$/, "");
};

var p = {
    parse: function(data) {
        return data;
    }
};

function set(e, t, n, a, r, i, s) {
        var c = s
          , u = ""
          , d = ""
          , f = "";
        if ((n = n == null ? 73e3 : n) !== 0) {
            var _ = new Date;
            String(n).slice(-1) === "s" ? _.setTime(_.getTime() + 1e3 * Number(String(n).slice(0, -1))) : _.setTime(_.getTime() + 24 * n * 60 * 60 * 1e3),
            u = "; expires=" + _.toGMTString()
        }
        function l(y) {
            return !!y && y.replace(/\r\n/g, "")
        }
        Be(r) && r !== "" && (f = "; SameSite=" + r),
        i && (d = "; secure");
        var h = ""
          , p = ""
          , g = "";
        e && (h = l(e)),
        t && (p = l(t)),
        c && (g = l(c)),
        h && p && (cookie = h + "=" + encodeURIComponent(p) + u + "; path=/" + g + f + d)
    return cookie
}

function Be(e) {
    return Object.prototype.toString.call(e) == "[object String]"
}

function be(e) {
    return e != null && Object.prototype.toString.call(e) == "[object Object]"
}
var y0 = function() {
    var e = new Date().getTime();
    return function(t) {
        return Math.ceil((e = (9301 * e + 49297) % 233280) / 233280 * t)
    }
}();
function En() {
    if (typeof Uint32Array == "function") {
        var e = "";
        if (typeof crypto != "undefined" ? e = crypto : typeof msCrypto != "undefined" && (e = msCrypto),
        be(e) && e.getRandomValues) {
            var t = new Uint32Array(1);
            return e.getRandomValues(t)[0] / Math.pow(2, 32)
        }
    }
    return y0(1e19) / 1e19
}
var e = function() {
        for (var t = 1 * new Date, n = 0; t == 1 * new Date; )
            n++;
        return t.toString(16) + n.toString(16)
    };
function cs() {
        var t = String(921600);
        t = t && /\d{5,}/.test(t) ? t.toString(16) : String(31242 * En()).replace(".", "").slice(0, 8);
        var n = e() + "-" + En().toString(16).replace(".", "") + "-" + function() {
            var a, r, i = navigator.userAgent, s = [], c = 0;
            function u(d, f) {
                var _, l = 0;
                for (_ = 0; _ < f.length; _++)
                    l |= s[_] << 8 * _;
                return d ^ l
            }
            for (a = 0; a < i.length; a++)
                r = i.charCodeAt(a),
                s.unshift(255 & r),
                s.length >= 4 && (c = u(c, s),
                s = []);
            return s.length > 0 && (c = u(c, s)),
            c.toString(16)
        }() + "-" + t + "-" + e();
        return n || (String(En()) + String(En()) + String(En())).slice(2, 15)
}
function ka(){
    return cs()
}
// 整理：移除示例日志与演示性设置


// 整理：移除演示性 Base64 编解码示例
// 定义存储接口数组
const Wu = [
    { name: 'cookie', read: function(key) { return document.cookie.split(';').find(c => c.trim().startsWith(key + '='))?.split('=')[1]; }, write: function(key, value) { document.cookie = key + '=' + value + '; path=/'; } },
    { name: 'sessionStorage', read: function(key) { return sessionStorage.getItem(key); }, write: function(key, value) { sessionStorage.setItem(key, value); } },
    { name: 'localStorage', read: function(key) { return localStorage.getItem(key); }, write: function(key, value) { localStorage.setItem(key, value); } }
];
const lr = Mc;
var Ss = typeof btoa === lr(334) ? "__" + btoa("@#$%^&") + "__" : "__QCMkJV4m__"
function Rc() {
    const e = ["parse", "assign", "10190RdYmdo", "pgrnR", "8wRasvg", "create", "2HkiSel", "366108gqFYsq", "write", "name", "memory", "localStorage", "remove", "KEUmV", "sessionStorage", "748924rlrSZD", "129031GuZKUC", "524514ombcXK", "function", "stringify", "oDKox", "excludes", "read", "6921MkiWdT", "FRRTR", "LncWf", "forEach", "Iwftm", "includes", "506225aiYmxM", "198019NAYyiH"];
    return Rc = function() {
        return e
    }
    ,
    Rc()
}
function n(c) {
        return e[ar(245)](c)
    }
function Mc(e, t) {
    const n = Rc();
    return Mc = function(a, r) {
        return a = a - 323,
        n[a]
    }
    ,
    Mc(e, t)
}
function Nc() {
    const e = ["66145NdJamj", "7273413MMmzfi", "2720968BkPoHp", "clear", "getItem", "36fdsDqT", "key", "Nliml", "21LzrjSB", "23111316orKyCM", "874702EOYtxE", "634787zrkYNZ", "hcwgx", "setItem", "removeItem", "778052LoyKre"];
    return Nc = function() {
        return e
    }
    ,
    Nc()
}
function ar(e, t) {
    const n = Nc();
    return ar = function(a, r) {
        return a = a - 238,
        n[a]
    },
    ar(e, t)
}
function dog(e) {
        const t = lr;
        for (const n of Wu) {
            const a = n.read("" + Ss + e);
            if (a == null) {
                continue
            }
            try {
                return JSON.parse(a)
            } catch (r) {
                return a
            }
        }
}
// '__QCMkJV4m__QoooOQ'


function Wc() {
    const e = ["782721jXMZoR", "70jaXZiw", "split", "SrsqE", "set", "810492LafFHn", "includes", "all", "forEach", "string", "2796EthDtZ", "onPostSuccess", "569149ltqRGh", "remove", "OfflineAudio", "1570144DlydhK", "host", "ClipboardData", "get", "42976LNyinn", "data", "resolve", "UMvDq", "push", "fid", "Cjjyn", "aesKey", "fingerprint", "bfDqK", "stack", "zInNp", "uYylY", "xvfzs", "_fmd", "10929NEdIey", "length", "slice", "fp_token_exp", "122CqIBCc", "Canvas", "onCollect", "keys", "KDIww", "catch", "oOo", "then", "stringify", "publicKey", "eQkwD", "QViUp", "appKey", "Gvock", "platform", "_fpcanvas", "join", "customKey", "2215SuypTW", "Ooo", "fp_token", "message", "XhuMh", "toUTCString", "fingerprint_decrypt_fail", "apply", "onLaunch", "getTime", "fingerprint_collect_fail", "RSA", "OOo", "LTQIw", "HWMKm", "reduce", "onError", "onCollectSuccess", "finally", "referPath", "assign"];
    return Wc = function() {
        return e
    }
    ,
    Wc()
}
function bn(e, t) {
    const n = Wc();
    return bn = function(a, r) {
        return a = a - 402,
        n[a]
    }
    ,
    bn(e, t)
}
function g8(e) {
    const t = Fn;
    return {
        OPVYs: function(n, a) {
            return n(a)
        }
    }.OPVYs(Js, Ro.join(Mr.parse(e)))
}
// Ml ={
//     const e = bn
//       , t = Rt == null ? void 0 : Rt[e(431)];
//     if (!t)
//        return "";
// }
function Ml() {
    const e = bn
      , t = Rt == null ? void 0 : Rt.appKey;
    if (!t)
        return "";
    const n = On.getItem("fp_token")
      , a = n ? li(n, {
        key: t
    }) : ""
      , r = On.getItem("fp_token_exp")
      , i = a ? Vp(r).split(":").reduce( (s, c) => li(c, {
        custom: ![],
        key: a,
        iv: li(s, {
            custom: ![],
            key: t
        })
    })) : "";
    if (i && a) {
        const s = Up()
          , c = [ui(s, {
            custom: ![],
            key: t
        }), ui(i, {
            key: a,
            iv: s,
            custom: ![]
        }), new Date().getTime()]
          , u = g8(c.join(":"));
        return On.setItem(Wa("fp_token"), u),
        On.setItem(Wa("fp_token_exp"), new Date().getTime() + 5 * 60 * 1e3),
        u
    }
    return ""
}
function setStorage(e, t, n) {
        if (t === void 0)
            return dog(e);
        const r = n == null ? void 0 : n.includes
          , i = n == null ? void 0 : n.excludes
          , s = JSON.stringify(t);
        return Wu.forEach(c => {
            if ((!r || r.includes(c.name)) && (!i || !i.includes(c.name))) {
                c.write("" + Ss + e, s)
            }
        }),
        t
    }
e='QooOOQ'

On.setItem(Wa("fp_token_exp"), new Date().getTime() + 5 * 60 * 1e3)

function Ks() {
    const e = ["substring", "15zvImfh", "GSeaK", "tPXPh", "parse", "SamPR", "ixQeb", "getKey", "ECB", "564JZNCxN", "qrPhN", "toString", "aZSea", "sjRuQ", "mode", "customKey", "xeBvv", "bitLength", "setPublicK", "ZUnUS", "22567597dVdPBB", "7GKmwvV", "2934564HzwAvW", "ciphertext", "TEyRB", "779252BSjiKl", "daDYt", "DKObb", "CBC", "yUpBn", "function", "mjnpX", "7899312dmqckX", "doHrL", "trim", "encrypt", "key", "9hoQCwk", "custom", "105137rJFzCv", "nqYsH", "210PsfbxD", "320353etwAUt", "QRbUm", "hex", "decrypt", "WtmgX", "padding", "22ybYSdK", "sDglT", "stringify", "374823UvmZaL", "replace", "OPVYs", "zMPlD", "length"];
    return Ks = function() {
        return e
    }
    ,
    Ks()
}
function Js(e) {
    return e[Fn(173)](/={1,2}$/, "")
}
function stringify(u) {
                        var d = u.words
                          , f = u.sigBytes
                          , _ = this._map;
                        u.clamp();
                        for (var l = [], h = 0; h < f; h += 3)
                            for (var p = d[h >>> 2] >>> 24 - h % 4 * 8 & 255, g = d[h + 1 >>> 2] >>> 24 - (h + 1) % 4 * 8 & 255, y = d[h + 2 >>> 2] >>> 24 - (h + 2) % 4 * 8 & 255, w = p << 16 | g << 8 | y, v = 0; v < 4 && h + v * .75 < f; v++)
                                l.push(_.charAt(w >>> 6 * (3 - v) & 63));
                        var k = _.charAt(64);
                        if (k)
                            for (; l.length % 4; )
                                l.push(k);
                        return l.join("")
                    }
function Ys(e, t) {
    const n = Ks();
    return Ys = function(a, r) {
        return a = a - (-126 * -61 + 8665 * -1 + -572 * -2),
        n[a]
    }
    ,
    Ys(e, t)
}
function g8(e) {
    const t = Ys;
    return {
        OPVYs: function(n, a) {
            return n(a)
        }
    }.OPVYs(Js, Ro.join(Mr.parse(e)))
}
function f(v) {
                        return p.parse(unescape(encodeURIComponent(v)))
                    }
// 整理：移除示例输出
})();
// ACW environment integration (isolated scope)
(function(){
    // lightweight shims to make the injected code runnable if host doesn't provide them
    if (typeof Ne === "undefined") {
        var Ne = Object.assign ? Object.assign.bind(Object) : function(target){
            for (var i=1;i<arguments.length;i++){ var src=arguments[i]||{}; for (var k in src){ if (Object.prototype.hasOwnProperty.call(src,k)) target[k]=src[k]; } }
            return target;
        };
    }
    if (typeof gv === "undefined") {
        var gv = {
            encrypt: {
                encrypt: function(data, opts){ try { return btoa(typeof data === 'string' ? data : JSON.stringify(data)); } catch(e){ return ""; } },
                decrypt: function(data, opts){ try { return atob(data); } catch(e){ return ""; } },
                encode: function(s){ return String(s); },
                decode: function(s){ return String(s); },
                base64UrlEncode: function(s){ try { var b = typeof s === 'string' ? btoa(s) : s; return b.replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,''); } catch(e){ return ""; } },
                getRandomString: function(){ return Math.random().toString(16).slice(2,10); }
            },
            hash: {
                x64hash128: function(s){ try { return (btoa(unescape(encodeURIComponent(String(s)))) + Array(34).join('0')).slice(0,32); } catch(e){ return (String(s)+Array(33).join('0')).slice(0,32); } }
            }
        };
    }
    if (typeof De === "undefined") {
        var De = { request: function(opts){
            return new Promise(function(resolve){
                try {
                    if (typeof fetch === 'function') {
                        var init = { method: opts && opts.method || 'GET', headers: opts && opts.header || {} };
                        if (opts && opts.data && init.method !== 'GET') { init.body = JSON.stringify(opts.data); if (!init.headers['Content-Type']) init.headers['Content-Type']='application/json'; }
                        fetch(String(opts && opts.url || ''), init).then(function(r){ return r.text(); }).then(function(t){ try{ resolve(JSON.parse(t)); } catch(_){ resolve({}); } }).catch(function(){ resolve({}); });
                    } else {
                        resolve({});
                    }
                } catch(_) { resolve({}); }
            });
        } };
    }
    if (typeof Yv === "undefined") {
        var Yv = function(){ return ""; };
    }

    // Public API container
    if (typeof window !== 'undefined') {
        window.ACWEnv = window.ACWEnv || {};
    }

    // Begin injected user-provided code block
    const bt = Pc;
    (function(e, t) {
        const n = Pc
          , a = e();
        for (; []; )
            try {
                if (-parseInt(n(170)) / 1 * (parseInt(n(162)) / 2) + -parseInt(n(167)) / 3 * (-parseInt(n(185)) / 4) + parseInt(n(189)) / 5 * (parseInt(n(153)) / 6) + -parseInt(n(166)) / 7 + parseInt(n(172)) / 8 + -parseInt(n(160)) / 9 * (-parseInt(n(190)) / 10) + parseInt(n(161)) / 11 * (-parseInt(n(154)) / 12) === t)
                    break;
                a.push(a.shift())
            } catch (r) {
                a.push(a.shift())
            }
    }
    )(Sc, 294010);
    var L_;
    const ca = ((L_ = globalThis == null ? void 0 : globalThis.navigator) == null ? void 0 : L_[bt(152)]) || bt(177)
      , d9 = /macintosh/i[bt(169)](ca)
      , Fv = /ipad/i[bt(169)](ca) || d9 && navigator[bt(184)] > 1
      , Vv = /iphone/i.test(ca)
      , Bp = bt(187)in ((globalThis == null ? void 0 : globalThis[bt(180)]) || {}) || /firefox/i[bt(169)](ca)
      , Uv = /trident/i[bt(169)](ca) || /msie/i[bt(169)](ca)
      , qv = /edge/i[bt(169)](ca)
      , p9 = /webkit/i[bt(169)](ca) && !qv
      , f9 = /IqiyiApp/[bt(169)](ca);
    var R_;
    const $p = typeof ((R_ = globalThis == null ? void 0 : globalThis.window) == null ? void 0 : R_.chrome) !== bt(178) || /chrome/i[bt(169)](ca) || /CriOS/i[bt(169)](ca);
    var M_;
    const Bo = ((M_ = window == null ? void 0 : window[bt(156)]) == null ? void 0 : M_[bt(175)]) || ( () => 0);
    var B_;
    const Hv = ((B_ = window == null ? void 0 : window.console) == null ? void 0 : B_[bt(188)]) || ( () => 0)
      , h9 = () => {
        const e = bt;
        if (Bp || Uv)
            return;
        const t = / /;
        let n = ![];
        return t[e(165)] = () => {
            const a = e;
            return a(183) !== a(158) ? (n = !![],
            a(157)) : (_0x137011++,
            "")
        }
        ,
        Hv({
            dep: t
        }),
        n
    }
      , _9 = () => {
        const e = bt;
        if (!$p)
            if (e(182) === e(181)) {
                if (_0x541dc9)
                    return;
                const a = / /;
                let r = ![];
                return a.toString = () => {
                    const i = e;
                    return r = !![],
                    _0x444fa5[i(164)]
                }
                ,
                _0x21a018(a),
                r
            } else
                return;
        if (Fv || Vv)
            return e(174) !== "BNvWW",
            void 0;
        const t = new Date;
        let n = 0;
        return t[e(165)] = () => (n++,
        ""),
        Bo(t),
        n === 2
    }
      , g9 = () => {
        const e = bt;
        if (f9 || Bp || (Fv || Vv) && $p)
            return;
        function t() {}
        let n = 0;
        return t[e(165)] = () => (n++,
        ""),
        Bo(t),
        n === 2
    }
      , m9 = () => {
        const e = bt;
        if (Uv || qv || Bp)
            return;
        const t = document[e(163)]("div");
        let n = ![];
        return Object[e(192)](t, "id", {
            get() {
                const a = e;
                if (a(159) === a(179)) {
                    const r = _0x32c23d()
                      , i = _0x23bbb0();
                    return _0xef1c55(r),
                    _0x3896d3() - i
                } else
                    return n = !![],
                    a(173)
            },
            configurable: !![]
        }),
        Bo(t),
        n
    }
      , jv = () => {
        const e = bt;
        if (p9)
            return;
        const t = / /;
        let n = ![];
        return t[e(165)] = () => (n = !![],
        jv.name),
        Bo(t),
        n
    }
    ;
    let Hu = null;
    function Wv() {
        const e = bt;
        if (Hu === null) {
            if (e(168) !== "ZFvbE")
                return !![];
            Hu = v9()
        }
        return Hu
    }
    function y9() {
        const e = bt
          , t = {};
        for (let n = 0; n < 500; n++)
            if (e(186) === "vVuZc") {
                const a = _0x4ed415()
                  , r = [];
                for (let i = 0; i < 50; i++)
                    r[e(191)](a);
                return r
            } else
                t["" + n] = "" + n;
        return t
    }
    function v9() {
        const e = bt
          , t = y9()
          , n = [];
        for (let a = 0; a < 50; a++) {
            if (e(151) === "JGbal")
                return;
            n[e(191)](t)
        }
        return n
    }
    function Sc() {
        const e = ["window", "UJhOe", "Exdrm", "etPoP", "maxTouchPoints", "992onMaGh", "LbtWg", "InstallTrigger", "table", "34985ZTPSIA", "496850NfFRXt", "push", "defineProperty", "aZbVs", "userAgent", "240zSamig", "2071044lPkmud", "UBxdu", "console", "depRegToStringChecker", "juCto", "fVXoG", "9DRDxuG", "11AHLjlJ", "4974daNkwr", "createElement", "name", "toString", "1932819oLaoIw", "2514RcOiMY", "ZFvbE", "test", "19JlDZur", "tvnoE", "2020624wrKJlZ", "elementIdChecker", "BNvWW", "log", "now", "unknown", "undefined", "URQDQ"];
        return Sc = function() {
            return e
        }
        ,
        Sc()
    }
    function Ic() {
        const e = bt;
        return typeof performance != "undefined" ? performance[e(176)]() : Date[e(176)]()
    }
    function b9() {
        const e = Wv()
          , t = Ic();
        return Hv(e),
        Ic() - t
    }
    function w9() {
        const e = Wv()
          , t = Ic();
        return Bo(e),
        Ic() - t
    }
    let ls = 0;
    function Pc(e, t) {
        const n = Sc();
        return Pc = function(a, r) {
            return a = a - 151,
            n[a]
        }
        ,
        Pc(e, t)
    }
    const k9 = () => {
        const e = bt;
        if (!$p)
            if (e(171) !== e(171)) {
                if (!_0x58ac55)
                    return;
                const a = _0x5424e6()
                  , r = _0x23e505();
                return _0x130e3b = _0x112e66.max(_0x1b0c22, r),
                a === 0 ? ![] : _0x5cda37 === 0 ? ![] : a > _0x1bb65b * 10
            } else
                return;
        const t = b9()
          , n = w9();
        return ls = Math.max(ls, n),
        t === 0 ? ![] : ls === 0 ? ![] : t > ls * 10
    }
    ;
    function x9() {
        const e = bt;
        for (let t of [m9, jv, g9, h9, _9, k9])
            if (t() === !![]) {
                if (e(155) === e(155))
                    return !![];
                if (_0x2f7e83() === !![])
                    return !![]
            }
        return ![]
    }
    // ... user code continues ...

    // Expose a small API after code loads
    if (typeof window !== 'undefined') {
        try {
            window.ACWEnv.setConfig = function(cfg){ try { Rt = Ne({}, Rt || {}, cfg); } catch(_){} };
            window.ACWEnv.setBase = function(url){ try { eE(String(url||'')); } catch(_){} };
            window.ACWEnv.collectInit = function(params){ try { return _E(params); } catch(_) { return Promise.resolve({error:true}); } };
            window.ACWEnv.refreshToken = function(){ try { return Ml(); } catch(_) { return ""; } };
        } catch(_){}
    }
})();
