class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lookup = {0: -1}
        count = 0
        j = 0
        output = 0

        while (j < len(nums)):
            if (nums[j] == 0):
                count -= 1
            elif (nums[j] == 1):
                count += 1

            if (count not in lookup):
                lookup[count] = j
            else:
                output = max(output, j - lookup[count])

            j += 1

        return output
            
        