from collections import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0, float('inf'), -float('inf')
            
            N1, n1, min1, max1 = dfs(node.left)
            N2, n2, min2, max2 = dfs(node.right)

            if node.val > max1 and node.val < min2:
                n = 1 + n1 + n2
            else:
                n = -float('inf')
            
            return max(n, N1, N2), n, min(min1, node.val), max(max2, node.val)
        return dfs(root)[0]

