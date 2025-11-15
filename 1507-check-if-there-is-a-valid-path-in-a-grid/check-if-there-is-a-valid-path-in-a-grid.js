var hasValidPath = function(grid) {
    let rows = grid.length;
    let columns = grid[0].length;
    let queue = [[0, 0]];
    let up = {};
    let right = {};
    let down = {};
    let left = {};
    let lookup = new Set();

    [2, 5, 6].forEach(x=> {up[x] = new Set([2, 3, 4])});
    [1, 4, 6].forEach(x=>{ right[x] = new Set([1, 3, 5])});
    [2, 3, 4].forEach(x=> {down[x] = new Set([2, 5, 6])});
    [1, 3, 5].forEach(x=> {left[x] = new Set([1, 4, 6])});
    let directions = [[-1, 0, up], [0, 1, right], [1, 0, down], [0, -1, left]];

    function isValid(new_x, new_y, i, j, direction) {
        if (new_x < 0 || new_y < 0 || new_x == rows || new_y == columns) return false
        let street = grid[i][j]
        let path = grid[new_x][new_y]

        if (!(street in direction) || !(direction[street].has(path))) return false
        return true
    }

    while (queue.length) {
        let [i, j] = queue.shift()
        if (i == rows - 1 && j == columns - 1) return true

        for (let [x, y, direction] of directions) {
            let new_x = x + i
            let new_y = y + j

            if (isValid(new_x, new_y, i, j, direction) && !lookup.has(new_x + "," + new_y)) {
                queue.push([new_x, new_y])
                lookup.add(new_x + "," + new_y)
            }
        }
    }

    return false



};