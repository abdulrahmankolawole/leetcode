var getSumAbsoluteDifferences = function(nums) {
    let total = nums.reduce((a, b)=> a + b, 0)
    let output = new Array(nums.length).fill(0)
    let leftSum = 0

    for (let i = 0; i < nums.length; i++) {
        let leftSize = i
        let rightSize = nums.length - leftSize - 1
        rightSum = total - leftSum - nums[i]
        output[i] = ((leftSize * nums[i]) - leftSum) + (rightSum - (nums[i] * rightSize)) 
        leftSum += nums[i]
    }
    return output  
};