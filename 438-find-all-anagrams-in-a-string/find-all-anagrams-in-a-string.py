class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slookup = Counter(s[:len(p)])
        plookup = Counter(p)
        output = []
        if (len(s) < len(p)):
            return output

        if (plookup == slookup):
            output.append(0)

        for i in range(len(p), len(s)):
            if (s[i] not in slookup):
                slookup[s[i]] = 0
            slookup[s[i]] += 1
            if (slookup[s[i - len(p)]] == 1):
                slookup.pop(s[i - len(p)])
            else:
                slookup[s[i - len(p)]] -= 1

            if (plookup == slookup):
                output.append(i - len(p) + 1)

        return output

        

    

        