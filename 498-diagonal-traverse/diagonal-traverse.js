var findDiagonalOrder = function(mat) {
    let rows = mat.length
    let columns = mat[0].length
    let goingUp = true
    let output = []
    let size = rows * columns
    let i = 0
    let j = 0

    while (output.length < size) {

        if (goingUp) {

            while (i >= 0 && j < columns) {
                output.push(mat[i][j])
                i -= 1
                j += 1
            }
            if (j == columns) {
                i += 2
                j -= 1
            }
            else i += 1
            goingUp = false

        }
        else {
            while (j >= 0 && i < rows) {
                output.push(mat[i][j])
                i += 1
                j -= 1
            }
            if (i == rows) {
                i -= 1
                j += 2
            }
            else j += 1
            goingUp = true
        }
    }
    return output
};