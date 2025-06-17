class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowLookup = {}
        columnLookup = {}
        rows = len(grid)
        columns = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell):
                    if i not in rowLookup:
                        rowLookup[i] = 0
                    rowLookup[i] += 1

                    if j not in columnLookup:
                        columnLookup[j] = 0
                    columnLookup[j] += 1

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell):
                    if rowLookup[i] > 1 or columnLookup[j] > 1:
                        count += 1

        return count
                
        