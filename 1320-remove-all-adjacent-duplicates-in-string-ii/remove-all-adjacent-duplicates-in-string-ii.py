class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for val in s:
            if (not stack):
                stack.append([val, 1])
                continue

            if (stack[-1][0] != val):
                stack.append([val, 1])
                continue

            streak = stack[-1][1]
            if (streak + 1 == k):
                stack.pop()
                continue
            
            stack[-1][1] = streak + 1
                

        result = [(val * count) for val, count in stack]

        return "".join(result)
        