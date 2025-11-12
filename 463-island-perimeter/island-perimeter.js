var islandPerimeter = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    let perimeter = 0

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = grid[i][j]
            if (cell == 1) {
                perimeter += 4
                if (j > 0 && grid[i][j - 1] == 1) perimeter -= 2
                if (i > 0 && grid[i - 1][j] == 1) perimeter -= 2
            }   
        }
    }  

    return perimeter
};