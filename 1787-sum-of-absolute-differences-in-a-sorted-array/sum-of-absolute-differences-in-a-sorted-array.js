var getSumAbsoluteDifferences = function(nums) {
    let totalSum = nums.reduce((a, b)=> a + b, 0)
    let leftSum = 0
    let currentSum = 0
    let output = new Array(nums.length).fill(0)

    for (let i = 0; i < nums.length; i++) {
        let leftSize = i
        rightSize = nums.length - i - 1
        let rightSum = totalSum - leftSum - nums[i]
        output[i] = ((leftSize * nums[i]) - leftSum) + (rightSum - (rightSize * nums[i]))
        leftSum += nums[i]
    }

    return output
};