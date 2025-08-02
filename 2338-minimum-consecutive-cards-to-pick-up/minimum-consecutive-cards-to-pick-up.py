class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        i = 0
        j = 0
        lookup = set()
        output = float("inf")

        while (j < len(cards)):
            card = cards[j]

            while (card in lookup):
                output = min(output, j - i + 1)
                lookup.remove(cards[i])
                i += 1

            lookup.add(card)
            j += 1

        return - 1 if output == float("inf") else output


        