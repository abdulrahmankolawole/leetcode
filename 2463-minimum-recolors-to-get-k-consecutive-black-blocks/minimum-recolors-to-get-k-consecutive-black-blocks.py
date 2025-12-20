class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        j = 0
        output = float("inf")
        window_blacks = 0

        while (j < len(blocks)):
            block = blocks[j]

            if (block == "B"):
                window_blacks += 1

            while (j - i + 1 > k):
                if (blocks[i] == "B"):
                    window_blacks -= 1
                i += 1

            if (j - i + 1 == k):
                recolors = j - i + 1 - window_blacks
                output = min(recolors, output)

            j += 1

        return output
        