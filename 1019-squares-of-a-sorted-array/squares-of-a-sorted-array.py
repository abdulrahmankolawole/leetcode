class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        nums = [num ** 2 for num in nums]
        result = [None] * len(nums)
        k = len(nums) - 1

        while (i <= j):
            if (nums[i] > nums[j]):
                result[k] = nums[i]
                i += 1
            else:
                result[k] = nums[j]
                j -= 1
            k -= 1

        return result