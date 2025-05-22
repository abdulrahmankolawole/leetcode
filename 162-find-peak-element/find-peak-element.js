var findPeakElement = function(nums) {
    let i = 0
    let j = nums.length - 1

    while (i <= j) {
        let mid = Math.floor((i + j) / 2)

        if (mid > 0 && nums[mid] < nums[mid - 1]) j = mid - 1
        else if (mid + 1 < nums.length && nums[mid] < nums[mid + 1]) i = mid + 1
        else return mid

    }    

    return -1
};