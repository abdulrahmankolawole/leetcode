var findClosestElements = function(arr, k, x) {
    let i = 0
    let j = arr.length - k

    while (i < j) {
        let mid = Math.floor((i + j) / 2)
        if (x - arr[mid] > arr[mid + k] - x) {
            i = mid + 1
        }
        else j = mid
    }

    return arr.slice(i, i + k)
};