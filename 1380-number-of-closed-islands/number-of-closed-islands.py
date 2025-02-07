class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        def traverse(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns or grid[i][j]):
                return 
            grid[i][j] = 1
            traverse(i - 1, j) #up
            traverse(i, j + 1) #right
            traverse(i + 1, j) #down
            traverse(i, j - 1) #left

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (not cell):
                    if (i == 0 or j == 0 or i == rows - 1 or j == columns - 1):
                        traverse(i, j)

        count = 0
        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (not cell):
                    count += 1
                    traverse(i, j)
        
        return count
        
