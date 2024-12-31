class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i = 0
        j = 0
        max_window = - 1
        current_sum = 0
        total_sum = sum(nums)
        target = total_sum - x

        while (j < len(nums)):
            current_sum += nums[j]

            while (current_sum > target and i <= j):
                current_sum -= nums[i]
                i += 1
            
            if (current_sum == target):
                max_window = max(max_window, j -i + 1)
            
            j += 1

        
        return max_window if max_window == - 1 else len(nums) - max_window