// var g_word = ""
//   , status_hub = []
//   , status_hub_count = 0
//   , g_id = -1
//   , hsp_arr = window.location.hostname.split(".")
//   , hs_base = "." + hsp_arr[hsp_arr.length - 2] + "." + hsp_arr[hsp_arr.length - 1]
//   , g_hostname_arr = ["www" + hs_base, "www2.jiumodiary.com", "www5.jiumodiary.com"];
// var window={}
// var g_word = ""
//   , status_hub = []
//   , status_hub_count = 0
//   , g_id = -1
//   , hsp_arr = window.location.hostname.split(".")
//   , hs_base = "." + hsp_arr[hsp_arr.length - 2] + "." + hsp_arr[hsp_arr.length - 1]
//   , g_hostname_arr = ["www" + hs_base, "www2.jiumodiary.com", "www5.jiumodiary.com"];
function ajax_fetch_hub(a, e) {
    for (var l = !1, t = [], n = 0; n < g_hostname_arr.length; n++) {
        var r = g_hostname_arr[n];
        t[r] = new XMLHttpRequest,
        t[r].onreadystatechange = function(o, i) {
            return function() {
                var e, t, n, r;
                4 === i.readyState && 200 === i.status && (l ? c_log("abandant ajax " + o) : (l = !0,
                g_id === a && (n = i.responseText,
                e = (r = JSON.parse(n)).status,
                t = r.status_extra,
                n = r.log,
                status_hub_count = parseInt(r.count),
                r = r.sources,
                c_log(e + ": " + n + ", new_count:" + status_hub_count),
                "succeed" === e && (status_hub = status_hub.concat(r),
                "completed" !== t && ajax_fetch_hub(a, status_hub_count)),
                render(t))))
            }
        }(r, t[r]),
        t[r].open("POST", "https://" + r + "/ajax_fetch_hubs.php", !0),
        t[r].setRequestHeader("Content-type", "application/x-www-form-urlencoded"),
        t[r].setRequestHeader("X-Requested-With", "XMLHttpRequest"),
        t[r].send("id=" + encodeURIComponent(a) + "&set=" + encodeURIComponent(e)),
        c_log("ajax request : " + r + ", id=" + encodeURIComponent(a) + "&set=" + encodeURIComponent(e))
    }
}
function init_fetch_hub(e) {
    for (var t = (new Date).getTime(), o = !1, n = [], r = 0; r < g_hostname_arr.length; r++) {
        var i = g_hostname_arr[r];
        n[i] = new XMLHttpRequest,
        n[i].onreadystatechange = function(n, r) {
            return function() {
                if (4 === r.readyState && 200 === r.status)
                    if (o)
                        c_log("abandant init " + n);
                    else {
                        o = !0;
                        var e = r.responseText
                          , t = JSON.parse(e)
                          , e = t.status;
                        if ("succeed" !== e)
                            return hide_loading(),
                            "exceed" === e ? void exceed_alert() : "tooshort" === e ? void tooshort_alert() : void notfound_alert();
                        status_hub = t.sources,
                        status_hub_count = parseInt(t.count),
                        c_log("g_id received: " + (g_id = t.id)),
                        ajax_fetch_hub(g_id, status_hub_count),
                        render("more")
                    }
            }
        }(i, n[i]),
        n[i].open("POST", "https://" + i + "/init_hubs.php", !0),
        n[i].setRequestHeader("Content-type", "application/x-www-form-urlencoded"),
        n[i].setRequestHeader("X-Requested-With", "XMLHttpRequest"),
        n[i].send("q=" + encodeURIComponent(e) + "&remote_ip=" + g_ip + "&time_int=" + t),
        c_log("init request : " + i + ",  q=" + encodeURIComponent(e) + "&remote_ip=" + g_ip + "&time_int=" + t)
    }
}
var e='偏微分'
// console.log(init_fetch_hub(e))

console.log(encodeURIComponent(e))