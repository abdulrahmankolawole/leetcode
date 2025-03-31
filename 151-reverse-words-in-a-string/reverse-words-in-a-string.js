var reverseWords = function(s) {
    s = s.trim().split(" ").filter((word) => !!(word))
    i = 0
    j = s.length - 1

    while (i < j) {
        [s[i], s[j]] = [s[j], s[i]]
        i += 1
        j -= 1
    }   

    return s.join(" ") 
};