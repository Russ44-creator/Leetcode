from collections import List
import heapq

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        directions = {
            'u': (-1, 0),
            'd': (1, 0),
            'l': (0, -1),
            'r': (0, 1)
        }
        m = len(maze)
        n = len(maze[0])

        visited = set()
        queue = []
        heapq.heappush(queue, (0, '', ball[0], ball[1]))
        visited.add(('', ball[0], ball[1]))

        while queue:
            dist, inst, i, j = heapq.heappop(queue)
            if (i, j) == (hole[0], hole[1]):
                return inst
            if inst:
                # see if the ball is still moving from last instruction
                di, dj = directions[inst[-1]]
                ni, nj = i + di, j + dj
                if (0 <= ni < m) and (0 <= nj < n) and maze[ni][nj] == 0:
                    # we have to continue moving in current direction
                    heapq.heappush(queue, (dist + 1, inst, ni, nj))
                    continue

            for direction in directions:
                di, dj = directions[direction]
                ni, nj = i + di, j + dj
                if not ((0 <= ni < m) and (0 <= nj < n)):
                    continue
                if maze[ni][nj] == 1:
                    continue
                if (direction, ni, nj) in visited:
                    continue
                heapq.heappush(queue, (dist + 1, inst + direction, ni, nj))
                visited.add((direction, ni, nj))
                
        return 'impossible'
    