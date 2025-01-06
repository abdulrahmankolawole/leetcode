// use bs
// if the mid squared is equal to the target return the mid value
// else if the mid value squared is greater than the target value, reduce search space less
// else if the mid value squared is less than the target search right

var mySqrt = function(x) {
    let i = 0
    let j = x
    res = 0

    while (i <= j) {
        let mid = Math.floor((i + j) / 2)
        let squared = mid**2
        if ((squared) == x) return mid
        else if (squared > x) j = mid - 1
        else {
            i = mid + 1
            res = mid
        } 
        
    }

    return res
};