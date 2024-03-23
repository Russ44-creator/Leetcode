class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        n = len(cardPoints)
        m = n - k
        min_s = s = sum(cardPoints[:m])
        for i in range(m, n):
            s += cardPoints[i] - cardPoints[i - m]
            min_s = min(min_s, s)
        return sum(cardPoints) - min_s