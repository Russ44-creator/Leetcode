# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        self.ans = float('-inf')
        # node = root
        def dfs(node):
            # nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = 0 if left < 0 else left
            right = 0 if right < 0 else right
            self.ans = max(self.ans, left + right + node.val)
            return max(left + node.val, right + node.val)
        dfs(root)
        return self.ans