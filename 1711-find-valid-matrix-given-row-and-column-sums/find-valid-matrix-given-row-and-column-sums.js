var restoreMatrix = function(rowSum, colSum) {
    let rows = rowSum.length
    let columns = colSum.length 
    let matrix = Array.from({ length: rows }, () => new Array(columns).fill(0));
    let currColSum = 0

    for (let i = 0; i < rows; i++) {
        matrix[i][0] = rowSum[i]
    }  

    for (let j = 0; j < columns; j++) {
        currColSum = 0

        for (let i = 0; i < rows; i++) {
            currColSum += matrix[i][j]
        }

        let i = 0
        while (currColSum > colSum[j]) {
            let diff = currColSum - colSum[j]
            let maxShift = Math.min(diff, matrix[i][j])
            matrix[i][j + 1] += maxShift
            matrix[i][j] -= maxShift
            currColSum -= maxShift
            i += 1
        }
    }  

    return matrix


};