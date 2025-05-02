/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    // x = x.toLowerCaxe().replace(/[^a-z0-9]/g, "")
    x = x.toString()
    let i = 0
    let j = x.length - 1

    while (i < j) {
        if (x[i] != x[j]) return false
        i++
        j--
    }
    return true
};
