
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

import collections
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        queue = collections.deque([p, q])
        while queue:
            curr = queue.popleft()
            if curr in seen:
                return curr
            seen.add(curr)
            if curr.parent:
                queue.append(curr.parent)