var minimumLength = function(s) {
    let i = 0
    let j = s.length - 1

    while (i < j && s[i] == s[j]) {
        let char = s[i]
        while (i <= j && s[i] == char) i += 1
        while (i <= j && s[j] == char) j -= 1
    }    
    return j - i + 1
};