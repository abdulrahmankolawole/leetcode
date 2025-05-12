var shortestBridge = function(grid) {
    let directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    let n = grid.length

    function isValid(i, j) {
        if (i < 0 || j < 0 || i == n || j == n) {
            return false
        }
        return true

    }

    let queue = []
    let mySet = new Set()
    
    function traverse(i, j) {
        if (!isValid(i, j) || grid[i][j] != 1) return 
        grid[i][j] = 0
        queue.push([i, j])
        traverse(i - 1, j) // up
        traverse(i, j + 1) // right
        traverse(i + 1, j) // down
        traverse(i, j - 1) // left
    }

    function bfs() {
        let bridge = 0
        while (queue.length) {
            let size = queue.length

            for (let i = 0; i < size; i++) {
                let [i, j] = queue.shift()


                for (let [x, y] of directions) {
                    new_x = x + i
                    new_y = y + j
                    if (isValid(new_x, new_y) && !mySet.has(new_x + ',' + new_y)) {
                        if (grid[new_x][new_y] == 1) return bridge
                        queue.push([new_x, new_y])
                        mySet.add(new_x + "," + new_y)
                    }
                }

            }
            bridge += 1
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            let cell = grid[i][j]
            if (cell == 1) {
                traverse(i, j)
                return bfs()
            }
        }
    }
};