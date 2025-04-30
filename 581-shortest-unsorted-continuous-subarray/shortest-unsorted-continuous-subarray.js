var findUnsortedSubarray = function(nums) {
    let sorted = [...nums].sort((a, b)=> a - b)
    i = 0
    j = nums.length - 1

    while (i < nums.length) {
        if (nums[i] != sorted[i]) break
        i += 1
    }    

    while (j >= 0) {
        if (nums[j] != sorted[j]) break
        j -= 1
    }

    if (i == nums.length) return 0

    return j - i + 1
};