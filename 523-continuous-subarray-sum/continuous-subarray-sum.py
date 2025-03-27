class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lookup = {0: -1}
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            remainder = curr_sum % k

            if (remainder not in lookup):
                lookup[remainder] = i
            elif (i - lookup[remainder] > 1):
                return True

        return False
        