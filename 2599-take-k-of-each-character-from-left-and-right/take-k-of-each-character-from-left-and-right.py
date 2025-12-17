class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        lookup = Counter(s)
        def atLeastK():
            if (lookup["a"] < k or lookup["b"] < k or lookup["c"] < k):
                return False
            return True
        
        if (not atLeastK()):
            return -1

        i = 0
        j = 0
        output = float("inf")

        while (j < len(s)):
            lookup[s[j]] -= 1

            while (not atLeastK()):
                lookup[s[i]] += 1
                i += 1

            output = min(output, len(s) - (j - i + 1))
            j += 1


        return output

        