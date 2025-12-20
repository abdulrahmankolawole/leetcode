class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        j = 0
        output = 0
        string = str(num)

        while (j <= len(string) - k):
            substr = string[j: j + k]
            numbr = int(substr)

            if (numbr != 0 and num % numbr == 0):
                output += 1

            j += 1

        return output

        
        