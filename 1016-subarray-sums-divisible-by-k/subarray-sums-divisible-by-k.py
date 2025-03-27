class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        curr_sum = 0
        count = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            remainder = curr_sum % k

            if (remainder not in lookup):
                lookup[remainder] = 0
            else:
                count += lookup[remainder]
            lookup[remainder] += 1

        return count
        