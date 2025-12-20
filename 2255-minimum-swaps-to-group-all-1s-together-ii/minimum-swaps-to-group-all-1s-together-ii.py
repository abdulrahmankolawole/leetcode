class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # count the total number of ones
        no_of_ones = nums.count(1)
        window_ones = 0
        max_window_ones = 0
        N = len(nums)
        i = 0
        j = 0

        while (j < 2 * N):
            if (nums[j % N] == 1):
                window_ones += 1

            if (j - i + 1 > no_of_ones):
                if (nums[i % N] == 1):
                    window_ones -= 1
                i += 1

            max_window_ones = max(max_window_ones, window_ones) 

            j += 1

        return no_of_ones - max_window_ones  