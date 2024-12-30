var maxFreq = function(s, maxLetters, minSize, maxSize) {
    let j = 0
    let maxFreq = 0
    let lookup = {}

    function countUnique(string) {
        let mySet = new Set(string.split(""))
        return mySet.size
    }

    while (j <= s.length - minSize) {
        let substring = s.slice(j, j + minSize)

        if ((countUnique(substring) <= maxLetters)) {
            if (!(substring in lookup)) lookup[substring] = 0
            lookup[substring] += 1
            maxFreq = Math.max(maxFreq, lookup[substring])
        }
        j += 1
    }   
    return maxFreq
};