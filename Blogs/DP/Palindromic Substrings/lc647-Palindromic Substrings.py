class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 1
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(0, len(s)):
            dp[i][i] = True
        res = len(s)
        for j in range(1, len(s)):
            for i in range(0, j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    res += 1
        return res