var equalSubstring = function(s, t, maxCost) {
    let i = 0
    let j = 0
    let currentCost = 0
    let output = 0

    while (j < s.length) {
        currentCost += Math.abs(s[j].charCodeAt(0) - t[j].charCodeAt(0))

        while (currentCost > maxCost) {
            currentCost -= Math.abs(s[i].charCodeAt(0) - t[i].charCodeAt(0))
            i += 1
        }

        output = Math.max(output, j - i + 1)
        j ++
    }

    return output
};