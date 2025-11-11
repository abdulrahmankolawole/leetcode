class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # iterate through the grid
        # count the cell of the neighbors
        # if cell is live
        # if count of neigbors is not equal to two or 3, the cell dies (s)
        # if the cell is dead
        # if the count of neighbors is equal to 3, the cell lives on
        rows = len(board)
        columns = len(board[0])
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns):
                return False
            return True

        def countNeighbors(i, j):
            count = 0
            
            for x, y in directions:
                new_x = x + i
                new_y = y + j

                if (isValid(new_x, new_y)):
                    if (board[new_x][new_y] >= 1):
                        count += 1

            return count

        for i in range(rows):
            for j in range(columns):
                cell = board[i][j]

                count = countNeighbors(i, j)
                if (cell == 1):
                    if (count not in [2, 3]):
                        board[i][j] = 2
                elif (cell == 0):
                    if (count == 3):
                        board[i][j] = -1

        for i in range(rows):
            for j in range(columns):
                cell = board[i][j]

                if (cell == -1):
                    board[i][j] = 1
                elif (cell == 2):
                    board[i][j] = 0
                        