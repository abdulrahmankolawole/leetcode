var equalSubstring = function(s, t, maxCost) {
    let currentCost = 0
    let output = 0
    let i = 0
    let j = 0

    while (j < s.length) {

        currentCost += Math.abs(s[j].charCodeAt(0) - t[j].charCodeAt(0))

        while (currentCost > maxCost) {
            currentCost -= Math.abs(s[i].charCodeAt(0) - t[i].charCodeAt(0))
            i += 1
        }

        output = Math.max(output, j - i + 1)
        j +=1
    }   

    return output 
};