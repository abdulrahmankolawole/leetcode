class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        ans = []

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            
            left_size = i
            right_size = n - 1 - i
            
            left_total = (left_size * nums[i]) - left_sum
            right_total = right_sum - (right_size * nums[i])

            ans.append(left_total + right_total)
            left_sum += nums[i]
        
        return ans