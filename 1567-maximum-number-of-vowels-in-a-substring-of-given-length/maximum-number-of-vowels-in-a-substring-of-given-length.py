class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        my_set = {"a", "e", "i", "o", "u"}
        count = 0
        max_count = 0

        for i in range(k):
            if (s[i] in my_set):
                count += 1
        
        max_count = max(count, max_count)
        for i in range(k, len(s)):
            if (s[i] in my_set):
                count += 1
            if (s[i - k] in my_set):
                count -= 1
            max_count = max(count, max_count)

        
        return max_count
            
                

        