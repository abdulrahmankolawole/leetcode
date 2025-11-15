var countNegatives = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    let count = 0

    for (let j = columns - 1; j >= 0; j--) {
        for (let i = rows - 1; i >= 0; i--) {
            let cell = grid[i][j]
            if (cell >= 0) break
            count += 1
        }
    }    

    return count
};