class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_row = 0
        first_column = 0
        last_row = len(matrix) - 1
        last_column = len(matrix[0]) - 1

        while (first_row <= last_row and first_column <= last_column):
            if (matrix[first_row][last_column] == target):
                return True
            if (target > matrix[first_row][last_column]):
                first_row += 1
            else:
                last_column -= 1

        return False
        