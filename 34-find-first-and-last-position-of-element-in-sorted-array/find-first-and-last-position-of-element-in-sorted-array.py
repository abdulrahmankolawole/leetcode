class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def leftBinarySearch(array, val):
            i = 0
            j = len(array) - 1
            index = -1

            while (i <= j):
                mid = (i + j) // 2

                if (array[mid] == val):
                    index = mid
                    j = mid - 1
                elif (val < array[mid]):
                    j = mid - 1
                else: 
                    i = mid + 1

            return index

        def rightBinarySearch(array, val):
            i = 0
            j = len(array) - 1
            index = -1

            while (i <= j):
                mid = (i + j) // 2

                if (array[mid] == val):
                    index = mid
                    i = mid + 1
                elif (val < array[mid]):
                    j = mid - 1
                else: 
                    i = mid + 1

            return index

        left = leftBinarySearch(nums, target)
        right = rightBinarySearch(nums, target)
        

        return [left, right]