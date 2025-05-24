class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        def hasAllThree():
            
            if (("a" not in lookup) or ("b" not in lookup) or ("c" not in lookup)):
                return False
            if (lookup["a"] < 1 or lookup["b"] < 1 or lookup["c"] < 1):
                return False
            return True

        i = 0
        j = 0
        output = 0
        lookup = {}

        while (j < len(s)):
            char = s[j]
            if (char not in lookup):
                lookup[char] = 0
            lookup[char] += 1

            while (hasAllThree()):
                output += len(s) - j
                lookup[s[i]] -=1
                i += 1

            j += 1

        return output