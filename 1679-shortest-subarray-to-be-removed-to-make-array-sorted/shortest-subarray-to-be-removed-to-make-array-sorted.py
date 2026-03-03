class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        i = 0
        j = N - 1
        output = N

        while (i < N -1 and arr[i] <= arr[i + 1]):
            i += 1

        while (j > 0 and arr[j] >= arr[j - 1]):
            j -=1 

        if (j == 0):
            return 0

        output = min(output, j, N - i - 1)
        l = 0
        r = j

        while (l <= i and r < N):
            if (arr[l] <= arr[r]):
                output = min(output, r- l - 1)
                l += 1
            else:
                r += 1

        return output 
        
        