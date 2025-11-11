class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # capture unsurrounded regions
        # capture surrounded regions
        # uncapture surrounded regions
        rows = len(board)
        columns = len(board[0])
        
        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns):
                return False
            return True

        def traverse(i, j):
            if (not isValid(i, j) or board[i][j] != "O"):
                return 
            board[i][j] = "T"
            traverse(i - 1, j) #up
            traverse(i, j + 1) #right
            traverse(i + 1, j) #down
            traverse(i, j - 1) #left

        for i in range(rows):
            for j in range(columns):
                if (i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
                    traverse(i, j)

        for i in range(rows):
            for j in range(columns):
                cell = board[i][j]

                if (cell == "O"):
                    board[i][j] = "X"

        for i in range(rows):
            for j in range(columns):
                if (board[i][j] == "T"):
                    board[i][j] = "O"