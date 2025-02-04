class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        # iterate through the grid
        # if the current cell is on the boundary
        # traverse the adjacent land cells
        # iterate through the grid and count the number of land cells remaining

        rows = len(grid)
        columns = len(grid[0])

        def traverse(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns or grid[i][j] != 1):
                return 
            grid[i][j] = 0
            traverse(i - 1, j) #up
            traverse(i, j + 1) # right
            traverse(i + 1, j) #down
            traverse(i, j - 1) # left

        for i in range(rows):
            for j in range(columns):
                if ((i == 0 or j == 0 or i == rows - 1 or j == columns - 1) and grid[i][j]):
                    traverse(i, j)

        count = 0
        for i in range(rows):
            for j in range(columns):
                if (grid[i][j]):
                    count += 1

        return count
        


        