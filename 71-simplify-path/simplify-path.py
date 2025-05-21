class Solution:
    def simplifyPath(self, path: str) -> str:
        array = path.split("/")
        stack = []

        for char in array:
            if (char == "." or char == ""):
                continue
            elif (char == ".."):
                if (stack):
                    stack.pop()
            else:
                stack.append(char)

        return "/" + "/".join(stack)
        