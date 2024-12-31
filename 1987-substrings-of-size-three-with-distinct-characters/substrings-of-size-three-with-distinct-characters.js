var countGoodSubstrings = function (s) {
    let count = 0
    let lookup = {}
    let result = 0

    for (let i = 0; i < 3; i++) {
        let char = s[i]
        if (!lookup[char]) {
            count ++
            lookup[char] = 0
        }
        lookup[char] ++ 
    }
    
    if (count == 3) result ++
    for (let i = 3; i < s.length; i++) {
        let char = s[i]
        let prev = s[i - 3]
        if (lookup[prev] == 1) {
            count --
            delete lookup[prev]
        }
        else lookup[prev] --
        if (!lookup[char]) {
            lookup[char] = 0
            count ++
        } 
        lookup[char] ++
        if (count == 3) result ++
    }
    return result
};