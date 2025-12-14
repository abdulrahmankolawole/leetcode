var findMaxLength = function(nums) {
    let count = 0
    let maxLength = 0
    let lookup = {0: -1}

    for (let i = 0; i < nums.length; i++) {
        let num = nums[i]
        if (num == 0) count -= 1
        else if (num == 1) count += 1
        if (!(count in lookup)) lookup[count] = i
        else {
            let length = i - lookup[count]
            maxLength = Math.max(maxLength, length)
        }
    }   
    return maxLength

};