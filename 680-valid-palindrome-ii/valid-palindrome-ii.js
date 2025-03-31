var validPalindrome = function(s) {
    let i = 0
    let j = s.length - 1

    function isPalindrome(word) {
        i = 0
        j = word.length - 1

        while (i < j) {
            if (word[i] != word[j]) return false
            i += 1
            j -= 1
        }
        return true
    }   

    while (i <= j) {
        if (s[i] != s[j]) {
            word1 = s.slice(0, i) + s.slice(i + 1)
            word2 = s.slice(0, j) + s.slice(j + 1)
            if (!isPalindrome(word1) && !isPalindrome(word2)) return false
        }
        i += 1
        j -= 1
    }
    return true

};