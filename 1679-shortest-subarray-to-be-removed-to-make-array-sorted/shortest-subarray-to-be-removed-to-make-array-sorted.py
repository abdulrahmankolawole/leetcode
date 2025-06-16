class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        i = 0
        j = N - 1
        res = N - 1

        # find the longest prefix you can remove to make array sorted
        while (j > 0 and arr[j - 1] <= arr[j]):
            j -= 1

        res = j
        
        # find the longest postfix you can remove to make array sorted
        while (i + 1 < N  and arr[i] <= arr[i + 1]):
            i += 1

        if (i == N - 1):
            return 0

        res = min(res, N - 1 - i)

        # find smallest middle part you can remove
        l = 0
        r = j
        while (l <= i and r < N):
            if (arr[l] <= arr[r]):
                res = min(res, r - l - 1)
                l += 1
            else:
                r += 1

        return res


        