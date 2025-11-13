var snakesAndLadders = function(board) {
    let n = board.length
    let cells = new Array((n * n) + 1) 
    let label = 1

    for (let i = n - 1; i >= 0; i--) {
        if ((n - i) % 2 == 1) {
            for (j = 0; j < n; j++) {
                cells[label] = [i, j]
                label += 1
            }
        }
        else {
            for (j = n - 1; j >= 0; j--) {
                cells[label] = [i, j]
                label += 1
            }
        }
    }

    let min_moves = new Array((n * n) + 1).fill(-1)
    min_moves[1] = 0
    let queue = [1]
    while (queue.length) {
        let current = queue.shift()
        if (current === (n * n)) return min_moves[current]

        for (let next = current + 1; next <= Math.min(current + 6, (n * n)); next++) {
            let [i, j] = cells[next]
            let destination = next
            if (board[i][j] != -1) {
                destination = board[i][j]
            }

            if (min_moves[destination] == -1) {
                queue.push(destination)
                min_moves[destination] = min_moves[current] + 1
            }
        }
    }

    return -1



};