class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # brute force O(n2)
        # output = float("inf")
        
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         subarr = nums[i: j + 1]

        #         subarr_sum = sum(subarr)
        #         if (subarr_sum >= target):
        #             output = min(output, len(subarr))
        
        # return 0 if output == float("inf") else output

        # sliding window
        i = 0
        j = 0
        curr_sum = 0
        output = float("inf")

        while (j < len(nums)):
            curr_sum += nums[j]

            while (curr_sum >= target):
                output = min(output, j - i + 1)
                curr_sum -= nums[i]
                i += 1

            j += 1

        return 0 if output == float("inf") else output

