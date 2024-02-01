class Solution:
    def minMoves2(self, nums) -> int:
        nums.sort()
        return sum(abs(num - nums[len(nums) // 2]) for num in nums)