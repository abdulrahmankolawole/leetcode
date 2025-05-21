class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]

            if (not stack):
                stack.append((temp, i))
                continue
            
            while (stack and temp >= stack[-1][0]):
                stack.pop()

            if (stack):
                output[i] = stack[-1][1] - i
            
            stack.append((temp, i))

        return output
            


        