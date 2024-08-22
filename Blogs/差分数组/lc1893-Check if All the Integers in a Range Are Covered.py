from collections import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diffsum = [0] * right
        for interval in ranges:
            start = interval[0] - 1
            end = interval[1]
            if start < right:
                diffsum[start] += 1
            if end < right:
                diffsum[end] -= 1
        for i in range(1, len(diffsum)):
            diffsum[i] += diffsum[i - 1]
        for i in range(left - 1, right):
            if diffsum[i] == 0:
                return False
        return True
