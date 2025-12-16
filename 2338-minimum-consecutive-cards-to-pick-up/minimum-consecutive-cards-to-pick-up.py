class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        i = 0
        j = 0
        output = float("inf")
        lookup = set()

        while (j < len(cards)):

            while (cards[j] in lookup):
                output = min(output, (j - i + 1))
                lookup.remove(cards[i])
                i += 1

            lookup.add(cards[j])
            j += 1
        
        return -1 if output == float("inf") else output