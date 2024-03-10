class Solution:
    def findSubsequences(self, nums):
        ans = []
        path = []

        def backtrack(i):
            if len(path) > 1:
                ans.append(path.copy())
            uset = set()
            for j in range(i, len(nums)):
                if (path and nums[j] < path[-1]) or nums[j] in uset:
                    continue
                uset.add(nums[j])
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()
        backtrack(0)
        return ans