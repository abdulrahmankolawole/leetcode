var gameOfLife = function(board) {

    let rows = board.length
    let columns = board[0].length
    let directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    function isValid(i, j) {
        if (i < 0 || j < 0 || i == rows || j == columns) return false
        return true
    }

    function countNeighbors(i, j) {
        let count = 0

        for (let [x, y] of directions) {
            new_x = x + i
            new_y = y + j

            if (isValid(new_x, new_y)) {
                if(board[new_x][new_y] >= 1) count += 1
            }

        }
        return count
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            cell = board[i][j]
            if (cell == 1) {
                count = countNeighbors(i, j)
                if (!(count == 2 || count == 3)) {
                    board[i][j] = 2
                }
            }

            if (cell == 0) {
                count = countNeighbors(i, j)
                if (count == 3) {
                    board[i][j] = -1
                }
            }
        }
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = board[i][j]
            if (cell == 2) {
                board[i][j] = 0
            }

            else if (cell == -1) {
                board[i][j] = 1
            
            }
        }
    }



    
};