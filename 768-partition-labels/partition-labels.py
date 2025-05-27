class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lookup = {}
        output = []
        for idx, val in enumerate(s):
            lookup[val] = idx
        
        lastIdx = 0
        size = 0
        for idx, val in enumerate(s):
            lastIdx = max(lastIdx, lookup[val])
            size += 1

            if (idx == lastIdx):
                output.append(size)
                size = 0

        return output


        