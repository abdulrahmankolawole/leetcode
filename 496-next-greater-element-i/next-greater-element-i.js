var nextGreaterElement = function(nums1, nums2) {
    let lookup = {}
    let stack = []
    let result = new Array(nums1.length).fill(-1)

    for (let i = 0; i < nums1.length; i++) {
        let char = nums1[i]
        lookup[char] = i
    }    

    for (let i = nums2.length - 1; i >= 0; i--) {
        let char = nums2[i]

        if (!stack.length) {
            stack.push(char)
        }

        while (stack.length && char >= stack.at(-1)) {
            stack.pop()
        }
        if (stack.length) {
            if (char in lookup) {
                index = lookup[char]
                result[index] = stack.at(-1)
            }

        }
        stack.push(char)
      
    }
    return result
};