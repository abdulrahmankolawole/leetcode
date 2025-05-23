var findRepeatedDnaSequences = function(s) {
    let output = []
    if (s.length < 10) return output
    let lookup = {}
    let j = 0

    while (j < s.length - 9) {
        let substr = s.slice(j, j + 10)
        
        if (!(substr in lookup)) lookup[substr] = 0
        lookup[substr] += 1
        if (lookup[substr] == 2) output.push(substr) 
        j += 1
    }
    return output


};