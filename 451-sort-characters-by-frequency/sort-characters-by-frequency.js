var frequencySort = function(s) {
    let lookup = {}

    for (let char of s) {
        if (!(char in lookup)) lookup[char] = 0
        lookup[char] += 1
    }    

    let array = []
    

    for (let [key, value] of Object.entries(lookup)) {
        array.push([key, value])
    }

    array.sort((a, b)=> b[1] - a[1])
    let output = ""
    for (let [key, value] of array) {
       output += key.repeat(value)
    }

    return output
};