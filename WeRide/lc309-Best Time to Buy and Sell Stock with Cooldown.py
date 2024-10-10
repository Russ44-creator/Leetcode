from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        # dp[i] = [持有一只股票，持有0只股票且在冷冻期，持有0只股票且不在冷冻期]
        dp[0] = [-prices[0], 0, 0]
        for i in range(1, n):
            p = prices[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - p)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + p)
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        return max(dp[n - 1])