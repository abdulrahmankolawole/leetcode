var divideArray = function(nums) {
    let lookup = {}

    for (let num of nums) {
        if (!(num in lookup)) lookup[num] = 0
        lookup[num] += 1
    }    

    for (let num of nums) {
        if (lookup[num] % 2 != 0) return false
    }

    return true
};