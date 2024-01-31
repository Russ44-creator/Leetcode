class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) <= 1: return True
        l, r = 0, nums[0]
        while r < len(nums) - 1:
            nxt = max(i + nums[i] for i in range(l, r + 1))
            if nxt == l:
                return False
            l, r = r, nxt
        return True