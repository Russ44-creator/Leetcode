class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n = len(coins)
        dp = [[amount+1] * (amount+1) for _ in range(n+1)]    
        dp[0][0] = 0    # 其他 dp[0][j]均不合法
        
        for i in range(1, n+1):          
            for j in range(amount+1):       
                if j < coins[i-1]:        
                    dp[i][j] = dp[i-1][j]
                else:                       
                    dp[i][j] = min( dp[i-1][j], dp[i][j-coins[i-1]] + 1 )

        ans = dp[n][amount] 
        return ans if ans != amount+1 else -1