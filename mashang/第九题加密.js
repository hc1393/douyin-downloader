const CryptoJS = require('crypto-js')
var time=Date.now()
var testData = {e: "xxxooo", t: '9527'+time}
const cryptojsHmacSHA1 = CryptoJS.HmacSHA1(testData.t, testData.e);
function get_m(){
    a=btoa(''+time)
    return [cryptojsHmacSHA1.toString(CryptoJS.enc.Hex), a]
}

console.log(get_m())