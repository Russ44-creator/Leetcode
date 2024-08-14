# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 1
        if root.left:
            max_depth = max(max_depth, 1 + self.maxDepth(root.left))
        if root.right:
            max_depth = max(max_depth, 1 + self.maxDepth(root.right))
        return max_depth
