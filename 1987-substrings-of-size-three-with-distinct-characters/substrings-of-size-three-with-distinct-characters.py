class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        lookup = {}
        count = 0
        result = 0

        for i in range(3):
            if (s[i] not in lookup):
                lookup[s[i]] = 0
                count += 1

            lookup[s[i]] += 1

        if (count == 3):
            result += 1

        for i in range(3, len(s)):
            if (s[i] not in lookup):
                count += 1
                lookup[s[i]] = 0
            lookup[s[i]] += 1

            if(lookup[s[i - 3]] == 1):
                lookup.pop(s[i - 3])
                count -= 1
            else:
                lookup[s[i - 3]] -= 1

            if (count == 3):
                result += 1

        return result


