# Definition for a binary tree node.
# dfs递归 把值加在最后
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def boundaryOfBinaryTree(self, root):
        if root and not root.left and not root.right:
            return [root.val]
        Left = []
        Bottom = []
        Right = []
        def dfsLeft(root):
            if root and (root.left or root.right):
                Left.append(root.val)
                if root.left:
                    dfsLeft(root.left)
                else:
                    dfsLeft(root.right)
        def dfsBottom(root):
            if root:
                if not root.left and not root.right:
                    Bottom.append(root.val)
                else:
                    dfsBottom(root.left)
                    dfsBottom(root.right)
        
        def dfsRight(root):
            if root and (root.left or root.right):
                Right.append(root.val)
                if root.right:
                    dfsRight(root.right)
                else:
                    dfsRight(root.left)
        dfsLeft(root.left)
        dfsBottom(root)
        dfsRight(root.right)
        return [root.val] + Left + Bottom + Right[::-1]