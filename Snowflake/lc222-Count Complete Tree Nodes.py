# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, root:TreeNode):
        height = 0
        while root:
            root = root.left
            height += 1
        return height

    def countNodes(self, root) -> int:
        if not root:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        if leftHeight == rightHeight: # 左边是完全树
            return (2 ** leftHeight - 1) + self.countNodes(root.right) + 1
        else:
            return (2 ** rightHeight - 1) + self.countNodes(root.left) + 1
