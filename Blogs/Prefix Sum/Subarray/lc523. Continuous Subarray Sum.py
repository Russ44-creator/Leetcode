class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        # 23, 25, 29
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        s = set()
        for i in range(2, n + 1):
            s.add(prefix_sum[i - 2] % k)
            if prefix_sum[i] % k in s:
                return True
        return False
        