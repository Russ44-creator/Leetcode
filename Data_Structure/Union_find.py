class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.components = n
    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        return root
    def union(self, A, B):
        root_a = self.find(A)
        root_b = self.find(B)
        if root_a == root_b:
            return
        self.parent[root_a] = root_b
        self.components -= 1