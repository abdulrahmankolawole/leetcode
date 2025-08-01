class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0),(0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        result = 0

        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns):
                return False
            return True

        def dfs(i, j):
            path = 0
            if (not isValid(i, j) or grid[i][j] == 0):
                return 0

            temp = grid[i][j]
            grid[i][j] = 0
            path = max(path, temp + dfs(i - 1, j)) #up
            path = max(path, temp + dfs(i, j + 1)) #right
            path = max(path, temp + dfs(i + 1, j)) #down
            path = max(path, temp + dfs(i, j - 1)) #left
            grid[i][j] = temp
            return path

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (not cell):
                    continue

                result = max(result, dfs(i, j))

        return result
