from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0]*n for _ in range(m)]   # memoization matrix to store the length of the longest increasing path starting from each cell
        res = 0   # maximum length of the increasing path found so far

        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            path = 1
            for x, y in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i+x < m and 0 <= j+y < n and matrix[i+x][j+y] > matrix[i][j]:   # if the neighbor has a greater value, move to it
                    path = max(path, 1 + dfs(i+x, j+y))   # update the length of the increasing path
            memo[i][j] = path   # memoize the length of the increasing path starting from the current cell
            return path
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))   
        return res