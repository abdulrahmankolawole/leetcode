var maxScore = function(s) {
    let zeroes = 0
    let ones = 0
    let maxScore = 0

    for (let char of s) {
        num = parseInt(char)
        if (num) ones += 1
    }    

    for (let i = 0; i < s.length - 1; i++) {
        let char = s[i]
        if (char == "0") zeroes += 1
        else ones -= 1
        let score = zeroes + ones
        maxScore = Math.max(score, maxScore)
    }

    return maxScore
};