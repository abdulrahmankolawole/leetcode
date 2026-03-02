class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        lookup = {0: -1}
        total_sum = sum(nums)
        total_rem = total_sum % p
        if (total_rem == 0):
            return 0

        output = len(nums)
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            current_rem = current_sum % p

            prefix_rem = ((current_rem - total_rem) + p) % p

            if (prefix_rem in lookup):
                output = min(output, i - lookup[prefix_rem])
            
            lookup[current_rem] = i

        return - 1 if output == len(nums) else output