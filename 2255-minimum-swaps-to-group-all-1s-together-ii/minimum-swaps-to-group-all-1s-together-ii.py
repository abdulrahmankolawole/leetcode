class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = nums.count(1)
        i = 0
        j = 0
        max_window_ones = 0
        window_ones = 0

        while (j < 2 * len(nums)):
            if (nums[j % len(nums)] == 1):
                window_ones += 1
            
            while (j - i + 1 > total_ones):
                if (nums[i % len(nums)] == 1):
                    window_ones -= 1
                i += 1

            max_window_ones = max(window_ones, max_window_ones)
            j += 1

        return total_ones - max_window_ones
        