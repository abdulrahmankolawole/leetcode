class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        columns = len(mat[0])
        i = 0
        j = 0

        while (i < rows and j < columns):
            cell = mat[i][j]

            if (i > 0 and cell <= mat[i - 1][j]):
                i -= 1
            elif (j < columns - 1 and cell <= mat[i][j + 1]):
                j += 1
            elif (i < rows - 1 and cell <= mat[i + 1][j]):
                i += 1
            elif (j > 0 and cell <= mat[i][j - 1]):
                j -= 1
            else:
                return [i, j]

        return [-1, -1]
        