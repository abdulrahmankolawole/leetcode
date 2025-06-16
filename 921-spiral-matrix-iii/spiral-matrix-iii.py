class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        r = rStart
        c = cStart

        def isValid(i, j):
            if (i < 0 or j < 0 or i >= rows or j >= cols):
                return False
            return True

        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1
        i = 0

        while (len(result) < rows * cols):

            for _ in range(2):
                a, b = directions[i]
                for _ in range(steps):
                    if (isValid(r, c)):
                        result.append([r, c])
                
                    r += a
                    c += b

                
                i = (i + 1) % 4
            steps += 1

        return result

        

        