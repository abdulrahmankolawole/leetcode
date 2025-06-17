class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        up = {x: set([2, 3, 4]) for x in [2, 5, 6]}
        right = {x: set([1, 3, 5]) for x in [1, 4, 6]}
        down = {x: set([2, 5, 6]) for x in [2, 3, 4]}
        left = {x: set([1, 4, 6]) for x in [1, 3, 5]}
        rows = len(grid)
        columns = len(grid[0])
        lookup = set()

        def isValid(i, j, row, col, direction):
            if (row < 0 or col < 0 or row == rows or col == columns or (row, col) in lookup):
                return False            
            street = grid[i][j]
            if (street not in direction):
                return False
            path = grid[row][col]
            if (path not in direction[street]):
                return False
            return True

        queue = [(0, 0)]
        directions = [(-1, 0, up), (0, 1, right), (1, 0, down), (0, -1, left)]
        
        while (queue):
            x, y = queue.pop(0)
            if (x == rows - 1 and y == columns - 1):
                return True

            for i, j, direction in directions:
                row = i + x
                col = j + y

                if (isValid(x, y, row, col, direction)):
                    queue.append((row, col))
                    lookup.add((row, col))

        return False
        