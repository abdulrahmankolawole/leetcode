class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        columns = len(colSum)
        matrix = [[0] * columns for _ in range(rows)]
        
        # validate the rowsum
        for i in range(rows):
            matrix[i][0] = rowSum[i]

        # validate the columns
        for j in range(columns):
            col_sum = 0
            for i in range(rows):
                col_sum += matrix[i][j]
            
            i = 0
            while (col_sum > colSum[j]):
                difference = col_sum - colSum[j]
                max_shift = min(matrix[i][j], difference)
                matrix[i][j + 1] += max_shift
                matrix[i][j] -= max_shift
                col_sum -= max_shift
                i += 1 

        return matrix

        