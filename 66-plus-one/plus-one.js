var plusOne = function(digits) {
    let size = digits.length 
    let result = new Array(size + 1).fill(0)

    for (let i = size - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i] += 1
            return digits
        }
        else {
            digits[i] = 0
        }
    }
    
    result[0] = 1
    return result
};