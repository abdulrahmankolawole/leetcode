var numberOfSubarrays = function(nums, k) {
    for (let i = 0; i < nums.length; i++) {
        if (isOdd(nums[i])) nums[i] = 1
        else nums[i] = 0
    }

    function isOdd(num) {
        return num % 2 !== 0
    }
    let currentSum = 0
    let lookup = {0: 1}
    let output = 0

    for (let i = 0; i < nums.length; i++) {
        currentSum += nums[i]

        if ((currentSum - k) in lookup) {
            output += lookup[currentSum - k]
        }
        if (!(currentSum in lookup)) lookup[currentSum] = 0
        lookup[currentSum] += 1
    }
    return output

};