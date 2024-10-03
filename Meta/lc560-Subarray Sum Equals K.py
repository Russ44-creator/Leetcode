from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x

        ans = 0
        cnt = defaultdict(int)
        for sj in s:
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans