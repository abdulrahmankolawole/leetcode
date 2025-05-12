class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        fresh = 0
        queue = []
        
        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]
                if (cell == 0):
                    continue
                elif (cell == 1):
                    fresh += 1
                    # oranges += 1
                else:
                    queue.append((i, j))
                    # oranges += 1


        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns or grid[i][j] != 1):
                return False
            return True

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        minutes = 0
        while (queue and fresh > 0):
            size = len(queue)

            for _ in range(size):
                i, j = queue.pop(0)

                for x, y in directions:
                    new_x = x + i
                    new_y = y + j

                    if (isValid(new_x, new_y)):
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 2
                        fresh -= 1
            minutes += 1
            if (fresh <= 0):
                break

        if (fresh > 0):
            return -1
        else:
            return minutes