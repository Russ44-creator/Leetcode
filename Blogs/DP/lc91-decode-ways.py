class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        a = ord(s[0]) - ord('0')
        if 1 <= a <= 9:
            dp[1] = dp[0]
        for i in range(2, n + 1):
            a = ord(s[i - 1]) - ord('0')
            b = (ord(s[i - 2]) - ord('0')) * 10 + ord(s[i - 1]) - ord('0')
            if 1 <= a <= 9:
                dp[i] = dp[i - 1]
            if 10 <= b <= 26:
                dp[i] += dp[i - 2]
        return dp[n]
            