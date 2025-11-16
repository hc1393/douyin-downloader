import * as crypto from "node:crypto"
const CryptoJS = require("crypto-js");
var time='1761747228111'
/**
 * 获取a3
 * @returns
 */
function get_dfpId() {
    const dfp_timestamp = time
    const constant_str = "AOMEOAG"
    const env = { "platform": "Win32", "vendor": "Google Inc." }
    const envUint8Array = new TextEncoder().encode(JSON.stringify(env))
    // md5.md5算法可以在星球获取
    const gA = CryptoJS.MD5(envUint8Array)
    // 1736411131947AOMEOAGfd79fef3d01d5e9aadc18ccd4d0c9507
    return `${dfp_timestamp}${constant_str}${gA}`
}
console.log(get_dfpId())