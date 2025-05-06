class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell == 1):
                    perimeter += 4
                    if (j > 0 and grid[i][j - 1] == 1):
                        perimeter -= 2
                    if (i > 0 and grid[i - 1][j] == 1):
                        perimeter -=2

        return perimeter
        