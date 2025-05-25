var maxFrequency = function(nums, k) {
    nums = nums.sort((a, b)=> a - b)
    let i = 0
    let j = 0
    let output = 0
    let currentSum = 0

    while (j < nums.length) {
        currentSum += nums[j]

        while (nums[j] * (j - i + 1) > currentSum + k) {
            currentSum -= nums[i]
            i += 1
        }
        output = Math.max(j - i + 1, output)
        j +=1
    }
    return output
};