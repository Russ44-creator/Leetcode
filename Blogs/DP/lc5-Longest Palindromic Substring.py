class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ans = max
        # dp[i][j] = dp[i+1][j-1]
        if len(s) < 2:
            return s
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(0, len(s)):
            dp[i][i] = True
        maxLen = 1
        begin = 0
        for j in range(1, len(s)):
            for i in range(0, j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    begin = i
        return s[begin:begin+maxLen]
