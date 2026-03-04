class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = [-1 for _ in range(len(nums))]
        size = len(nums)
        j = size * 2
        stack = []

        while (j >= 0):
            if (not stack):
                stack.append(nums[j % size])
            else:
                while (stack and nums[j % size] >= stack[-1]):
                    stack.pop()

                if (stack):
                    output[j % size] = stack[-1]
                
                stack.append(nums[j % size])

            j -= 1
            
        return output