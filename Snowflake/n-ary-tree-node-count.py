class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
    
import collections

class Solution:
    def count(self, node):
        res = 0
        if not node:
            return 0
        dq = collections.deque([node])
        while dq:
            n = dq.popleft()
            if n.children:
                for c in n.children:
                    dq.append(c)
                    res += 1
        return res