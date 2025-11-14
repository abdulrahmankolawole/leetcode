class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        output = 0

        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns or grid[i][j]):
                return False
            return True 

        def traverse(i, j):
            if (not isValid(i, j)):
                return 
            grid[i][j] = 1
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i + 1, j)
            traverse(i, j - 1)

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell == 0):
                    if (i == 0 or j == 0 or i == rows - 1 or j == columns - 1):
                        traverse(i, j)
        
        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell == 0):
                    output += 1
                    traverse(i, j)

        return output
        