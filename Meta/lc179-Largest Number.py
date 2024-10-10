from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # strs = map(str, nums)
        strs = []
        for num in nums:
            strs.append(str(num))
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'