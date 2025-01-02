var minStartValue = function(nums) {
    let minSum = Infinity
    let curSum = 0

    for (let num of nums){
        curSum += num
        minSum = Math.min(minSum, curSum)
    }

    return 1 - Math.min(minSum, 0)
};