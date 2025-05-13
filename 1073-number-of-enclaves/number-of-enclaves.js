var numEnclaves = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    let count = 0

    function traverse(i, j) {
        if (i < 0 || j < 0 || i == rows || j == columns || grid[i][j] != 1) return
        grid[i][j] = 0
        traverse(i - 1, j) //up
        traverse(i, j + 1) //right
        traverse(i + 1, j) //down
        traverse(i, j - 1) //left
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            cell = grid[i][j]
            if (cell == 1) {
                if (i == 0 || j == 0 || i == rows - 1 || j == columns - 1) {
                    traverse(i, j)
                }
            }
        }
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            cell = grid[i][j]
            if (cell == 1) count += 1
        }
    }
    return count
};