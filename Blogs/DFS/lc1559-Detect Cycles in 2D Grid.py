from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool: 
        m, n = len(grid), len(grid[0])
        seen = set()
        def dfs(node, p):
            if node in seen: return True
            seen.add(node)
            i, j = node
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) != p and grid[x][y] == grid[i][j]:
                    if dfs((x, y), node): return True
            return False
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and dfs((i, j), None):
                    return True
        
        return False