# https://www.1point3acres.com/bbs/thread-967100-1-1.html

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root) -> bool:
        q = deque([root])
        gap = False
        while q:
            poping = q.popleft()
            if not poping:
                gap = True
            else:
                if gap:
                    return False
                q.append(poping.left)
                q.append(poping.right)
        return True
