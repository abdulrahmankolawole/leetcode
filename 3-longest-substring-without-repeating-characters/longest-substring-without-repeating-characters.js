var lengthOfLongestSubstring = function(s) {
    let i = 0
    let j = 0
    let maxLength = 0
    let lookup = new Set()

    while (j < s.length) {

        while (lookup.has(s[j])) {
            lookup.delete(s[i])
            i += 1
        }

        lookup.add(s[j])
        maxLength = Math.max(maxLength, j - i + 1)
        j += 1
    }   

    return maxLength


};