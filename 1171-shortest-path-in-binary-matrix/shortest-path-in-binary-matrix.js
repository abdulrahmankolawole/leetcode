var shortestPathBinaryMatrix = function(grid) {
    let n = grid.length
    let mySet = new Set()
    let directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]];
    if (grid[0][0] !== 0 || grid[n - 1][n - 1] !== 0) return -1;



    function isValid(i, j) {
        if (i < 0 || j < 0 || i== n || j == n || grid[i][j] == 1) return false
        return true
    }

    let queue = [[0, 0]]
    let distance = 1
    while (queue.length) {
        let size = queue.length

        for (let i = 0; i < size; i++) {
            
            let [i, j] = queue.shift()
            if (i == n - 1 && j == n-1) return distance
            for (let [x, y] of directions) {
                let new_x = x + i
                let new_y = y + j

                if (isValid(new_x, new_y)) {
                    queue.push([new_x, new_y])
                    grid[new_x][new_y] = 1
                }
            }

        }
        distance += 1
    }

    return -1

};