class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        # cnt统计奇数个数为odd出现的数组的位置
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                ans += cnt[odd - k]
            cnt[odd] += 1
        return ans