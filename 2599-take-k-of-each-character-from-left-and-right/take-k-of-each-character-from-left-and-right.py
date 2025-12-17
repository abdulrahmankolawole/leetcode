class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = Counter(s)
        
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1
        
        i = 0
        j = 0
        output = float("inf")
        
        while j < len(s):
            count[s[j]] -= 1
            
            while (count['a'] < k or
                   count['b'] < k or
                   count['c'] < k):
                count[s[i]] += 1
                i += 1
            
            output = min(output,len(s) - (j - i + 1))
            j += 1
        
        return output