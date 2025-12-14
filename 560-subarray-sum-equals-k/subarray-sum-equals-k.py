class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num

            prefix = running_sum - k

            if (prefix in lookup):
                count += lookup[prefix]
            
            if (running_sum not in lookup):
                lookup[running_sum] = 0
            lookup[running_sum] += 1

        return count
        