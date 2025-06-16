class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        result = 0

        def isMagic(r, c):
            # validate cells in 3 * 3 grid are unique
            lookup = set()

            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    cell = grid[i][j]
                    
                    if (cell in lookup or not (1 <= cell <= 9)):
                        return 0
                    lookup.add(cell)


            # validate rows
            for i in range(r, r + 3):
                row_sum = sum(grid[i][c : c + 3])

                if (row_sum != 15):
                    return 0                

            # validate columns
            for j in range(c, c + 3):
                column_sum = 0
                for i in range(r, r + 3):
                    column_sum += grid[i][j]

                if (column_sum != 15):
                    return 0

            # validate diagonals
            if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15) or (grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15):
                return 0

            return 1


        for i in range(rows - 2):
            for j in range(columns - 2):
                result += isMagic(i, j)


        return result