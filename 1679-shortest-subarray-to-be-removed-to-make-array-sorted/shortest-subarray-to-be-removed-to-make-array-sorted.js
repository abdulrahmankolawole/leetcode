var findLengthOfShortestSubarray = function(arr) {
    let N = arr.length;
    let l = 0
    let r = N - 1;

    // remove prefix
    while (r > 0 && arr[r - 1] <= arr[r]) {
        r -= 1
    }
    let res = r

    // remove postfix
    while (l + 1 < N && arr[l] <= arr[l + 1]) {
        l += 1
    }
    // If the entire array is already sorted
    if (l === N - 1) return 0;
    res = Math.min(res, N -l - 1, r)



    // Step 4: Use two pointers to find the smallest middle part to remove
    let i = 0, j = r;
    while (i <= l && j < N) {
        if (arr[i] <= arr[j]) {
            res = Math.min(res, j - i - 1);
            i++;
        } else {
            j++;
        }
    }
    return res
};