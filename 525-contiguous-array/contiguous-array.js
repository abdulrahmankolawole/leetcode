var findMaxLength = function(nums) {
    let runningSum = 0
    let output = 0
    let lookup = {0: -1}
    let count = 0

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 1) count += 1
        else count -= 1
        if (!(count in lookup)) lookup[count] = i
        else {
            output = Math.max(output, i - lookup[count])
        }
    }   
    return output

};