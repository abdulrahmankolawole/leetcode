class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        lookup = {0: -1}
        total_sum = sum(nums)
        total_rem = total_sum % p
        curr_sum = 0
        output = len(nums)

        if total_rem == 0:
            return 0

        for i, val in enumerate(nums):
            curr_sum += val
            curr_rem = curr_sum % p

            target_rem = (curr_rem - total_rem + p) % p

            if target_rem in lookup:
                output = min(output, i - lookup[target_rem])
            
            lookup[curr_rem] = i

        return -1 if output == len(nums) else output