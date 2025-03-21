class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        lookup = {}
        result = []
        j = 0

        while (j < len(s) - 9):
            substring = s[j: j + 10]

            if (substring not in lookup):
                lookup[substring] = 0
            lookup[substring] += 1

            if (lookup[substring] == 2):
                result.append(substring)

            j +=1

        return result 
