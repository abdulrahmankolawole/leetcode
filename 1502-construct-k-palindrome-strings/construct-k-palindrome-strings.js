var canConstruct = function(s, k) {
    let lookup = {}
    let odds = 0

    if (s.length < k) return false

    for (let char of s) {
        if (!(char in lookup)) lookup[char] = 0
        lookup[char] += 1
    }    

    for (let [char, count] of Object.entries(lookup)) {
        if (count % 2 != 0) odds += 1
    }

    return odds <= k
};