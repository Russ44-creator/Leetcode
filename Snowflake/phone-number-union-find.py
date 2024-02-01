phone_list = [[0, 10, 789], [1, 10, 45], [2, 34, 3234], [3, 300, 45], [4, 300, 678]]
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}

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
        self.parent[root_b] = root_a

id_map, number_map = defaultdict(list), defaultdict(list)
for phone in phone_list:
    id_map[phone[1]].append(phone[0])
    number_map[phone[2]].append(phone[0])

uf = UnionFind()
for i in range(len(phone_list)):
    uf.parent[i] = i
for key, value in id_map.items():
    if len(value) > 1:
        for i in range(1, len(value)):
            uf.union(value[i - 1], value[i])
for key, value in number_map.items():
    if len(value) > 1:
        for i in range(1, len(value)):
            uf.union(value[i - 1], value[i])
            
res_dict = {}
for i in uf.parent:
    rootNode = uf.find(i)
    if rootNode in res_dict:
        res_dict[rootNode].append(i)
    else:
        res_dict[rootNode] = [i]

print(res_dict)

