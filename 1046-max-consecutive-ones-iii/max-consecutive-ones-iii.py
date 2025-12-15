class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        output = 0
        zeroes = 0

        while (j < len(nums)):
            if (nums[j] == 0):
                zeroes += 1

            while (zeroes > k):
                if (nums[i] == 0):
                    zeroes -= 1
                i += 1

            output = max(output, j - i + 1)
            j += 1

        return output


        