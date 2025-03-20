var hasValidPath = function(grid) {
    const rows = grid.length;
    const columns = grid[0].length;
    const queue = [[0, 0]]; // Start from the top-left corner
    const up = {};
    const right = {};
    const down = {};
    const left = {};
    let lookup = new Set();

    [2, 5, 6].forEach(x => {
        up[x] = new Set([2, 3, 4]);
    });

    [1, 4, 6].forEach(x => {
        right[x] = new Set([1, 3, 5]);
    });

    [2, 3, 4].forEach(x => {
        down[x] = new Set([2, 5, 6]);
    });

    [1, 3, 5].forEach(x => {
        left[x] = new Set([1, 4, 6]);
    });

    const directions = [[-1, 0, up], [0, 1, right], [1, 0, down], [0, -1, left]];

    function isValid(dr, dc, i, j, direction) {
        if ((dr < 0 || dc < 0) || (dr == rows || dc == columns) || lookup.has(dr + ',' + dc)) return false;
        let street = grid[i][j];
        let path = grid[dr][dc]
        if (!(street in direction) || !(direction[street].has(path))) return false;
        return true;
    }

    while (queue.length) {
        let [i, j] = queue.shift();

        if ((i === rows - 1) && (j === columns - 1)) return true;

        for (let [dr, dc, direction] of directions) {
            let newX = dr + i;
            let newY = dc + j;

            if (isValid(newX, newY, i, j, direction)) {
                queue.push([newX, newY]);
                lookup.add(newX + "," + newY);
            }
        }
    }

    return false;
};