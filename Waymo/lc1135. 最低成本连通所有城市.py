class Solution:
    def find(self, x):
        if x == self.father[x]:
            return x
        return self.find(self.father[x])

    def minimumCost(self, n: int, connections) -> int:
        self.father = [i for i in range(n + 1)]
        connections.sort(key=lambda edge: edge[2])
        ans = 0
        edge_cnt = 0
        for a, b, cost in connections:
            root_a = self.find(a)
            root_b = self.find(b)
            if root_a != root_b:
                self.father[root_a] = root_b
                ans += cost
                edge_cnt += 1
            if edge_cnt == n - 1:
                return ans
        return -1