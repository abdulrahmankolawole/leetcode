class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        count = 0
        running_sum = 0

        for idx, val in enumerate(nums):
            running_sum += val

            curr_rem = running_sum % k

            if (curr_rem not in lookup):
                lookup[curr_rem] = 0
            else:
                count += lookup[curr_rem]
            
            lookup[curr_rem] += 1

        return count        