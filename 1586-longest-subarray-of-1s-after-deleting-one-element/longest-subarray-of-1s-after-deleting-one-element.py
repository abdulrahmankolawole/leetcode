class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        max_size = 0
        count_of_zeroes = 0
        
        while (j < len(nums)):
            if (nums[j] == 0):
                count_of_zeroes += 1
            
            while (count_of_zeroes > 1):
                if (nums[i] == 0):
                    count_of_zeroes -= 1
                i += 1
            
            max_size = max(max_size, j - i)
            j += 1
        
        return max_size