var numberOfSubstrings = function(s) {

    let lookup = {}

    function containsAllThree() {
        return (lookup["a"] > 0 && lookup["b"] > 0 && lookup["c"] > 0)
    }

    let i = 0
    let j = 0
    let output = 0
    
    while (j < s.length) {
        if (!(s[j] in lookup)) lookup[s[j]] = 0
        lookup[s[j]] += 1

        while (containsAllThree()) {
            output += s.length - j
            lookup[s[i]] -= 1
            i += 1
        }
        j +=1 
    }

    return output


};