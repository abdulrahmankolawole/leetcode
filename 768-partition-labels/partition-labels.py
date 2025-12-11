class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lookup = {}
        output = []
        size = 0
        end = 0

        for i in range(len(s)):
            lookup[s[i]] = i

        for i in range(len(s)):
            size += 1
            end = max(end, lookup[s[i]])

            if (i == end):
                output.append(size)
                size =0
        return output
             
        