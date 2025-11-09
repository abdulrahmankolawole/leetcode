var isIsomorphic = function(s, t) {
    let sLookup = {}
    let tLookup = {}
    if (s.length !== t.length) return false

    for (let i = 0; i < s.length; i++) {
        let char = s[i]
        if (char in sLookup && sLookup[char] != t[i]) return false
        sLookup[char] = t[i]
    }

    for (let i = 0; i < t.length; i++) {
        let char = t[i]
        if (char in tLookup && tLookup[char] != s[i]) return false
        tLookup[char] = s[i]
    }

    return true
};