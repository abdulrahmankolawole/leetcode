var maxScore = function(cardPoints, k) {
    let score = 0
    let maxScore = 0
    let totalScore = cardPoints.reduce((a, b)=> a + b)
    let windowSum = 0
    let windowSize = cardPoints.length - k

    for (let i = 0; i < windowSize; i++) {
        windowSum += cardPoints[i]
    }   

    maxScore = totalScore - windowSum
    for (let i = windowSize; i < cardPoints.length; i++) {
        windowSum += cardPoints[i] - cardPoints[i - windowSize]
        score = totalScore - windowSum
        maxScore = Math.max(score, maxScore)
    }

    return maxScore

};