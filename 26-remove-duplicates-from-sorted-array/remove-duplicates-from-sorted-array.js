var removeDuplicates = function(nums) {
    k = 0

    for (let i = 1; i < nums.length; i++) {
        if (nums[k] != nums[i]) {
            k += 1
            nums[k] = nums[i]
        }
    }   
    return k + 1


};