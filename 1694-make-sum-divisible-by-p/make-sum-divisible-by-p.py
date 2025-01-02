class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        lookup = {0: -1}
        total = sum(nums)
        remain = total % p
        current_sum = 0
        res = len(nums)

        if (remain == 0):
            return 0

        for i, val in enumerate(nums):
            current_sum += val
            current_rem = current_sum % p

            prefix = (current_rem - remain + p) % p

            if (prefix in lookup):
                res = min(res, i - lookup[prefix])
            lookup[current_rem] = i

        return -1 if res == len(nums) else res   

        