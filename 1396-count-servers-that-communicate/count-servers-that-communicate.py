class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        lookup = {}

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell):
                    row = f"row: {i}"
                    column = f"column: {j}"

                    if (row not in lookup):
                        lookup[row] = 0
                    lookup[row] += 1

                    if (column not in lookup):
                        lookup[column] = 0
                    lookup[column] += 1

        count = 0
        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]
                row = f"row: {i}"
                column = f"column: {j}"

                if (cell):
                    if (lookup[row] > 1 or lookup[column] > 1):
                        count += 1

        return count
        