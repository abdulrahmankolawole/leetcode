class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        first_row = 0
        first_column = 0
        rows = len(matrix)
        columns = len(matrix[0])

        while (first_row < rows and first_column < columns):
            # traverse left to right
            for j in range(first_column, columns):
                output.append(matrix[first_row][j])
            first_row += 1

            # traverse up to down
            for i in range(first_row, rows):
                output.append(matrix[i][columns - 1])
            columns -= 1

            if (first_row < rows):
                # traverse right to left
                for j in range(columns - 1, first_column - 1, -1):
                    output.append(matrix[rows - 1][j])
                rows -= 1

            if (first_column < columns):
                # traverse bottom to top
                for i in range(rows - 1, first_row - 1, -1):
                    output.append(matrix[i][first_column])
                first_column += 1

        return output