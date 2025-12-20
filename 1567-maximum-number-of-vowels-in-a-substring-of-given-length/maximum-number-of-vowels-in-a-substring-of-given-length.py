class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lookup = set("aeiou")
        vowels = 0
        output = 0

        for i in range(k):
            char = s[i]
            if (char in lookup):
                vowels += 1

        output = max(vowels, output)

        for i in range(k, len(s)):
            char = s[i]
            if (char in lookup):
                vowels += 1
            if (s[i - k] in lookup):
                vowels -= 1

            output = max(vowels, output)

        return output     