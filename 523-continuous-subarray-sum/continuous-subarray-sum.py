class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # iterate through nums
        # keep track of the curr_sum as we go
        # check the current remainder
        # if the current remainder has been seen return the size of the current subarray
        
        lookup = {0: -1}
        curr_sum = 0

        for idx, val in enumerate(nums):
            curr_sum += val
            curr_rem = ((curr_sum % k) + k) % k


            if (curr_rem in lookup):
                if (idx - lookup[curr_rem] >= 2):
                    return True
            else:
                lookup[curr_rem] = idx

        
        return False