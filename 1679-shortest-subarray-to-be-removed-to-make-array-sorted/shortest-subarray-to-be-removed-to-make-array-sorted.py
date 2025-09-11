class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        # find the length of minimum postfix that can be removed
        i = 0
        N = len(arr)
        j = N - 1
        output = N

        while (i < N - 1 and arr[i] <= arr[i + 1]):
            i += 1

        # find the length of minimum prefix that can be removed
        while (j > 0 and arr[j] >= arr[j - 1]):
            j -= 1

        if (j == 0):
            return 0

        l = 0
        r = j
        output = min(output, N - i - 1, r)

        while (l <= i and r < N):
            if (arr[l] <= arr[r]):
                output = min(output, r - l - 1)
                l += 1
            else:
                r += 1

        return output
        
