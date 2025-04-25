var checkSubarraySum = function(nums, k) {
    let lookup = {}
    lookup = {0: -1}
    let currentSum = 0

    for (let i = 0; i < nums.length; i++) {
        currentSum += nums[i]
        // currentRem = currentSum % k
        currentRem = ((currentSum % k) + k) % k
        if (!(currentRem in lookup)) lookup[currentRem] = i
        else if (i - lookup[currentRem] >= 2) return true
    }

    return false
};