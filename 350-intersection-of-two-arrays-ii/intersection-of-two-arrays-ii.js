var intersect = function(nums1, nums2) {
    let lookup = {}
    let output = []

    for (let i = 0; i < nums1.length; i++) {
        let char = nums1[i]
        if (!(char in lookup)) lookup[char] = 0
        lookup[char] ++ 
    }

    for (let i = 0; i < nums2.length; i++) {
        let char = nums2[i]
        if (!lookup[char]) continue
        output.push(char)
        lookup[char] --
    }    
    return output
};