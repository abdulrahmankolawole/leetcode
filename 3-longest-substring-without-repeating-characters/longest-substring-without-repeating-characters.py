class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # output = 0
        # def isUnique(arr):
        #     lookup = set(arr)

        #     return len(arr) == len(lookup)

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         substr = s[i: j + 1]
        #         if (isUnique([char for char in substr])):
        #             output = max(output, len(substr))
        
        # return output


        lookup = set()
        i = 0
        j = 0
        output = 0

        while (j < len(s)):

            while (s[j] in lookup):
                lookup.remove(s[i])
                i += 1

            lookup.add(s[j])
            length = j - i + 1
            output = max(output, length)
            j += 1

        return output

        