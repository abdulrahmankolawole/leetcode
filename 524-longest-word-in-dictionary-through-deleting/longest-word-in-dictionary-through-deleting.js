var findLongestWord = function(s, dictionary) {
    
    function isSubSeq(char, substr) {
        let i = 0
        let j = 0

        while (i < char.length) {
            if (char[i] == substr[j]) {
                i += 1
                j += 1
            }
            else i += 1
        }
        return j == substr.length
    } 

    let output = ""
    let maxLength = 0

    for (let word of dictionary) {
        if (isSubSeq(s, word)) {
            if (word.length > output.length) {
                output = word
            }
            else if (word.length == output.length) {
                output = output < word ? output : word
            }
        }
    }
    return output
};