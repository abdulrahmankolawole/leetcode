class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        j = len(arr) - 1

        while (i <= j):
            mid = (i + j) // 2

            if ((mid == 0 or arr[mid - 1] < arr[mid]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1])):
                return mid
            else:
                if (arr[mid] < arr[mid + 1]):
                    i = mid + 1
                else:
                    j = mid - 1
        