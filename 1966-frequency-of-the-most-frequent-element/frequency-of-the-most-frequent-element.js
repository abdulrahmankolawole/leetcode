var maxFrequency = function(nums, k) {
    nums.sort((a, b)=> a - b)
    let i = 0
    let j = 0
    let runningSum = 0
    let output = 0

    while (j < nums.length) {
        runningSum += nums[j]

        while (nums[j] * (j - i + 1) > runningSum + k) {
            runningSum -= nums[i]
            i += 1
        }

        output = Math.max(output, (j - i + 1))
        j += 1
    }

    return output

};