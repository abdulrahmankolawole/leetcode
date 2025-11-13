class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        def is_diagonal_univalue(i, j):
            val = matrix[i][j]
            while (i < rows and j < columns):
                if (matrix[i][j] != val):
                    return False
                i += 1
                j += 1
            
            return True

        for j in range(columns):
            if (not is_diagonal_univalue(0, j)):
                return False
        
        for i in range(1, rows):
            if (not is_diagonal_univalue(i, 0)):
                return False

        return True

