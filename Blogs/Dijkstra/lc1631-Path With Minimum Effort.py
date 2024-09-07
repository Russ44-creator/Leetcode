from typing import List
from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
      m, n = len(heights), len(heights[0])
      queue = deque()
      queue.append((0, 0))
      cost = { (row, col): float('inf') for col in range(n) for row in range(m) }
      cost[(0, 0)] = 0
      dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
      while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < m and 0 <= new_y < n:
                new_cost = max(cost[(x, y)], abs(heights[new_x][new_y] - heights[x][y]))
                if new_cost < cost[(new_x, new_y)]:
                    cost[(new_x, new_y)] = new_cost
                    queue.append((new_x, new_y))
      return cost[(m - 1, n - 1)]
