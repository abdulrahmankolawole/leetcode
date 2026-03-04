class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key = lambda x: (-len(x), x))

        def isSubSeq(part, whole):
            i = 0
            j = 0

            while (j < len(whole) and i < len(part)):
                if (part[i] == whole[j]):
                    i += 1
                j += 1

            return i == len(part)

        output = ""    
        for word in dictionary:
            if (isSubSeq(word, s)):
                return word

        return output

        