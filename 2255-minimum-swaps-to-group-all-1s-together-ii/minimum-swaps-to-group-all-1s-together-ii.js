var minSwaps = function(nums) {
    let countOfOnes = 0
    let k = nums.length

    for (let num of nums) {
        countOfOnes += num
    }
    
    let i = 0
    let j = 0
    let maxWindowOnes = 0
    let windowOnes = 0

    while (j < nums.length * 2) {
        if (nums[j % k]) windowOnes += 1

        while (j - i + 1 > countOfOnes) {
            if (nums[i % k]) windowOnes -= 1
            i += 1
        }
        maxWindowOnes = Math.max(maxWindowOnes, windowOnes)
        j += 1 
    }
    return countOfOnes - maxWindowOnes

};