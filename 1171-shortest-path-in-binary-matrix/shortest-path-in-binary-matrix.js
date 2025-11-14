var shortestPathBinaryMatrix = function(grid) {
    let n = grid.length
    let directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    let queue = [[0, 0]]
    if (grid[0][0] !== 0 || grid[n - 1][n - 1] !== 0) return -1;
    let path = 1

    function isValid(i, j) {
        if (i < 0 || j < 0 || i == n || j == n) return false
        return true
    }

    while (queue.length) {
        let size = queue.length

        for (let k = 0; k < size; k++) {
            let [i, j] = queue.shift()
            if (i == n - 1 && j == n - 1) return path

            for (let [x, y] of directions) {
                let new_x = x + i
                let new_y = y + j

                if (isValid(new_x, new_y) && grid[new_x][new_y] == 0) {
                    grid[new_x][new_y] = 1
                    queue.push([new_x, new_y])
                }
            }
        }
        path += 1
    }

    return -1
};