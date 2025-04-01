class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        output = 0

        while (j < len(prices)):
            if (prices[j] > prices[i]):
                profit = prices[j] - prices[i]
                output = max(output, profit)
            else:
                i = j
            
            j +=1
        
        return output