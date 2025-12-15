class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        lookup = {}
        most_freq = 0
        output = 0

        while (j < len(s)):
            char = s[j]

            if (char not in lookup):
                lookup[char] = 0
            lookup[char] += 1
            most_freq = max(most_freq, lookup[char])

            while ((j - i + 1) - most_freq > k):
                lookup[s[i]] -= 1
                i += 1

            output = max(output, j - i + 1)
            j += 1

        return output
        