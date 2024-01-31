# lc 1514
from typing import List
from collections import defaultdict, deque

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g, dq = defaultdict(list), deque([start])
        for i, (a, b) in enumerate(edges):
            g[a].append([b, i])
            g[b].append([a, i])
        p = [0.0] * n    
        p[start] = 1.0
        while dq:
            cur = dq.popleft()
            for neighbor, i in g[cur]:
                if p[cur] * succProb[i] > p[neighbor]:
                    p[neighbor] = p[cur] * succProb[i]
                    dq.append(neighbor)
        return p[end]
