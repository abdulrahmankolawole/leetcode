var maximumUniqueSubarray = function(nums) {
    let lookup = new Set()
    let i = 0
    let j = 0
    let output = 0
    let currentSum = 0

    while (j < nums.length) {
        let num = nums[j]
        currentSum += nums[j]

        while (lookup.has(nums[j])) {
            lookup.delete(nums[i])
            currentSum -= nums[i]
            i += 1
        }

        lookup.add(num)
        output = Math.max(output, currentSum)
        j += 1
    }

    return output
};