// p.parse function implementation
function parse(v) {
    for (var k = v.length, S = [], P = 0; P < k; P++)
        S[P >>> 2] |= (v.charCodeAt(P) & 255) << 24 - P % 4 * 8;
    return new _.init(S, k);
}

// Example usage:
// var result = parse("your string here");