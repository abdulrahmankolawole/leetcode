class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        result = [0 for _ in range(len(nums))]

        for i, val in enumerate(nums):
            right_sum = total_sum - val - left_sum
            left_size = i
            right_size = len(nums) - left_size - 1

            result[i] = ((left_size * val) - left_sum) + (right_sum - (right_size * val))
            left_sum += val
        
        return result

        