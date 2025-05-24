class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # return the max score of unique elems
        total = 0
        i = 0
        j = 0
        lookup = set()
        output = 0

        while (j < len(nums)):
            while (nums[j] in lookup):
                total -= nums[i]
                lookup.remove(nums[i])
                i += 1

            total += nums[j]
            lookup.add(nums[j])
            output = max(output, total)
            j += 1

        return output
        
        