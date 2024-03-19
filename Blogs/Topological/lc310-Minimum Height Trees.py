from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges):
        res = []
        if n == 1:
            res.append(0)
            return res
        degree = [0] * n
        graph = defaultdict(list)
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        dq = deque()
        for i in range(n):
            if degree[i] == 1:
                dq.append(i)
        while dq:
            res = []
            size = len(dq)
            for i in range(size):
                cur = dq.popleft()
                res.append(cur)
                neighbors = graph[cur]
                for neighbor in neighbors:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        dq.append(neighbor)
        return res