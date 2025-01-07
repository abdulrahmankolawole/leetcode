var findMin = function(nums) {
    let i = 0
    let j = nums.length - 1
    if (nums[i] <= nums[j]) return nums[i]
    
    while (i <= j) {
        let mid = Math.floor((i + j) / 2)
        let leftOfMid = nums[mid - 1]
        let rightOfMid = nums[mid + 1]

        if (leftOfMid > nums[mid]) return nums[mid]
        if (nums[mid] > rightOfMid) return rightOfMid
        if (nums[i] <= nums[mid]) i = mid + 1
        else if (nums[mid] <= nums[j]) j = mid - 1
    }   

};