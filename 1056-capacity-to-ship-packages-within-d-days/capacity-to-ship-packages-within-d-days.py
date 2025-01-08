class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(weight):
            current_weight = 0
            no_of_days = 1

            for amount in weights:
                current_weight += amount
                if (current_weight > weight):
                    no_of_days += 1
                    current_weight = amount
            
            return no_of_days <= days

        
        i = max(weights)
        j = sum(weights)

        while (i <= j):
            mid = (i + j) // 2

            if (canShip(mid)):
                j = mid - 1
            else:
                i = mid + 1

        
        return i