var minSubarray = function(nums, p) {
    let total = nums.reduce((a, b)=> a + b, 0)
    if (total % p == 0) return 0
    let totalRemainder = total % p
    let lookup = {0: -1}
    let minLength = nums.length
    let currSum = 0

    for (let i = 0; i < nums.length; i++) {
        currSum += nums[i]
        let currRemainder = currSum % p

        targetRemainder = ((currRemainder - totalRemainder) + p) % p
        if (targetRemainder in lookup) {
            minLength = Math.min(minLength, i - lookup[targetRemainder])
        }
        lookup[currRemainder] = i

    }
    return minLength == nums.length ? -1 : minLength

};