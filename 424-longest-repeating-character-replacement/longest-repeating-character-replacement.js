var characterReplacement = function(s, k) {
    let mostFreq = 0
    let lookup = {}
    let i = 0
    let j = 0
    let output = 0

    while (j < s.length) {
        let char = s[j]
        if (!(char in lookup)) {
            lookup[char] = 0
        }
        lookup[char] += 1
        mostFreq = Math.max(mostFreq, lookup[char])

        while (j - i + 1 - mostFreq > k) {
            lookup[s[i]] -= 1
            i += 1
        }
        output = Math.max(output, j - i + 1)
        j ++ 
    }

    return output
        
};