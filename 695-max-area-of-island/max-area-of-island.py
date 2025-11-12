class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        columns = len(grid[0])

        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns):
                return False
            return True

        def traverse(i, j):
            area = 0
            if (not isValid(i, j) or grid[i][j] != 1):
                return 0
            temp = grid[i][j]
            grid[i][j] = 0
            area += temp
            area += traverse(i - 1, j)
            area += traverse(i, j + 1)
            area += traverse(i + 1, j)
            area += traverse(i, j - 1)
            return area

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell == 1):
                    max_area = max(max_area, traverse(i, j))
        

        return max_area
        