class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lookup = {0: -1}
        curr_sum = 0
        output = 0

        for i in range(len(nums)):
            num = nums[i]
            if (num == 0):
                curr_sum -= 1
            elif (num == 1):
                curr_sum += 1

            if (curr_sum not in lookup):
                lookup[curr_sum] = i
            else:
                output = max(output, i - lookup[curr_sum])

        return output