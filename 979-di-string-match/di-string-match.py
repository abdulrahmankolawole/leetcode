class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        output = [None] * len(s)

        for i in range(len(s)):
            char = s[i]
            if (char == "I"):
                output[i] = low
                low += 1
            else:
                output[i] = high
                high -= 1

        output.append(low)
        return output
