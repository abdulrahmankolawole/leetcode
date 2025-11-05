class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(["+", "-", "*", "/"])

        for token in tokens:
        
            if (token in operands):
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if (token == "+"):
                    stack.append(num1 + num2)
                elif (token == "-"):
                    stack.append(num1 - num2)
                elif (token == "*"):
                    stack.append(num1 * num2)
                elif (token == "/"):
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
            
        return stack.pop()
        