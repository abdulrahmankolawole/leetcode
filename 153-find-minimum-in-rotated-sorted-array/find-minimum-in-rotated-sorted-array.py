class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        if (nums[i] <= nums[j]):
            return nums[0]

        while (i <= j):
            mid = (i + j) // 2

            if (mid + 1 < len(nums) and nums[mid + 1] < nums[mid]):
                return nums[mid + 1]
            if (mid > 0 and nums[mid - 1] > nums[mid]):
                return nums[mid]
            
            if (nums[i] <= nums[mid]):
                i = mid + 1

            elif (nums[mid] <= nums[j]):
                j = mid - 1
        
        return -1
            
        