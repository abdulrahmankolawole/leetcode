class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if (not stack or ast > 0):
                stack.append(ast)
                continue
            
            while (stack):
                peek = stack[-1]
                if (peek < 0):
                    stack.append(ast)
                    break

                if (peek == -ast):
                    stack.pop()
                    break
                
                if (peek > -ast):
                    break

                
                stack.pop()
                if (not stack):
                    stack.append(ast)
                    break
        
        return stack

            

        