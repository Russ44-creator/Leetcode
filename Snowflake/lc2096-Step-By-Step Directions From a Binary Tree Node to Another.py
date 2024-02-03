# https://www.1point3acres.com/bbs/thread-981138-1-1.html


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getDirections(self, root, startValue: int, destValue: int) -> str:
        path = []
        def find(node, val):
            if not node:
                return False
            if node.val == val:
                return True
            path.append((node.val,"L"))
            if find(node.left, val):
                return True
            path.pop()
            path.append((node.val,"R"))
            if find(node.right, val):
                return True
            path.pop()
            return False
            
        
        find(root, startValue)
        path_s = path
        path = []
        find(root, destValue)
        i = 0
        while i < len(path_s) and i < len(path) and path_s[i] == path[i]:
            i += 1
        return "U" * (len(path_s) - i) + "".join(list(zip(*path))[1][i:]) if path else "U" * len(path_s)
