class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        output = 0
        lookup = set()
        sub_arr_sum = 0

        while (j < len(nums)):
            sub_arr_sum += nums[j]

            while (j - i + 1 > k or nums[j] in lookup):
                lookup.remove(nums[i])
                sub_arr_sum -= nums[i]
                i += 1
            
            if (j - i + 1 == k):
                output = max(output, sub_arr_sum)
            lookup.add(nums[j])

            j += 1

        return output

        