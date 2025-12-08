var threeSum = function(nums) {
    let lookup = new Set()
    let output = []
    nums.sort((a, b)=> a - b)

    for (let i = 0; i < nums.length - 2; i++) {
        let j = i + 1
        let k = nums.length - 1

        while (j < k) {
            let sum = nums[i] + nums[j] + nums[k]
            let triplets = nums[i] + "," + nums[j] + "," + nums[k]
            if (sum == 0) {
                if (!lookup.has(triplets)) {
                    lookup.add(triplets)
                    output.push([nums[i], nums[j], nums[k]])
                } 
                j ++
                k --
            } 
            else if (sum < 0) j ++
            else k --
        }
    }

    return output
};