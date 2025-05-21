class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for idx, val in enumerate(s):
            if (not stack):
                stack.append(val)
                continue

            if (stack[-1] == val):
                stack.pop()
                continue
            
            stack.append(val)

        return "".join(stack)
        