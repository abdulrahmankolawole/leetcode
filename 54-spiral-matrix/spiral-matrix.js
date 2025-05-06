var spiralOrder = function(matrix) {
    let rows = matrix.length
    let columns = matrix[0].length
    let result = []
    let firstRow = 0
    let lastRow = rows - 1
    let firstColumn = 0
    let lastColumn = columns - 1

    while (result.length < (rows * columns)) {
        // travel from left to right
        for (let i = firstColumn; i <= lastColumn; i++) {
            result.push(matrix[firstRow][i])
        }
        firstRow += 1

        // travel from up to down
        for (let i = firstRow; i <= lastRow; i++) {
            result.push(matrix[i][lastColumn])
        }
        lastColumn -= 1

        if (firstRow <= lastRow) {
            // travel from right to left
            for (let i = lastColumn; i >= firstColumn; i--) {
                result.push(matrix[lastRow][i])
            }
            lastRow -= 1

        }

        if (firstColumn <= lastColumn) {
            // travel from down to up  
            for (let i = lastRow; i >= firstRow; i--) {
                result.push(matrix[i][firstColumn])
            }
            firstColumn += 1
        }

    }
    return result
};