class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        columns = len(grid[0])
        visited = set((0, 0))
        
        # dictionaries for transition rule
        up = {x: set([2, 3, 4]) for x in [2, 5, 6]}
        right = {x: set([1, 3, 5]) for x in [1, 4, 6]}
        down = {x: set([2, 5, 6]) for x in [2, 3, 4]}
        left = {x: set([1, 4, 6]) for x in [1, 3, 5] }
        
        def isValid(dr, dc, i, j, direction):

            if dr < 0 or dr == rows or dc < 0 or dc == columns or (dr, dc) in visited:
                return False

            street = grid[i][j]

            if street not in direction:
                return False

            path = grid[dr][dc]
            if path not in direction[street]:
                return False

            return True
        

        directions = [(-1, 0, up), 
                        (0, 1, right), 
                        (1, 0, down),
                        (0, -1, left) ]

        queue = [(0, 0)]

        while queue:

            i, j = queue.pop(0)
            
            if (i, j) == (rows - 1, columns - 1):
                return True
            for dr, dc, map in directions:
                new_x = dr + i
                new_y = dc + j

                # if we travel out of bounds return False
                if isValid(new_x, new_y, i, j, map):
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))

        return False