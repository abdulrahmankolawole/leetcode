class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        columns = len(grid[0])
        count = 0

        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns):
                return False
            return True

        def traverse(i, j):
            if (not isValid(i, j) or grid[i][j] != "1"):
                return 
            grid[i][j] = "0"
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i + 1, j)
            traverse(i, j - 1)

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]
                if (cell == "1"):
                    count += 1
                    traverse(i, j)

        return count
        