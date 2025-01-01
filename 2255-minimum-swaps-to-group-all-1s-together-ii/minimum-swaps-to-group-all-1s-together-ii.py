class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_no_of_ones = nums.count(1)
        window_ones = 0
        max_window_ones = 0
        i = 0
        j = 0

        while (j < 2 * len(nums)):
            if (nums[j % len(nums)]):
                window_ones += 1
            
            if (j - i + 1 > total_no_of_ones):
                if (nums[i % len(nums)]):
                    window_ones -= 1
                i += 1
            
            max_window_ones = max(max_window_ones, window_ones)
            j += 1
        
        return total_no_of_ones - max_window_ones
                
                