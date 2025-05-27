class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 0
        while j < len(nums):
            streak = 1

            while (j + 1 < len(nums) and nums[j] == nums[j + 1]):
                streak += 1
                j += 1

            for _ in range(min(streak, 2)):
                nums[i] = nums[j]
                i += 1
            
            j += 1

        
        return i

        