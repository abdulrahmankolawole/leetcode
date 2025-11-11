var searchMatrix = function(matrix, target) {
    function isInRange(val, array) {
        let i = 0
        let j = array.length - 1
        return array[i] <= val && val <= array[j]
    }

    function binarySearch(val, array) {
        let i = 0
        let j = array.length - 1

        while (i <= j) {
            let mid = Math.floor((i + j) / 2)
            if (array[mid] == val) return true
            else if (val < array[mid]) j = mid - 1
            else i = mid + 1
        }

        return false
    }

    let i = 0
    let j = matrix.length - 1

    while (i <= j) {
        let mid = Math.floor((i + j) / 2)
        if (isInRange(target, matrix[mid])) return binarySearch(target, matrix[mid])
        else if (target < matrix[mid][0]) j = mid - 1
        else i = mid + 1
    }

    return false
};