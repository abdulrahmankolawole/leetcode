var transpose = function(matrix) {
    let rows = matrix.length
    let columns = matrix[0].length
    let output = Array.from({length: columns}, ()=> new Array(rows))

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            output[j][i] = matrix[i][j]
        }
    }

    return output
};