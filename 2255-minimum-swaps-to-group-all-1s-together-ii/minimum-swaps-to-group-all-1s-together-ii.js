var minSwaps = function(nums) {
    let totalOnes = 0
    let windowOnes = 0
    let maxWindowOnes = 0
    let i = 0
    let j = 0
    let n = nums.length

    for (let i = 0; i < n; i++) {
        if (nums[i] == 1) totalOnes += 1
    }

    while (j < 2 * n) {
        if (nums[j % n]) windowOnes += 1

        while (j - i + 1 > totalOnes) {
            if (nums[i % n]) windowOnes -= 1
            i +=1
        }
        
        maxWindowOnes = Math.max(maxWindowOnes, windowOnes)
        j += 1
    }

    return totalOnes - maxWindowOnes

};