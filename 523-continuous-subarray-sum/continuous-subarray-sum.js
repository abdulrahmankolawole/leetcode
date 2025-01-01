var checkSubarraySum = function(nums, k) {
    let lookup = {0: - 1}
    let total = 0

    for (let i = 0; i < nums.length; i++) {
        total += nums[i]
        remainder = total % k
    
        if (!(remainder in lookup)) {
            lookup[remainder] = i
        } 
        else if (i - lookup[remainder] > 1) return true
        
        // lookup[remainder] = i
    }

    return false

};