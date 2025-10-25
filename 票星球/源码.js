let Ee;
const wn = new Array(128).fill(void 0);

wn.push(void 0, null, !0, !1);
function qe(e) {
    return wn[e];
}
function Ze(e) {
    Pr === wn.length && wn.push(wn.length + 1);
    const t = Pr;
    return Pr = wn[t],
    wn[t] = e,
    t
}
function aa9065fa9dc5df96(t, a, n) {
        const r = qe(t).subarray(a >>> 0, n >>> 0);
        return Ze(r)
    }
// 创建一个包含 subarray 方法的对象放在数组中用于测试

ee = {t: 132, a: 0, n: 16};
console.log(wn)
console.log(qe(132))
console.log(aa9065fa9dc5df96(ee));