class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        output = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = rStart
        j = cStart
        steps = 1
        k = 0

        def isValid(i, j):
            if ((i < 0 or i >= rows) or (j < 0 or j >= cols)):
                return False
            return True
        
        while (len(output) < rows * cols):
                
            for _ in range(2):
                direction = directions[k]
                x, y = direction

                for _ in range(steps):

                    if (isValid(i, j)):
                        output.append([i, j]) 
                    i = x + i
                    j = j + y

                k = (k + 1) % len(directions)
                
            steps += 1

        return output
        