from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        n = len(s)
        count = Counter(s)
        
        # Check if we have enough of each character in the entire string
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1
        
        # We will use sliding window to find the longest middle substring
        # where the characters outside (taken from ends) still satisfy >= k of each
        curr = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        max_middle = 0
        
        for right in range(n):
            curr[s[right]] += 1
            
            # Shrink from left while the current window (middle) makes any char taken < k
            while (count['a'] - curr['a'] < k or
                   count['b'] - curr['b'] < k or
                   count['c'] - curr['c'] < k):
                curr[s[left]] -= 1
                left += 1
            
            # After shrinking, the current window [left..right] is valid middle
            max_middle = max(max_middle, right - left + 1)
        
        # Minimum characters taken = total length - longest valid middle
        return n - max_middle