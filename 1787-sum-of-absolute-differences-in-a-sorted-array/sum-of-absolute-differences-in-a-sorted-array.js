var getSumAbsoluteDifferences = function(nums) {
    let total = nums.reduce((a, b)=> a + b, 0)
    let leftSum = 0
    let size = nums.length
    let result = new Array(nums.length)

    for (let i = 0; i < size; i++) {
        rightSum = total - nums[i] - leftSum
        let leftSize = i
        let rightSize = size - i - 1
        let abs = ((leftSize * nums[i]) - leftSum) + (rightSum - (rightSize * nums[i]))
        result[i] = abs

        sum = rightSum + leftSum
        leftSum += nums[i]
    }    
    return result
};