class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        break_index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_index = i
                break 
        
        
        if break_index == -1:
            nums.reverse()
            return

        swap_index = -1
        for i in range(len(nums) -1, break_index, -1):
            if (nums[i] > nums[break_index]):
                swap_index = i
                break
        
        nums[swap_index], nums[break_index] = nums[break_index], nums[swap_index]

        i = break_index + 1
        j = len(nums) - 1
        while (i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        # return nums

        