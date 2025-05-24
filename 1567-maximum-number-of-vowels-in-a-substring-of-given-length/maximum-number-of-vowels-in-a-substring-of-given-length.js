var maxVowels = function(s, k) {
    let output = 0
    let lookup = new Set("aeiou".split(""))

    function isVowel(char) {
        return lookup.has(char)
    }    

    let count = 0
    for (let i = 0; i < k; i++) {
        let char = s[i]
        if (isVowel(char)) count += 1
    }

    output = count

    for (let i = k; i < s.length; i++) {
        let char = s[i]
        let prev = s[i - k]
        if (isVowel(prev)) count -=1
        if (isVowel(char)) count += 1
        output = Math.max(output, count)
    }
    return output
};