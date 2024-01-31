from collections import defaultdict

class Node(object):
    # 初始化一个节点
    def __init__(self,value = None):
        self.value = value  # 节点值
        self.child_list = []    # 子节点列表
    # 添加一个孩子节点
    def add_child(self,node):
        self.child_list.append(node)


# 初始化一颗测试二叉树
def init():
    '''
    初始化一颗测试二叉树:
            A
        B   C   D
      EFG       HIJ
    '''
    root = Node('A')
    B = Node('B')
    root.add_child(B)
    root.add_child(Node('C'))
    D = Node('D')
    root.add_child(D)
    B.add_child(Node('E'))
    B.add_child(Node('F'))
    B.add_child(Node('G'))
    D.add_child(Node('H'))
    D.add_child(Node('I'))
    D.add_child(Node('J'))
    return root

r = init()

def dfs(root):
    if not root:
        return (0, 0)
    temp = []

    for child in root.child_list:
        temp.append(dfs(child))
    # pick root
    ans = 1
    for i in temp:
        ans += i[1]
    # not pick root
    ans2 = 0
    for i in temp:
        ans2 += max(i[0], i[1])
    return (ans, ans2)

print(max(dfs(r)))
    
    