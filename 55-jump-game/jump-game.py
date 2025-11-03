class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for idx in range(len(nums) - 1, -1, -1):
            if (nums[idx] + idx >= goal):
                goal = idx
        
        return goal == 0
        