var searchRange = function(nums, target) {
    let first = leftBS(nums, target)
    let last = rightBS(nums, target)

    function leftBS(arr, val) {
        let i = 0
        let j = arr.length - 1
        let output = -1

        while (i <= j) {
            let mid = Math.floor((i + j) / 2)
            if (arr[mid] == val) {
                output = mid
                j = mid -1
            }
            else if (arr[mid] > val) j = mid - 1
            else i = mid + 1
        }

        return output
    }

    function rightBS(arr, val) {
        let i = 0
        let j = arr.length - 1
        output = -1

        while (i <= j) {
            let mid = Math.floor((i + j) / 2)
            if (arr[mid] == val) {
                output = mid
                i = mid + 1
            }
            else if (arr[mid] < val) i = mid + 1
            else j = mid - 1
        }

        return output
    }

    return [first, last]
};