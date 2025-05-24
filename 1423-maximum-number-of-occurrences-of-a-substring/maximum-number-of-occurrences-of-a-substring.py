class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        i = 0
        j = 0
        output = 0
        lookup = {}

        def noOfUnique(char):
            lookup = set([x for x in char])
            return len(lookup)

        while (j < len(s) - (minSize - 1)):
            substring = s[j: j + minSize]
            
            if (noOfUnique(substring) <= maxLetters):
                if (substring not in lookup):
                    lookup[substring] = 0
                lookup[substring] += 1

                output = max(output, lookup[substring])

            j += 1

        return output