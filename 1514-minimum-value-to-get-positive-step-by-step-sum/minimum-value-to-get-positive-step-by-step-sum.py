class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_value = 0
        running_sum = 0

        for num in nums:
            running_sum += num
            min_value = min(min_value, running_sum)

        return 1 - min_value