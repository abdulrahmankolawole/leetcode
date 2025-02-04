class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        lookup = {}
        max_number = 0

        for row in matrix:
            if (row[0]):
                key = tuple([0 if n else 1 for n in row])
            else:
                key = tuple(row)
            
            if (key not in lookup):
                lookup[key] = 0
            lookup[key] += 1
            max_number = max(max_number, lookup[key])

        
        return max_number
        # return max(lookup.values())