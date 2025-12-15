class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        output = [0 for _ in range(len(nums))]

        for idx, num in enumerate(nums):
            right_sum = total_sum - num - left_sum
            left_size = idx
            right_size = len(nums) - idx - 1

            output[idx] = ((left_size * num) - left_sum) + (right_sum - (right_size * num))
            left_sum += num

        return output
        
        