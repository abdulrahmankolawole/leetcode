var diStringMatch = function(s) {
    let i = 0
    let j = s.length
    let output = new Array()

    for (let char of s) {
        if (char == "I") {
            output.push(i)
            i += 1
        }
        else {
            output.push(j)
            j -= 1
        }
    }

    output.push(i)
    return output
};