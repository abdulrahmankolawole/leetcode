class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lookup = {}
        
        for i, val in enumerate(nums):
            if (val not in lookup):
                lookup[val] = 0
            lookup[val] += 1

        for val in lookup:
            if (lookup[val] == 1):
                return val
            
        