class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        l = 0
        r = N - 1
        res = N
        while (l < N - 1 and arr[l] <= arr[l + 1]):
            l += 1

        while (r > 0 and arr[r] >= arr[r - 1]):
            r -= 1

        if (r == 0):
            return 0

        i = 0
        j = r
        res = min(res, r, N - l - 1)
        while (i <= l and j < N):
            if (arr[i] <= arr[j]):
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1


        return res

        