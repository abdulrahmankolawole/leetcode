var pivotIndex = function(nums) {
    let totalSum = nums.reduce((a, b)=> a + b, 0)
    let leftSum = 0

    for (let i = 0; i < nums.length; i++) {
        let rightSum = totalSum - leftSum - nums[i]
        if (leftSum == rightSum) return i
        leftSum += nums[i]
    }
    
    return -1
};