class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookup1 = {}
        size = len(s1)

        if (len(s1) > len(s2)):
            return False

        for char in s1:
            if (char not in lookup1):
                lookup1[char] = 0
            lookup1[char] += 1

        j = size
        lookup2 = {}

        for i in range(size):
            if (s2[i] not in lookup2):
                lookup2[s2[i]] = 0
            lookup2[s2[i]] += 1

        if (lookup1 == lookup2):
            return True

        while (j < len(s2)):
            if (s2[j] not in lookup2):
                lookup2[s2[j]] = 0
            lookup2[s2[j]] += 1

            if lookup2[s2[j - size]] == 1:
                del lookup2[s2[j - size]]
            else:
                lookup2[s2[j - size]] -= 1

            if (lookup1 == lookup2):
                return True

            j += 1

        return False       
        