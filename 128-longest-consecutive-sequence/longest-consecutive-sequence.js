var longestConsecutive = function(nums) {
    let lookup = new Set(nums)
    let output = 0

    for (let num of lookup) {

        if (!(lookup.has(num - 1))) {
            let streak = 1

            while (lookup.has(num + 1)) {
                num += 1
                streak += 1
            }

            output = Math.max(output, streak)
        }
    }    

    return output
};