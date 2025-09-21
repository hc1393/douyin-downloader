import CryptoJS from "crypto-js"

const crypto = require('crypto');
function loadPage(pageNumber) {
    const timestamp = Date.now();
    const hash = crypto.createHash('md5');
    hash.update("tuling" + timestamp + pageNumber);
    const token = hash.digest('hex');
    a='https://www.mashangpa.com/api/problem-detail/4/data/?page='+pageNumber+'&sign='+token.toString()+'&_ts='+timestamp
    return a
}

let dd = {'a': CryptoJS};
const _0x38addf = _0x66a7;
function _0x66a7(_0x7461a9, _0x14ffcc) {
    const _0x4f0d09 = _0x4f0d();
    return _0x66a7 = function (_0x66a780, _0x2abc15) {
        _0x66a780 = _0x66a780 - 0xc5;
        let _0x477d8f = _0x4f0d09[_0x66a780];
        return _0x477d8f;
    }, _0x66a7(_0x7461a9, _0x14ffcc);
}
function _0x4f0d() {
    const _0x341c37 = ['2440720SaQcQw', 'jo8j9wGw%6HbxfFn', '9735516pjwmiO', '68862pbatqQ', 'mode', 'AES', '1923264HnviQd', '36906bPsIrd', '12hEJHOd', 'enc', 'pad', 'encrypt', 'Hex', 'Utf8', '689460JbShaf', 'parse', '957060HmuxSn', 'toString', '445UZKyxv'];
    _0x4f0d = function () {
        return _0x341c37;
    };
    return _0x4f0d();
}
function _0x66a7(_0x7461a9, _0x14ffcc) {
    const _0x4f0d09 = _0x4f0d();
    return _0x66a7 = function (_0x66a780, _0x2abc15) {
        _0x66a780 = _0x66a780 - 0xc5;
        let _0x477d8f = _0x4f0d09[_0x66a780];
        return _0x477d8f;
    }, _0x66a7(_0x7461a9, _0x14ffcc);
}

let key, iv;
['a']=CryptoJS;
key = dd['a'][_0x38addf(0xd6)][_0x38addf(0xc7)][_0x38addf(0xc9)](_0x38addf(0xce));
iv = dd['a'][_0x38addf(0xd6)]['Utf8'][_0x38addf(0xc9)]('0123456789ABCDEF');
function encrypt(_0x277028) {
    const _0x4d843e = _0x38addf;
    let _0x2703a2 = dd['a'][_0x4d843e(0xd6)]['Utf8']['parse'](_0x277028),
        _0x50fcf0 = dd['a'][_0x4d843e(0xd2)][_0x4d843e(0xc5)](_0x2703a2, key, {
            'mode': dd['a'][_0x4d843e(0xd1)]['CBC'],
            'padding': dd['a'][_0x4d843e(0xd7)]['Pkcs7'],
            'iv': iv
        });
    return _0x50fcf0['ciphertext'][_0x4d843e(0xcb)](Crypto[_0x4d843e(0xd6)][_0x4d843e(0xc6)]);
}

function loadPage(pageNumber) {
    var csrfTokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
    const timestamp = new Date().getTime();
    const params = {
        page: pageNumber,
        _ts: timestamp,
    };
    const jsonString = JSON.stringify(params);
    let encryptedQuery = encrypt(jsonString);
    fetch(`/api/problem-detail/${problemId}/data/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({xl: encryptedQuery})
    })
        .then(response => response.json())
        .then(data => updatePageContent(data))
        .catch(error => console.error('Error fetching problem details:', error));
}
console.log(loadPage('1'))