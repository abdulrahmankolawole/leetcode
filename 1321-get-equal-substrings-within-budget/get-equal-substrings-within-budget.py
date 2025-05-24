class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        j = 0
        current_cost = 0
        output = 0

        while (j < len(s)):
            current_cost += abs(ord(s[j]) - ord(t[j]))

            while (current_cost > maxCost):
                current_cost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            
            output = max(output, j - i + 1)
            j += 1

        return output
        