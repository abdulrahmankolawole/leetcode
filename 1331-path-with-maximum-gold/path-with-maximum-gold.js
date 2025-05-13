var getMaximumGold = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    let max_amount = 0

    function traverse(i, j) {
        let amount = 0
        if (i < 0 || j < 0 || i == rows || j == columns || grid[i][j] == 0 ) return 0
        let temp = grid[i][j]
        grid[i][j] = 0
        amount = Math.max(amount, temp + traverse(i - 1, j))
        amount = Math.max(amount, temp + traverse(i, j + 1))
        amount = Math.max(amount, temp + traverse(i + 1, j))
        amount = Math.max(amount, temp + traverse(i, j - 1))
        grid[i][j] = temp
        return amount
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            max_amount = Math.max(max_amount, traverse(i, j))
        }
    }    

    return max_amount


};