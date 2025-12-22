var numberOfAlternatingGroups = function(colors, k) {
    let N = colors.length
    let output = 0
    let i = 0
    let j = 1

    while (j < N + k - 1) {
        if (colors[j % N] == colors[(j - 1) % N]) i = j
        while (j - i + 1 > k) i += 1

        if (j - i + 1 == k) output += 1
        j += 1
    }   

    return output

};