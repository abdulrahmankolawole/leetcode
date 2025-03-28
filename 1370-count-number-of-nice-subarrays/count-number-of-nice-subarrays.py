class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        array = [x for x in nums]
        curr_sum = 0
        output = 0

        def isOdd(val):
            return val % 2 != 0

        for i in range(len(nums)):
            if (isOdd(nums[i])):
                array[i] = 1
            else:
                array[i] = 0

        for i in range(len(nums)):
            curr_sum += array[i]
            prefix = curr_sum - k

            if (prefix in lookup):
                output += lookup[prefix]
            if (curr_sum not in lookup):
                lookup[curr_sum] = 0
            lookup[curr_sum] += 1

        return output
            
        