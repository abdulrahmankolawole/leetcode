var spiralMatrixIII = function(rows, cols, rStart, cStart) {
    let size = rows * cols
    let result = new Array()   
    let i = rStart
    let j = cStart 
    let steps = 1
    let directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    let k = 0

    function isValid(i, j) {
        if (i < 0 || j < 0 || i >= rows || j >= cols) return false
        return true
    }

    while (result.length < size) {
        for (let a = 0; a < 2; a++) {
            let [x, y] = directions[k]
            for (let b = 0; b < steps; b++) {
                if (isValid(i, j)) {
                    result.push([i, j])
                }
                i = x + i
                j = y + j
            }
            k = (k + 1) % 4
        }
        steps +=1
    } 

    return result
};