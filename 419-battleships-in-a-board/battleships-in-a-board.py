class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        rows = len(board)
        columns = len(board[0])
        
        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns):
                return False
            return True
            
        def traverse(i, j):
            if (not isValid(i, j) or board[i][j] != "X"):
                return
            board[i][j] = "."
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i + 1, j)
            traverse(i, j - 1)
            
        for i in range(rows):
            for j in range(columns):
                cell = board[i][j]
                if (cell == "."):
                    continue
                else:
                    count += 1
                    traverse(i, j)

        return count