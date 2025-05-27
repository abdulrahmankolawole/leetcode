class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(string):
            i = 0
            j = len(string) - 1

            while (i < j):
                if (string[i] != string[j]):
                    return False
                i += 1
                j -= 1

            return True

        a = 0
        b = len(s) - 1

        while (a < b):
            if (s[a] != s[b]):
                return isPalindrome(s[:a] + s[a + 1:]) or isPalindrome(s[:b] + s[b + 1:])
            a += 1
            b -= 1

        return True
        