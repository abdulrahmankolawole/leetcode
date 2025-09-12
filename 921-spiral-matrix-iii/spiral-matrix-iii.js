var spiralMatrixIII = function(rows, cols, rStart, cStart) {
    let size = rows * cols
    let result = []
    let i = rStart
    let j = cStart
    let steps = 1
    let directions = [[0, 1], [1,0], [0, -1], [-1, 0]]
    let k = 0

    function isValid(row, col) {
        if (row < 0 || col < 0 || row >= rows || col >= cols) return false
        return true
    }

    while (result.length < size) {
        for (let a = 0; a < 2; a++) {
            let [x, y] = directions[k]
            for (let step = 0; step < steps; step++) {
                if (isValid(i, j)) {
                    result.push([i, j])
                }
                i = i + x
                j = j + y
            }
            k = (k + 1) % 4
        }
        steps += 1
    }

    return result
};