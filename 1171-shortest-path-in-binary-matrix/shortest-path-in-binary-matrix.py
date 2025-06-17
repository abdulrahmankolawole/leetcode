class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        path = 1
        queue = [(0, 0)]
        n = len(grid)

        if (grid[0][0] != 0):
            return -1


        def isValid(i, j):
            if (i < 0 or j < 0 or i == n or j == n or grid[i][j]):
                return False
            return True

        while (queue):
            size = len(queue)

            for _ in range(size):
                i, j = queue.pop(0)
                if (i == n - 1 and j == n - 1):
                    return path

                for x, y in directions:
                    row = i + x
                    col = j + y

                    if (isValid(row, col)):
                        grid[row][col] = 1
                        queue.append((row, col))
            path += 1

        return -1



        