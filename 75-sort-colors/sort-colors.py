class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        mid = 0
        j = len(nums) - 1

        while (mid <= j):
            if (nums[mid] == 0):
                nums[i], nums[mid] = nums[mid], nums[i]
                i += 1
                mid += 1
            elif (nums[mid] == 1):
                mid +=1
            else:
                nums[mid], nums[j] = nums[j], nums[mid]
                j -= 1