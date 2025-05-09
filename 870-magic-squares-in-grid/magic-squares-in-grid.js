var numMagicSquaresInside = function(grid) {
    let rows = grid.length;
    let columns = grid[0].length;
    let output = 0;

    function magic(r, c) {
        // if elements in magic square are not distinct, return 0
        let lookup = new Set()
        // Check all 9 cells in the 3x3 grid
        for (let i = r; i < r + 3; i++) {
            for (let j = c; j < c + 3; j++) {
                let cell = grid[i][j];
                if (lookup.has(cell) || cell < 1 || cell > 9) {
                    return 0;
                }
                lookup.add(cell);
            }
        }

        // iterate through row
        for (let i = r; i < r + 3; i++) {
            let row_sum = 0
            for (let j = c; j < c + 3; j++) {
                row_sum += grid[i][j]
            }
            if (row_sum != 15) return 0
        }

        // Check sums of columns
        for (let j = c; j < c + 3; j++) {
            let column_sum = 0;
            for (let i = r; i < r + 3; i++) {
                column_sum += grid[i][j];
            }
            if (column_sum !== 15) return 0;
        }

        // iterate through diagonals
        if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 || grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15) return 0 

        return 1

    }

    // iterate through grid
    // if its a magic square
    // increment the result by 1
    for (let i = 0; i < rows - 2; i++) {
        for (let j = 0; j < columns - 2; j++) {
            output += magic(i, j)
        }
    }
    return output

};