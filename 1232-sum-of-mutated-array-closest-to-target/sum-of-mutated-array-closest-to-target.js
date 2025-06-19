var findBestValue = function(arr, target) {
    let i = 0
    let j = Math.max(...arr)
    let minDiff = Infinity
    let result = 1

    function addSum(mid) {
        let sum = 0
        for (let val of arr) sum += val > mid ? mid: val
        return sum
    }

    while (i <= j) {
        let mid = Math.floor((i + j) / 2)
        let sum = addSum(mid)
        if (sum == target) return mid
        if (sum < target) i = mid + 1
        else j = mid - 1
        diff = Math.abs(target - sum)
        // if (diff < minDiff || diff == minDiff) {
        //     result = mid;
        //     minDiff = diff;
        // }
        if (diff < minDiff || diff == minDiff && mid < result) {
            result = mid;
            minDiff = diff;
        }
    }
    return result
};