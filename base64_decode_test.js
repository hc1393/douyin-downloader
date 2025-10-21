// Base64 decode function
function base64Decode(encodedString) {
    return decodeURIComponent(atob(encodedString).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
}

// Base64 encoded string you provided
var encodedString = "ZWViZTYzMjAzYWFhYWYzNTE5ODE5Yzg2ZDExOTAxOTQyNDMzZWRiNjljNDhjNTQ4NjI2Yjc5Y2JmMWY4NjI0YTpjZGRhY2Q0OTAzYmNiYzZiZDZkOGJiNmEwZDQ0OTYxY2EzNGY5MWJmMmVkMTEyZDQzMDBiNDBlZGE1NjkxYWY3YjNmOWFlY2ZjNmQ2MTYyYTg4MmZjODMwOGViNDk1MWUwNWIxOGNmNjMxOGZkMWQ2MzVjMTBhMjJlMjc1OGY1NTc1Y2JlYmEwNzE5NzlkNjk1YzMyNjFjYzVkZWUyYTFlMWU5ODU2ODI0MTQ2MjU5MjkwMjY0MzdlOTFiNjNiYzY6MTc2MDg3NTQ1NTcwMQ==";

// Decode the string
var decodedString = base64Decode(encodedString);

console.log("Encoded string:", encodedString);
console.log("Decoded string:", decodedString);

// Word array class - _.init implementation
var _ = {
    init: function(v, k) {
        v = this.words = v || [];
        k != undefined ? this.sigBytes = k : this.sigBytes = v.length * 4;
    }
};

// Parse function implementation
var p = {
    parse: function(v) {
        for (var k = v.length, S = [], P = 0; P < k; P++)
            S[P >>> 2] |= (v.charCodeAt(P) & 255) << 24 - P % 4 * 8;
        return new _.init(S, k);
    }
};

// Function f that processes string with encoding
function f(v) {
    return p.parse(unescape(encodeURIComponent(v)));
}

// Test with the decoded string
var result = f(decodedString);
console.log("Parsed result:", result);
console.log("Words:", result.words);
console.log("Signature bytes:", result.sigBytes);