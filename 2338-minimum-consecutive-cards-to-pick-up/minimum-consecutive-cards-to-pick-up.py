class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        i = 0
        j = 0
        output = float("inf")
        lookup = set()

        while (j < len(cards)):
            card = cards[j]

            while (card in lookup):
                lookup.remove(cards[i])
                output = min(output, j - i + 1)
                i += 1

            lookup.add(card)
            j += 1
        
        return output if output != float("inf") else -1
        