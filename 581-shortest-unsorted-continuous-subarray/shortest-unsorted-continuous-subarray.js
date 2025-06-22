var findUnsortedSubarray = function(nums) {
    let i = 0
    let j = nums.length - 1
    let sorted = [...nums].sort((a, b)=> a - b)

    while (i <= j && nums[i] == sorted[i]) i += 1
    while (i <= j && nums[j] == sorted[j]) j -= 1
    console.log(i, j)

    return j - i + 1    
};