var checkSubarraySum = function(nums, k) {
    let lookup = {0: -1}
    let runningSum = 0
    let output = 0

    for (let i = 0; i < nums.length; i++) {
        runningSum += nums[i]
        let remainder = ((runningSum % k) + k) % k
        if (!(remainder in lookup)) lookup[remainder] = i
        else {
            let length = i - lookup[remainder]
            if (length > 1) {
                return true
            }
        }
    }
    return false
};