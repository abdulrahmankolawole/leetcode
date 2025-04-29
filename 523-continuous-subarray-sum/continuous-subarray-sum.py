class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lookup = {0: -1}
        curr_sum = 0

        for idx, val in enumerate(nums):
            curr_sum += val
            curr_rem = ((curr_sum % k) + k) % k
            if (curr_rem not in lookup):
                lookup[curr_rem] = idx
            else:
                if (idx - lookup[curr_rem] > 1):
                    return True
        
        return False

        