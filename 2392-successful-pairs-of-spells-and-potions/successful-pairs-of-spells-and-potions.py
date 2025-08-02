class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        output = []

        def bs(spell):
            i = 0
            j = len(potions) - 1
        
            while (i <= j):
                mid = (i + j) // 2

                if (potions[mid] * spell >= success):
                    j = mid - 1
                else:
                    i = mid + 1

            return i

        for spell in spells:
            pairs = bs(spell)
            output.append(len(potions) - pairs)

        return output

        