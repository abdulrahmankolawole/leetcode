class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0
        j = len(arr) - k

        while (i < j):
            mid = (i + j) // 2

            if (x - arr[mid] > arr[mid + k] - x):
                i = mid + 1
            else:
                j = mid

        
        return arr[i: i + k]
        