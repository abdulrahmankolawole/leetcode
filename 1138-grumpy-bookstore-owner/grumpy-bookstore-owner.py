class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        i = 0
        j = 0
        window = 0
        max_window = 0
        satisfied = 0

        while (j < len(customers)):
            if (grumpy[j]):
                window += customers[j]
            else:
                satisfied += customers[j]

            if (j - i + 1 > minutes):
                if (grumpy[i]):
                    window -= customers[i]
                i += 1
            max_window = max(window, max_window)

            j += 1

        return satisfied + max_window