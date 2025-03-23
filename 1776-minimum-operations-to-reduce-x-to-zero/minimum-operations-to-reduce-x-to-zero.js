var minOperations = function(nums, x) {
    let totalSum = nums.reduce((a, b)=> a + b)
    let target = totalSum - x
    let i = 0
    let j = 0
    let output = - 1
    let currentSum = 0

    while (j < nums.length) {
        currentSum += nums[j]

        while (currentSum > target && i <= j) {
            currentSum -= nums[i]
            i += 1
        }

        if (currentSum == target) {
            output = Math.max(output, j - i + 1)
        }


        j += 1
    }
    return output == -1 ? -1 : nums.length - output
};