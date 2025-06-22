var partitionLabels = function(s) {
    let lookup = {}

    for (let i = 0; i < s.length; i++) {
        let char = s[i]
        lookup[char] = i
    }    

    let lastIdx = 0
    let size = 0
    let output = []

    for (let i = 0; i < s.length; i++) {
        size += 1
        let char = s[i]
        lastIdx = Math.max(lastIdx, lookup[char])
        if (lastIdx == i) {
            output.push(size)
            size = 0
        }
    }
    return output
};