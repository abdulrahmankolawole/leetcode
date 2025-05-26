class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        output = 0
        max_elem = max(nums)
        count = 0
        
        while (j < len(nums)):
            if (nums[j] == max_elem):
                count += 1

            while (count >= k):
                output += len(nums) - j
                if (nums[i] == max_elem):
                    count -= 1
                i += 1

            j += 1

        return output

        