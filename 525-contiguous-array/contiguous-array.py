class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lookup = {0: -1}
        count = 0
        output = 0

        for i in range(len(nums)):
            if (nums[i] == 0):
                count -= 1
            elif (nums[i] == 1):
                count += 1
            
            if (count not in lookup):
                lookup[count] = i
            else:
                length = i - lookup[count]
                output = max(length, output)

        return output