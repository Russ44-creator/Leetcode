import collections
# 从目标开始BFS 
class Solution:
    def wallsAndGates(self, rooms) -> None:
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        if m == 0:
            return
        queue = collections.deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in [[0,1], [1, 0], [0, -1], [-1, 0]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                    rooms[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))