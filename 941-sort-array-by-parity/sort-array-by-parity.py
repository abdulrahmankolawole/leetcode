class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        def isEven(number):
            return number % 2 == 0

        while (i <= j):
            if (isEven(nums[i])):
                i += 1
            elif (not isEven(nums[j])):
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        return nums
        