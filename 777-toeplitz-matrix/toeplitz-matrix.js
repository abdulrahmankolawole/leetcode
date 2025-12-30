var isToeplitzMatrix = function(matrix) {
    let rows = matrix.length
    let columns = matrix[0].length

    function isDiagonalUnivalue(i, j) {
        let cell = matrix[i][j]
        row = i
        column = j
        while (row < rows && column < columns) {
            if (matrix[row][column] != cell) return false
            row += 1
            column += 1
        }
        return true
    }    

    for (let j = 0; j < columns; j++) {
        if (!isDiagonalUnivalue(0, j)) return false
    }

    for (let i = 1; i < rows; i++) {
        if (!isDiagonalUnivalue(i, 0)) return false
    }

    return true
};