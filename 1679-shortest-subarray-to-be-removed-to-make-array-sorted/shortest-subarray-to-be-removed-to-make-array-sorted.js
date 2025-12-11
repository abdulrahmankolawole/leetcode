var findLengthOfShortestSubarray = function(arr) {
    let N = arr.length
    let r = N - 1
    let l = 0
    let output = N 

    while (r > 0 && arr[r - 1] <= arr[r]) r -= 1    
    while (l + 1 <= N && arr[l] <= arr[l + 1]) l += 1

    output = r
    if (l == N - 1) return 0
    output = Math.min(r, N - l - 1, output)


    let i = 0
    let j = r

    while (i <= l && j < N) {
        if (arr[i] <= arr[j]) {
            length = j - i - 1
            output = Math.min(output, length)
            i += 1
        }
        else {
            j ++
        }
    }

    return output
};