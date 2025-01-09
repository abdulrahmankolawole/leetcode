var threeSum = function(nums) {
    nums = nums.sort((a, b)=> a - b)
    let lookup = new Set()
    let target = 0
    let output = []

    for (let i = 0; i < nums.length - 2; i++) {
        a = i + 1
        b = nums.length - 1

        while (a < b) {
            sum = nums[i] + nums[a] + nums[b]
            if (sum == target) {
                triplet = nums[i] + ',' + nums[a] + ',' + nums[b]
                if (!lookup.has(triplet)) {
                    lookup.add(triplet)
                    output.push([nums[i], nums[a], nums[b]])
                }
                a += 1
                b -= 1
            }
            else if (sum < target) a +=1
            else b -= 1
        }
    }  
    
    return output
};