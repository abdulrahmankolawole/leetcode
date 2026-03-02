class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        lookup = {0: -1}
        output = 0

        for i in range(len(nums)):
            if (nums[i] == 0):
                count += 1
            else:
                count -= 1

            if (count in lookup):
                output = max(output, i - lookup[count])
            
            else:
                lookup[count] = i

        return output
        