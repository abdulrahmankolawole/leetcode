var orangesRotting = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    let fresh = 0
    let queue = []

    function isValid(i, j) {
        if (i < 0 || j < 0 || i == rows || j == columns) {
            return false
        }
        return true
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            cell = grid[i][j]
            if (cell == 0) continue
            if (cell == 1) fresh += 1
            else queue.push([i, j])
        }
    }
    let directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    let minutes = 0
    while (queue.length && fresh > 0) {
        let size = queue.length

        for (let k = 0; k < size; k++) {
            let [i, j] = queue.shift()
            
            for (let [x, y] of directions) {
                let row = i + x
                let col = j + y

                if (!isValid(row, col) || grid[row][col] != 1) continue
                grid[row][col] = 2
                fresh -= 1
                queue.push([row, col])
            }
        }
        minutes += 1
    }

    return fresh == 0 ? minutes : -1


};