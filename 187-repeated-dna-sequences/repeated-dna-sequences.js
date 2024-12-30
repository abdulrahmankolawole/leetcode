var findRepeatedDnaSequences = function(s) {
    let lookup = {}
    let i = 0
    let j = 0
    let output = []

    while (j < s.length - 9) {
        let substring = s.substring(j, j + 10)

        if (!(substring in lookup)) lookup[substring] = 0
        lookup[substring] += 1   

        if (lookup[substring] == 2) {
            output.push(substring)
        }
        j += 1
    }
    return output
};