class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        columns = len(grid1[0])
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        count = 0

        def isValid(i, j):
            if (i < 0 or j < 0 or i== rows or j == columns):
                return False
            if (i, j) in visited:
                return False
            if (grid2[i][j] != 1):
                return False
            return True

        

        def has_sub_island(i, j):
            is_sub_island = True
            queue = [(i, j)]

            if (grid1[i][j] != 1):
                is_sub_island = False

            while (queue):
                x, y = queue.pop(0)

                for a, b in directions:
                    new_x = a + x
                    new_y = b + y


                    if (isValid(new_x, new_y)):
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
                        if grid1[new_x][new_y] != 1:
                            is_sub_island = False


            return is_sub_island
                    
    

        for i in range(rows):
            for j in range(columns):
                cell = grid2[i][j]
                if (cell):
                    if isValid(i, j) and has_sub_island(i, j):
                        count += 1

        return count

        