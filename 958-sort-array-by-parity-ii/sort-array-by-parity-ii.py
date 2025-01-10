class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        result = [None] * len(nums)

        def isEven(number):
            return number % 2 == 0

        for num in nums:
            if (isEven(num)):
                result[even] = num
                even += 2
            else:
                result[odd] = num
                odd += 2
        
        return result