class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        output = [0 for _ in range(len(nums))]

        for idx, val in enumerate(nums):
            right_sum = total - val - left_sum
            left_size = idx
            right_size = len(nums) - left_size - 1
            output[idx] = ((left_size * val) - left_sum) + (right_sum - (right_size * val))
            left_sum += val

        return output
        