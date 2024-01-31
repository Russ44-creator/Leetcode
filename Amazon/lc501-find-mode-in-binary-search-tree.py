# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode):
        stack = []
        pre = None
        cnt = 0
        maxCnt = 0
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                cur = stack.pop()
                if pre == None:
                    cnt = 1
                elif pre.val == cur.val:
                    cnt += 1
                else:
                    cnt = 1
                if cnt == maxCnt:
                    res.append(cur.val)
                if cnt > maxCnt:
                    maxCnt = cnt
                    res = [cur.val]
                pre = cur
                root = cur.right
        return res
