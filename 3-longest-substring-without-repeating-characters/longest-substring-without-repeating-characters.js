var lengthOfLongestSubstring = function(s) {
    let i = 0
    let j = 0
    let output = 0
    let lookup = {}

    while (j < s.length) {

        while (s[j] in lookup) {
            if (lookup[s[i]] == 1) delete lookup[s[i]]
            else lookup[s[i]] -= 1
            i += 1
        }

        if (!(s[j] in lookup)) lookup[s[j]] = 0
        lookup[s[j]] += 1
        output = Math.max(output, j - i + 1)
        j += 1
    }   
    return output
};