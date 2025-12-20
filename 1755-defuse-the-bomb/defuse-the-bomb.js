var decrypt = function(code, k) {
    let N = code.length
    let output = new Array(N).fill(0)
    if (k == 0) return output
    let i = 0
    let j = 0
    let currentSum = 0

    while (j < N + Math.abs(k)) {
        currentSum += code[j % N]

        if (j - i + 1 > Math.abs(k)) {
            currentSum -= code[i % N]
            i = (i + 1) % N
        }
        if (j - i + 1 == Math.abs(k)) {
            if (k > 0) {
                output[((i - 1 + N)) % N] = currentSum
            }
            else if (k < 0) {
                output[(j + 1) % N] = currentSum
            }
        }
        j +=1
    }

    return output
};