class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        j = 0
        current_cost = 0
        max_length = 0

        while (j < len(s)):
            ascii1 = ord(s[j])
            ascii2 = ord(t[j])

            current_cost += abs(ascii1 - ascii2)

            while (current_cost > maxCost):
                current_cost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            
            max_length = max(max_length, j - i + 1)
            j += 1

        return max_length
        