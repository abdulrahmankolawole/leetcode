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
        if (tLookup[t[i]] && tLookup[t[i]] != s[i]) return false
        tLookup[t[i]] = s[i]
    }

    return true
};