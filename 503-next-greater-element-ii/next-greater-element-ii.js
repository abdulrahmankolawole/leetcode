var nextGreaterElements = function(nums) {
    let result = new Array(nums.length).fill(-1)
    let stack = []
    let length = nums.length

    for (let i = (length * 2) - 1; i >= 0; i--) {
        let char = nums[i % length]
        if (!stack.length) {
            stack.push(char)
            continue
        }
        while (stack.length && char >= stack.at(-1)) {
            stack.pop()
        }
        if (stack.length) {
            result[i % length] = stack.at(-1)
        }
        stack.push(char)
    }   
    return result

};