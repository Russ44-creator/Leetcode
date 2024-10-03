from typing import List
import collections

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        matrix = collections.defaultdict(list)
        for i in range(n):
            for j in range(len(nums[i])):
                # 因为是左上往右下遍历，后遍历的对象插入到前面
                matrix[i+j].insert(0, nums[i][j])
        res = []
        for val in matrix.values():
            res += val
        return res
