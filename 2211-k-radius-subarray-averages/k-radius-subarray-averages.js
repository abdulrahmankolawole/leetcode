var getAverages = function(nums, k) {
    let windowSize = (2 * k) + 1
    let output = new Array(nums.length)
    let windowSum = 0

    for (let i = 0; i < windowSize; i++) {
        windowSum += nums[i]
    }

    for (let i = 0; i < nums.length; i++) {
        if (i < k || i > nums.length- 1 - k) output[i] = -1
        else if (i == k) {
            output[i] = Math.trunc(windowSum / windowSize)
        }
        else {
            windowSum += nums[i + k] - nums[i - k - 1]
            output[i] = Math.trunc(windowSum / windowSize )
        } 
    }

    return output

    
};