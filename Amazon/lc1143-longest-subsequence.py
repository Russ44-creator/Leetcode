class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[[0, ""] for i in range(len(text2) + 1)]for j in range(len(text1) + 1)]
        for i in range(1, len(text1)+ 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j][0] = 1 + dp[i - 1][j - 1][0]
                    dp[i][j][1] = dp[i - 1][j - 1][1] + text1[i-1]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0])
                    dp[i][j][1] = dp[i - 1][j][1] if dp[i - 1][j][0] > dp[i][j - 1][0] else dp[i][j - 1][1]
        print(dp[-1][-1][1])
        
        return dp[-1][-1][0]