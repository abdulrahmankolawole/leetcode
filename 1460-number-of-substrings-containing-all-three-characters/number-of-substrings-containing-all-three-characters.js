var numberOfSubstrings = function(s) {
    let lookup = {}

    function containsAllThree() {
        if (!("a" in lookup) || !("b" in lookup) || !("c" in lookup)) return false
        return lookup["a"] > 0 && lookup["b"] > 0 && lookup["c"] > 0
    }    

    let i = 0
    let j = 0
    let output = 0

    while (j < s.length) {
        let char = s[j]
        if (!(char in lookup)) lookup[char] = 0
        lookup[char] += 1

        while (containsAllThree()) {
            lookup[s[i]] -= 1
            i += 1
            output += s.length - j
        }
        j += 1
    }

    return output
};