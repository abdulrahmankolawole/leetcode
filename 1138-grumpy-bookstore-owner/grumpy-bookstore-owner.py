class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        j = 0
        i = 0
        satisfied = 0
        max_window = 0
        window = 0

        while (j < len(customers)):
            if (grumpy[j] == 0):
                satisfied += customers[j]
            else:
                window += customers[j]

            if (j - i + 1 > minutes):
                if (grumpy[i]):
                    window -= customers[i]
                i += 1

            max_window = max(window, max_window)
            j += 1
            
        return max_window + satisfied

        