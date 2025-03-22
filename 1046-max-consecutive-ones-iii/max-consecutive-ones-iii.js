var longestOnes = function(nums, k) {
    let output = 0
    let i = 0
    let j = 0
    let flippedZeroes = 0

    while (j < nums.length) {

        if (nums[j] == 0) flippedZeroes += 1

        while (flippedZeroes > k) {
            if (nums[i] != 1) flippedZeroes -=1
            i += 1
        }

        output = Math.max(output, j - i + 1)
        j += 1
    }

    return output
};