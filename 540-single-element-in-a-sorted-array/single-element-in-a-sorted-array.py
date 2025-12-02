class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while (i <= j):
            mid = (i + j) // 2

            if ((mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1])):
                return nums[mid]
            left_size = mid if nums[mid] != nums[mid - 1] else mid - 1

            if (left_size % 2 == 1):
                j = mid - 1
            else:
                i = mid + 1


        return -1
        