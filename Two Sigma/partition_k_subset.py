from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        reqsum = total // k
        subsets = [0] * k
        nums.sort(reverse = True)
        def recurse(i):
            if i == len(nums):
                return True
            for j in range(k):
                if subsets[j] + nums[i] <= reqsum:
                    subsets[j] += nums[i]
                    if recurse(i + 1):
                        return True
                    subsets[j] -= nums[i]
                    if subsets[j] == 0:
                        break
            return False
        return recurse(0)