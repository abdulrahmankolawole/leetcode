var findErrorNums = function(nums) {
    let k = 1
    let lookup = new Set(nums)
    let counter = {}
    let n = nums.length
    let missing

    for (let num of nums) {
        if (!(num in counter)) counter[num] = 0
        counter[num] += 1
    }

    for (let i = 1; i <= n; i++) {
        if (!(k in counter)) missing = k
        if (counter[i] == 2) duplicate = i
        k += 1
    }

    return [duplicate, missing]
};