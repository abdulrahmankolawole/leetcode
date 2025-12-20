var maxScore = function(cardPoints, k) {
    let total = cardPoints.reduce((a, b)=> a + b, 0)
    let windowSize = cardPoints.length - k
    let windowSum = 0
    minWindowSum = Infinity
    let output = 0

    for (let i = 0; i < windowSize; i++) {
        windowSum += cardPoints[i]
    }

    output = total - windowSum

    for (let i = windowSize; i < cardPoints.length; i++) {
        windowSum += cardPoints[i] - cardPoints[i - windowSize]
        minWindowSum = Math.min(windowSum, minWindowSum)
    }
    
    return Math.max(total - minWindowSum, output)

};