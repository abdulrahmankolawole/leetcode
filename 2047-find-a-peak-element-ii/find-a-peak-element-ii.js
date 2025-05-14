var findPeakGrid = function(mat) {
    let i = 0
    let rows = mat.length 
    let j = 0
    let columns = mat[0].length 

    while (j < columns && i < rows) {
        if (i > 0 && mat[i][j] < mat[i - 1][j]) i -= 1
        else if (j < columns - 1 && mat[i][j] < mat[i][j + 1]) j += 1
        else if (i < rows - 1 && mat[i][j] < mat[i + 1][j]) i += 1
        else if (j > 0 && mat[i][j] < mat[i][j - 1]) j -= 1
        else return [i, j]
    }

};