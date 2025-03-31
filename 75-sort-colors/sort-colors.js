var sortColors = function(nums) {
    let i = 0
    let mid = 0
    let j = nums.length - 1

    while (mid <= j) {
        if (nums[mid] == 0) {
            [nums[i], nums[mid]] = [nums[mid], nums[i]]
            i += 1
            mid += 1
        }
        else if (nums[mid] == 2) {
            [nums[mid], nums[j]] = [nums[j], nums[mid]]
            j -= 1
        }
        else mid += 1
    }  
};