class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
         
        rows = len(grid)
        columns = len(grid[0])
        output = 0
        
        def dfs(i, j, visit):
            res = 0
            if (i < 0 or j < 0 or i == rows or j == columns or grid[i][j] == 0 or (i, j) in visit):
                return 0
            visit.add((i, j))
            res = grid[i][j]
            # res += grid[i][j]
            # grid[i][j] = 0
            res = max(res, grid[i][j] + dfs(i - 1, j, visit)) # up
            res = max(res, grid[i][j] + dfs(i, j + 1, visit)) # right
            res = max(res, grid[i][j] + dfs(i + 1, j, visit)) # down
            res = max(res, grid[i][j] + dfs(i, j - 1, visit)) # left
            # grid[i][j] = temp
            visit.remove((i, j))
            return res

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell):
                    output = max(output, dfs(i, j, set()))

        return output

