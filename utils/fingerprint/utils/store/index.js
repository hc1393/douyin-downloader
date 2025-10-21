define("utils/fingerprint/utils/store/index.js", function(require, module, exports, window, document, frames, self, location, navigator, localStorage, history, Caches, screen, alert, confirm, prompt, XMLHttpRequest, WebSocket, Reporter, webkit, WeixinJSCore) {
    "use strict";
    require("../../../../@babel/runtime/helpers/Arrayincludes");
    var e = require("./storage.js")
      , r = require("./memory.js")
      , t = require("./uni.store.js")
      , n = [e.useStorage(r.memory, "memory"), e.useStorage(t.uniStore, "uniStore")]
      , o = "function" == typeof btoa ? "__".concat(btoa("@#$%^&"), "__") : "__QCMkJV4m__"
      , c = {
        get: function(e) {
            for (var r = 0, t = n; r < t.length; r++) {
                var c = t[r].read("".concat(o).concat(e));
                if (null != c)
                    try {
                        return JSON.parse(c)
                    } catch (e) {
                        return c
                    }
            }
        },
        set: function(e, r) {
            var t = "string" == typeof r ? r : JSON.stringify(r);
            n.forEach((function(n) {
                n.write("".concat(o).concat(e), t)
            }
            ))
        },
        remove: function(e) {
            n.forEach((function(r) {
                r.remove("".concat(o).concat(e))
            }
            ))
        },
        clear: function() {
            n.forEach((function(e) {
                e.clear()
            }
            ))
        }
    };
    module.exports = c;
});