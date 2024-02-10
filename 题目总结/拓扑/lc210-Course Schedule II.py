from collections import defaultdict, deque

class Solution:
    def findOrder(self, n: int, edges):
        graph = defaultdict(list)
        indegree = defaultdict(lambda: 0)
        for i in range(n):
            indegree[i] = 0
        q = deque()
        ans = []
        for nxt, pre in edges:
            graph[pre].append(nxt)
            indegree[nxt] += 1
        for key, value in indegree.items():
            if value == 0:
                q.append(key)
        while q:
            cur = q.popleft()
            ans.append(cur)
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return ans if len(ans) == n else []
