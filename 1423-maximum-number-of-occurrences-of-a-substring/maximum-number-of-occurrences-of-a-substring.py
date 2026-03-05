class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        lookup = {}
        output = 0
        j = 0

        def isValid(word):
            my_set = set(word)

            return len(my_set) <= maxLetters

        while (j <= len(s) - minSize):
            substr = s[j: j + minSize]
            
            if (isValid(substr)):
                if (substr not in lookup):
                    lookup[substr] = 0
                lookup[substr] += 1

                output = max(output, lookup[substr])

            j += 1

        return output