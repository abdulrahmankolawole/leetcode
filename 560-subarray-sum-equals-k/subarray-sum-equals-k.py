class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        output = 0
        total = 0

        for i, val in enumerate(nums):
            total += val
            prefix = total - k

            if (prefix in lookup):
                output += lookup[prefix]
            
            if (total not in lookup):
                lookup[total] = 0
            lookup[total] += 1

        return output


        