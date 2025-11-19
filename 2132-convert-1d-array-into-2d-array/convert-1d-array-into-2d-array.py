class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = len(original)
        if (size > m * n or size < m * n):
            return []
        matrix = [[None] * n for _ in range(m)]
        k = 0

        for i in range(m):
            for j in range(n):
                matrix[i][j] = original[k]
                k = (k + 1) % size

        return matrix
        