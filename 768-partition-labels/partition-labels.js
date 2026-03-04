var partitionLabels = function(s) {
    let lookup = {}

    for (let i = 0; i < s.length; i++) {
        lookup[s[i]] = i
    }

    let size = 1
    let end = 0
    let output = []
    for (let i = 0; i < s.length; i++) {
        end = Math.max(end, lookup[s[i]])
        if (i == end) {
            output.push(size)
            size = 0
        }
        size += 1
    }

    return output
};