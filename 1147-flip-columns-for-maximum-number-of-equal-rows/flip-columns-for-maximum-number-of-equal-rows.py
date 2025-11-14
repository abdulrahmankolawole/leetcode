class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        lookup = {}
        rows = len(matrix)
        columns = len(matrix)
        count = 0

        for row in matrix:
            row_key = tuple(row)
            if (not row[0]):
                row_key = tuple([0 if char == 1 else 1 for char in row])
            
            if (row_key not in lookup):
                lookup[row_key] = 0
            lookup[row_key] += 1

        for key in lookup:
            if (lookup[key] > 1):
                count = max(count, lookup[key])

        return 1 if count == 0 else count
