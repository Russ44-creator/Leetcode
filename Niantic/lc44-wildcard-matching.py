class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s) + 1
        p_len = len(p) + 1
        dp = [[False] * p_len for _ in range(s_len)]
        dp[0][0] = True
        for j in range(1, p_len):
            if p[j - 1] != "*":
                break
            dp[0][j] = True
        for i in range(1, s_len):
            for j in range(1, p_len):
                if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]