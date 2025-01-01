class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        lookup = {0: 1}
        count = 0
        total = 0

        for i, val in enumerate(nums):
            total += val

            prefix = total - goal

            if (prefix in lookup):
                count += lookup[prefix]
            
            if (total not in lookup):
                lookup[total] = 0
            lookup[total] += 1
        
        return count
            
        