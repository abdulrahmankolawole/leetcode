var checkSubarraySum = function(nums, k) {
    let lookup = new Set()
    let runningSum = 0
    let prevRem = 0

    for (let num of nums) {
        runningSum += num
        let remainder = runningSum % k
        if (lookup.has(remainder) )return true
        lookup.add(prevRem)
        prevRem = remainder
        
    }
    return false
};