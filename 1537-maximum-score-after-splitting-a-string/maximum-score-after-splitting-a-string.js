var maxScore = function(s) {
    let zeroes = 0
    let ones = 0
    let output = 0

    for (let char of s) {
        if (char == "1") ones += 1
    }

    for (let i = 0; i < s.length - 1; i++) {
        let char = s[i]
        if (char == "1") ones -= 1
        else zeroes += 1
        score = zeroes + ones
        output = Math.max(output, score) 
    }

    return output
};