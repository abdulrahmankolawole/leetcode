class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)

        def canEat(k):
            amount = 0
            for pile in piles:
                rate = math.ceil(pile / k)
                amount += rate
            
            return amount <= h

        while (i <= j):
            mid = (i + j) // 2

            if (canEat(mid)):
                j = mid - 1
            else:
                i = mid + 1

        return i


        