var partitionLabels = function(s) {
    let size = 0
    let result = []
    let end = 0
    let lookup = {}

    for (let i = 0; i < s.length; i++) {
        lookup[s[i]] = i
    }

    for (let i = 0; i < s.length; i++) {
        size += 1
        end = Math.max(end, lookup[s[i]])
        if (i == end) {
            result.push(size)
            size = 0
        } 
    }   

    return result
};