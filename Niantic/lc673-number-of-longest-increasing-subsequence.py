class Solution:
    def findNumberOfLIS(self, nums) -> int:
        dp = [[1, 1] for i in range(len(nums))]
        max_len = 1
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
            max_len = max(max_len, dp[i][0])
        return sum(item[1] for item in dp if item[0] == max_len)
                    