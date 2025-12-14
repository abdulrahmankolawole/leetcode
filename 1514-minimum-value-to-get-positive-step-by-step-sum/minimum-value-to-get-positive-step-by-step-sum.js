var minStartValue = function(nums) {
    let runningSum = 0
    let output = 0

    for (let num of nums) {
        runningSum += num
        output= Math.min(output, runningSum)
    }

    return 1 - output
};