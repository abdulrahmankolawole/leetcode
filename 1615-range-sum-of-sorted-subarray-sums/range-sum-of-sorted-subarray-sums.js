var rangeSum = function(nums, n, left, right) {
    let subarraySums = []
    let modulo = (10 ** 9) + 7

    for (let i = 0; i < nums.length; i++) {
        for (let j = i; j < nums.length; j++) {
            let subarray = nums.slice(i, j + 1)
            let sum = subarray.reduce((a, b)=> a + b, 0)
            subarraySums.push(sum)
        }
    }    
    subarraySums.sort((a, b)=> a - b)
    
    let sum = 0
    for (let i = left - 1; i < right; i++) {
        sum += subarraySums[i]
    }

    return sum % modulo
};