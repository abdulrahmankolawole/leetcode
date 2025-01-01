class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lookup = {0: -1}
        max_length = 0
        count = 0

        for i, val in enumerate(nums):
            if (val == 0):
                count -= 1
            else:
                count += 1
            
            if (count not in lookup):
                lookup[count] = i
            else:
                max_length = max(max_length, i - lookup[count])
        
        return max_length
        