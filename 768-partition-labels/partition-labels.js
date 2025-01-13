// iterate through the string
// use a hash table to store the occurence of the last index of each letter
// iterate through the string

var partitionLabels = function(s) {
    let lookup = {}
    let start = 0
    let end = 0
    let result = []

    for (let i = 0; i < s.length; i++) {
        let char = s[i]
        lookup[char] = i
    }

    for (let i = 0; i < s.length; i++) {
        end = Math.max(end, lookup[s[i]])
        if (i == end) {
            result.push(end - start + 1)
            start = end + 1
        }
    }   

    return result


};