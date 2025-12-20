var findMaxAverage = function(nums, k) {
    let windowSum = 0
    let maxWindowSum = 0

    for (let i = 0; i < k; i++) {
        windowSum += nums[i]    
    }

    maxWindowSum = windowSum

    for (let i = k; i < nums.length; i++) {
        windowSum += nums[i] - nums[i - k]
        maxWindowSum = Math.max(maxWindowSum, windowSum)
    }

    return maxWindowSum / k

};