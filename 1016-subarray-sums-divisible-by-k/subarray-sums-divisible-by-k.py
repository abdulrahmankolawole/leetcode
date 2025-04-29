class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        lookup = {0: 1}
        curr_sum = 0

        for idx, val in enumerate(nums):
            curr_sum += val
            curr_rem = curr_sum % k

            if (curr_rem not in lookup):
                lookup[curr_rem] = 0
            else:
                count += lookup[curr_rem]
            lookup[curr_rem] += 1
        
        return count




        