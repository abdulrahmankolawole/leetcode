var numberOfSubstrings = function(s) {
    let lookup = {}
    let i = 0
    let j = 0
    let output = 0

    function containsAllThree() {
        if (!lookup["a"] || !lookup["b"] || !lookup["c"]) return false
        return true
    }

    while (j < s.length) {
        if (!(s[j] in lookup)) lookup[s[j]] = 0
        lookup[s[j]] += 1

        while (containsAllThree()) {
            output += s.length - j
            lookup[s[i]] -= 1
            i += 1
        }


        j += 1
    }

    return output


};