class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        output = 0
        N = len(colors)
        i = 0
        j = 1

        while (j < N + 2):
            
            if (colors[j % N] == colors[(j - 1) % N]):
                i = j
            
            while (j - i + 1 > 3):
                i += 1

            if (j - i + 1 == 3):
                output += 1

            j += 1
            
        return output
            