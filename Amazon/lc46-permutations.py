from collections import Counter

class Solution:
    def permute(self, nums):
        res = []
        def dfs(counter, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path + [x])
                    counter[x] += 1
        dfs(Counter(nums), [])
        return res