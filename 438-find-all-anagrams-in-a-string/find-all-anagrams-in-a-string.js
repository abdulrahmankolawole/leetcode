var findAnagrams = function(s, p) {
    let size = p.length
    let lookup1 = {}

    for (let char of p) {
        if (!(char in lookup1)) lookup1[char] = 0
        lookup1[char] += 1
    }

    let lookup2 = {}

    for (let k = 0; k < size; k++) {
        if (!(s[k] in lookup2)) lookup2[s[k]] = 0
        lookup2[s[k]] += 1
    }

    let j = size
    let output = []
    if (_.isEqual(lookup1, lookup2)) output.push(0)

    while (j < s.length) {
        if (!(s[j] in lookup2)) lookup2[s[j]] = 0
        lookup2[s[j]] += 1

        if (lookup2[s[j - size]] == 1) {
            delete lookup2[s[j - size]]
        } 
        else lookup2[s[j - size]] -= 1

        if (_.isEqual(lookup1, lookup2)) {
            output.push(j - size + 1)
        } 
        j += 1
    }

    return output
};