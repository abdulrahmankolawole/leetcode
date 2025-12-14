class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        lookup = {0: 1}
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num
            prefix = running_sum - goal

            if (prefix in lookup):
                count += lookup[prefix]

            if (running_sum not in lookup):
                lookup[running_sum] = 0
            lookup[running_sum] += 1


        return count
        