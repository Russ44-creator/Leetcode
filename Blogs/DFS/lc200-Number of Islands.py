from collections import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        if not grid:
            return 0

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    cnt += 1
        return cnt