from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # if k == 0:
        #     return 0
        
        n = len(s)
        count = Counter(s)
        
        # Check if we have enough of each character in the entire string
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1
        
        # We will use sliding window to find the longest middle substring
        # where the characters outside (taken from ends) still satisfy >= k of each
        lookup = {'a': 0, 'b': 0, 'c': 0}
        i = 0
        j = 0
        output = 0
        
        while j < len(s):
            lookup[s[j]] += 1
            
            # Shrink from i while the current window (middle) makes any char taken < k
            while (count['a'] - lookup['a'] < k or
                   count['b'] - lookup['b'] < k or
                   count['c'] - lookup['c'] < k):
                lookup[s[i]] -= 1
                i += 1
            
            # After shrinking, the lookupent window [i..j] is valid middle
            output = max(output, j - i + 1)
            j += 1
        
        # Minimum characters taken = total length - longest valid middle
        return n - output