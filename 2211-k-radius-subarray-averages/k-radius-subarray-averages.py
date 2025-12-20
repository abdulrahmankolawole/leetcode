class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        size = (k * 2) + 1
        output = [-1] * len(nums)

        if len(nums) < size:
            return output  # Return early if nums is too short

        # Calculate the initial sum for the first window
        current_sum = sum(nums[:size])

        for i in range(len(nums)):
            if i - k < 0 or i + k >= len(nums):
                continue
            if i > k:
                current_sum += nums[i + k] - nums[i - k - 1]
            average = current_sum // size  # Use integer division
            output[i] = average

        return output