class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        going_up = True
        rows = len(mat)
        columns = len(mat[0])
        output = []
        i = 0
        j = 0

        while (len(output) < (rows * columns)):
            if going_up:
                while (i >= 0 and j < columns):
                    output.append(mat[i][j])
                    i -= 1
                    j += 1

                if (j == columns):
                    i += 2
                    j -= 1
                else:
                    i += 1
                going_up = False
            else:
                while (j >= 0 and i < rows):
                    output.append(mat[i][j])
                    j -= 1
                    i += 1

                if (i == rows):
                    j += 2
                    i -= 1
                else:
                    j += 1
                going_up = True


        return output


            