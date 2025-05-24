class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_score = sum(cardPoints)
        window_size = len(cardPoints) - k
        window_score = sum(cardPoints[:window_size])
        # current_score = total_score - window_score
        output = total_score - window_score

        for i in range(window_size, len(cardPoints)):
            window_score += cardPoints[i] - cardPoints[i - window_size]
            output = max(output, total_score - window_score)

        return output


        