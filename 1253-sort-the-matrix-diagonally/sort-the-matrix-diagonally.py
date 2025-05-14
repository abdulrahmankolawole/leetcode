class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        columns = len(mat[0])
        lookup = {}

        for i in range(rows):
            for j in range(columns):
                cell = mat[i][j]
                diagonal = i - j
                if (diagonal not in lookup):
                    lookup[diagonal] = []
                lookup[diagonal].append(cell)

        for key in lookup:
            lookup[key].sort(reverse=True)

        for i in range(rows):
            for j in range(columns):
                diagonal = (i - j)
                mat[i][j] = lookup[diagonal].pop()

        return mat
                
        
        