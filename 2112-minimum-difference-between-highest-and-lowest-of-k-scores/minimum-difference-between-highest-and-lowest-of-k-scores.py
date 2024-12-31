class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i = 0
        j = k - 1
        output = 10 ** 5

        while (j < len(nums)):
            difference = nums[j] - nums[i]
            output = min(difference, output)

            i += 1
            j += 1

        return output
        