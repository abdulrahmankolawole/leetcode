class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        output = [0] * len(s)
        prev = float("inf")

        for i in range(len(s)):
            if (s[i] == c):
                prev = i
            else:
                output[i] = abs(prev - i)

        
        prev = float("inf")

        for i in range(len(s) - 1, -1, -1):
            if (s[i] == c):
                prev = i
            output[i] = min(abs(prev - i), output[i])
        
        return output


        