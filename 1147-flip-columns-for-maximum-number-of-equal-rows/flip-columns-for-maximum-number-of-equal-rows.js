var maxEqualRowsAfterFlips = function(matrix) {
    let lookup = {}
    let result = 0

    for (let row of matrix) {
        let key = ""
        if (!row[0]) {
            for (let num of row) {
                key += num ? 0 : 1
            }
        }
        else {
            for (let num of row) key += num
        }
        if (!(key in lookup)) lookup[key] = 0
        lookup[key] += 1
        result = Math.max(result, lookup[key])

    }    
    return result
};