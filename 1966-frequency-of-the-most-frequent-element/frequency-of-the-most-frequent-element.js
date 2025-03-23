var maxFrequency = function(nums, k) {
    nums = nums.sort((a, b) => a - b)   
    let i = 0
    let j = 0
    let total = 0
    let output = 0

    while (j < nums.length) {
        total += nums[j]

        while (nums[j] * (j - i + 1) > total + k) {
            total -= nums[i]
            i += 1
        }

        output = Math.max(output, j - i + 1)
        j += 1
    }

    return output
};