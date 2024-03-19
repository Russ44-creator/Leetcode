class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        output, stack = [], []
        def backtrack(i):
            if i >= len(nums):
                output.append(stack.copy())
                return
            stack.append(nums[i])
            backtrack(i + 1)
            stack.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        backtrack(0)
        return output