/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
    let directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    let rows = board.length
    let columns = board[0].length

    function isValid(i, j) {
        if (i < 0 || j < 0 || i == rows || j == columns) return false
        if (board[i][j] < 1) return false
        return true
    }

    function countNeigbors(i, j) {
        let count = 0
        for (let [x, y] of directions) {
            new_x = x + i
            new_y = j + y
            if (isValid(new_x, new_y)) {
                count += 1
            }
        }
        return count
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = board[i][j]
            let count = countNeigbors(i, j)
            if (cell == 1) {
                if (!(count == 2 || count == 3)) {
                    board[i][j] = 2
                }

            }
            else if (cell == 0) {
                if (count == 3) {
                    board[i][j] = -1
                }
            }
        }
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = board[i][j]
            if (cell == 2) board[i][j] = 0
            else if (cell == -1) board[i][j] = 1 
        }
    }

};