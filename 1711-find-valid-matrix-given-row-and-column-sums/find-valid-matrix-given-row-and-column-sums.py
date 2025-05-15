class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        columns = len(colSum)
        cur_col_sum = 0
        matrix = [[0] * columns for _ in range(rows)]

        for i in range(rows):
            matrix[i][0] = rowSum[i]

        for j in range(columns):
            cur_col_sum = 0

            for i in range(rows):
                cur_col_sum += matrix[i][j]

            i = 0
            while (cur_col_sum > colSum[j]):
                diff = cur_col_sum - colSum[j]
                max_shift = min(diff, matrix[i][j])
                matrix[i][j + 1] += max_shift
                matrix[i][j] -= max_shift
                cur_col_sum -= max_shift
                i += 1

        return matrix