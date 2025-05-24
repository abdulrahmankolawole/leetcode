var minimumDifference = function(nums, k) {
    nums = nums.sort((a, b) => a - b)
    let i = 0
    let j = k - 1
    let output = Infinity

    while (j < nums.length) {
        diff = nums[j] - nums[i]
        output = Math.min(output, diff)
        i +=1
        j += 1
    }
    return output
};