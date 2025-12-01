class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while (i <= j):
            mid = (i + j) // 2

            if (mid > 0 and nums[mid] < nums[mid - 1]):
                j = mid - 1
            elif (mid < len(nums) - 1 and nums[mid] < nums[mid + 1]):
                i = mid + 1
            else:
                return mid



        