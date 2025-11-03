var maxProfit = function(prices) {
    let k = 0
    let i = 1
    let maxProfit = 0

    while (i < prices.length) {
        if (prices[i] > prices[k]) {
            profit = prices[i] - prices[k]
            maxProfit = Math.max(profit, maxProfit)
        }
        else {
            k = i
        }

        i ++
    }

    return maxProfit
};