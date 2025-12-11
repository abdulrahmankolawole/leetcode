var findLongestWord = function(s, dictionary) {

    dictionary.sort((a, b)=> b.length == a.length ? a.toLowerCase().localeCompare(b.toLowerCase()) : b.length - a.length)
    
    function isSubseq(s, t) {
        let i = 0
        let j = 0

        while (j < t.length) {
            if (s[i] == t[j]) i += 1
            j += 1
        }   

        return i == s.length
    };

    let output = ""

    for (let word of dictionary) {
        if (isSubseq(word, s)) return word
    }
    return output
};