var isSubsequence = function(s, t) {
    let i = 0
    let j = 0

    while (j < t.length) {
        if (s[i] == t[j]) i += 1
        j += 1
    }   

    return i == s.length 
};