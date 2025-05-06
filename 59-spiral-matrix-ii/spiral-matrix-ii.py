class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(n)]
        start = 1
        end = (n * n)
        first_row = 0
        last_row = n
        first_column = 0
        last_column = n 

        while (start <= end ):
            # traverse left to right
            for i in range(first_column, last_column):
                matrix[first_row][i] = start
                start += 1
            first_row += 1

            # traverse up to down
            for i in range(first_row, last_row):
                matrix[i][last_column - 1] = start
                start += 1
            
            last_column -= 1

            # travel right to left
            for i in range(last_column - 1, first_column - 1, -1):
                matrix[last_row - 1][i] = start
                start += 1
            
            last_row -= 1

            # travel down to up
            for i in range(last_row - 1, first_row - 1, -1):
                matrix[i][first_column] = start
                start += 1

            first_column += 1

        return matrix


        