var sortArrayByParity = function(nums) {
    
    function isOdd(num) {
        return num % 2 != 0
    }

    i = 0
    j = nums.length - 1

    while (i < j) {
        if (!isOdd(nums[i])) i += 1
        else if (isOdd(nums[j])) j -= 1
        else {
            [nums[i], nums[j]] = [nums[j], nums[i]]
            i += 1
            j -= 1
        }
    }   

    return nums 
};