# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root):
        def dfs(root):
            if not root:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            depth = max(l, r) + 1
            res[depth].append(root.val)
            return depth
        res = collections.defaultdict(list)
        dfs(root)
        return [v for v in res.values()]