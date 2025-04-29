class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq = 1
        curr_sum = 0
        i = 0
        j = 0

        while (j < len(nums)):
            curr_sum += nums[j]

            while (nums[j] * (j - i + 1) > curr_sum + k):
                curr_sum -= nums[i]
                i += 1

            max_freq = max(max_freq, j - i + 1)
            j += 1

        return max_freq
        
            

            