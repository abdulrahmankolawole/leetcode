var numMagicSquaresInside = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    let count = 0

    function isMagic(row, col) {
        let lookup = new Set()

        for (let i = row; i < row + 3; i++) {
            for (let j = col; j < col + 3; j++) {
                let cell = grid[i][j]
                if (lookup.has(cell) || cell < 1 || cell > 9) return false
                lookup.add(cell)
            }
        }
        for (let i = row; i < row + 3; i++) {
            let row_sum = 0
            for (let j = col; j < col + 3; j++) {
                row_sum += grid[i][j]
            }
            if (row_sum != 15) return false
        }

        for (let j = col; j < col + 3; j++) {
            let col_sum = 0
            for (let i = row; i < row + 3; i++) {
                col_sum += grid[i][j]
            }
            if (col_sum != 15) return false
        }

        let primary_diag = 0
        primary_diag += grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]

        if (primary_diag != 15) return false


        let secondary_diag = 0
        secondary_diag += grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
        if (secondary_diag != 15) return false

        return true
    }

    for (let i = 0; i < rows - 2; i++) {
        for (let j = 0; j < columns - 2; j++) {
            if (isMagic(i, j)) {
                count += 1
            }
        }
    }

    return count
};