var shortestBridge = function(grid) {
    let n = grid.length
    let directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    function isValid(i, j) {
        if (i < 0 || j < 0 || i == n || j == n) return false
        return true
    }

    let queue = []
    let lookup = new Set()

    function traverse(i, j) {
        if (!isValid(i, j) || grid[i][j] != 1) return
        queue.push([i, j])
        grid[i][j] = 0
        traverse(i - 1, j)
        traverse(i, j + 1)
        traverse(i + 1, j)
        traverse(i, j - 1)
    }

    function bfs() {
        let bridge = 0
        while (queue.length) {
            let size = queue.length

            for (let i = 0; i < size; i++) {
                let [i, j] = queue.shift()

                for (let [x, y] of directions) {
                    let new_x = x + i
                    let new_y = y + j

                    if (isValid(new_x, new_y) && !lookup.has(new_x + "," + new_y)) {
                        if (grid[new_x][new_y] == 1) return bridge
                        queue.push([new_x, new_y])
                        lookup.add(new_x + "," + new_y)
                    }

                }
            }
            bridge += 1
        }
        return bridge
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