var countSubarrays = function(nums, k) {
    let maxNum = Math.max(...nums)  
    let countOfMaxNumber = 0
    let output = 0
    let i = 0
    let j = 0

    while (j < nums.length) {
        if (nums[j] == maxNum) {
            countOfMaxNumber += 1
        }

        while (countOfMaxNumber >= k) {
            output += nums.length - j
            if (nums[i] == maxNum) countOfMaxNumber -= 1
            i += 1
        }

        j += 1
    }
    return output

};