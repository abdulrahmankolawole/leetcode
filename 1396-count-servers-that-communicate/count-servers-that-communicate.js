var countServers = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    let rowCount = {}
    let columnCount = {}
    let count = 0

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = grid[i][j]
            if (cell) {
                if (!rowCount[i]) rowCount[i] = 0
                rowCount[i] ++
                if (!columnCount[j]) columnCount[j] = 0
                columnCount[j] ++
            }
        }
    }    

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = grid[i][j]
            if (cell) {
                if (rowCount[i] > 1 || columnCount[j] > 1) count += 1
            }
        }
    }    
    return count


};