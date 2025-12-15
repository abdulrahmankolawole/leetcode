var maxFreq = function(s, maxLetters, minSize, maxSize) {
    let output = 0
    let j = 0
    let lookup = {}

    function noUniqueChars(string) {
        let lookup = new Set(string)
        return lookup.size
    }
    
    while (j <= s.length - minSize) {
        let substr = s.slice(j, j + minSize)
        if (noUniqueChars(substr) <= maxLetters) {
            if (!(substr in lookup)) lookup[substr] = 0
            lookup[substr] += 1
            output = Math.max(lookup[substr], output)
        }
        j += 1
    }

    return output
};