var frequencySort = function(s) {
    let lookup = {}
    let bucket = {}

    for (let char of s) {
        if (!(char in lookup)) lookup[char] = 0
        lookup[char] += 1
    }        

    for (let [char, count] of Object.entries(lookup)) {
        if (!(count in bucket)) bucket[count] = []
        bucket[count].push(char)
    }

    let output = ""
    for (let count = s.length; count >= 1; count--) {
        if (count in bucket) {
            let chars = bucket[count]
            for (let char of chars) output += char.repeat(count)
        }
    }

    return output
};