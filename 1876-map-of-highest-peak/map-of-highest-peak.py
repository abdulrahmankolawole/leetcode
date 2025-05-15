class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        columns = len(isWater[0])
        queue = []
        matrix = [[-1] * columns for _ in range(rows)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j== columns or matrix[i][j] != -1):
                return False
            return True

        for i in range(rows):
            for j in range(columns):
                cell = isWater[i][j]

                if (cell):
                    matrix[i][j] = 0
                    queue.append((i, j))

        while (queue):
            size = len(queue)

            for _ in range(size):

                i, j = queue.pop(0)
                for x, y in directions:
                    new_x = x + i
                    new_y = y + j

                    if (isValid(new_x, new_y)):
                        queue.append((new_x, new_y))
                        matrix[new_x][new_y] = matrix[i][j] + 1

        return matrix


        