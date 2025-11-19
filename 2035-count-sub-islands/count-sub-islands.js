var countSubIslands = function(grid1, grid2) {
    let rows = grid1.length
    let columns = grid2[0].length
    let count = 0

    function isValid(i, j) {
        if (i < 0 || j < 0 || i == rows || j == columns) {
            return false
        }
        return true
    }

    function traverse(i, j) {
        let isSub = true
        if (!isValid(i, j) || grid2[i][j] != 1) {
            return true
        }
        if (grid1[i][j] != 1) isSub = false
        grid2[i][j] = 0
        isSub = traverse(i - 1, j) && isSub
        isSub = traverse(i, j + 1) && isSub
        isSub = traverse(i + 1, j) && isSub 
        isSub = traverse(i, j - 1) && isSub
        return isSub
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = grid2[i][j]
            if (cell == 1) {
                if (traverse(i, j)) count += 1
            }
        }
    }

    return count
};