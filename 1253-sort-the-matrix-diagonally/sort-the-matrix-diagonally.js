var diagonalSort = function(mat) {
    let lookup = {}
    let rows = mat.length
    let columns = mat[0].length

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = mat[i][j]
            let diagonal = (i - j)
            if (!(diagonal in lookup)) lookup[diagonal] = []
            lookup[diagonal].push(cell)
        }
    }    

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let diagonal = (i - j)
            lookup[diagonal].sort((a, b)=> b - a)
        }
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let diagonal = (i - j)
            mat[i][j] = lookup[diagonal].pop()
        }
    }

    return mat
};