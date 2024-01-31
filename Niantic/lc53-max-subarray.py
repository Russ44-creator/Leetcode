class Solution:
    def maxSubArray(self, nums) -> int:
        # maxsum = float('-inf')
        # currentsum = 0
        # for num in nums:
        #     currentsum += num
        #     if currentsum > maxsum:
        #         maxsum = currentsum
        #     if currentsum < 0:
        #         currentsum = 0
        # return maxsumw
        dp = [*nums]
        print(dp)
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)