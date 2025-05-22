/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function(n) {
    let steps = 0

    while (n > steps) {
        steps += 1
        n -= steps
    }
    // 5 - 1 = 4
    // 4 - 2 = 2
    // 2- 3 = - 1
    return steps 
};