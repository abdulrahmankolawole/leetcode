class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while (i <= j):
            mid = (i + j) // 2

            if ((mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1])):
                return nums[mid]
            left_size = mid - 1 if nums[mid] == nums[mid - 1] else mid

            if (left_size % 2 == 0):
                i = mid + 1
            else:
                j = mid - 1
            
        