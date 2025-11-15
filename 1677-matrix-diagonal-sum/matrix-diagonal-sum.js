var diagonalSum = function(mat) {
    let rows = mat.length
    let columns = mat[0].length
    let lookup = new Set()
    let output = 0

    function isOnPrimaryDiagonal(i, j) {
        return i == j
    }    

    function isOnSecondaryDiagonal(i, j) {
        return (i + j) == columns - 1
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let diagonal = i + "," + j
            if ((isOnPrimaryDiagonal(i, j) || isOnSecondaryDiagonal(i, j)) && !(lookup.has(diagonal))) output += mat[i][j]
            lookup.add(diagonal)
        }
    }

    return output
};