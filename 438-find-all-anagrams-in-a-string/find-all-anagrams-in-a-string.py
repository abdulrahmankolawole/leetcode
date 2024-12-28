class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        if (len(s) < len(p)):
            return output
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)])
        output = [0] if (sCounter == pCounter) else []

        i = 0
        j = len(p)

        while (j < len(s)):
            sCounter[s[j]] = 1 + sCounter.get(s[j], 0)
            sCounter[s[i]] -= 1 

            if (sCounter[s[i]] == 0):
                sCounter.pop(s[i])
            i += 1
        
            if (sCounter == pCounter):
                output.append(i)
            
            j += 1

        
        return output


        



        