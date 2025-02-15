class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_score = sum(cardPoints)
        n = len(cardPoints)
        window = n - k
        score = sum(cardPoints[:window])
        result = total_score - score

        for idx in range(n - window):
            score = score - cardPoints[idx] + cardPoints[idx + window]
            result = max(result, total_score - score)

        return result
