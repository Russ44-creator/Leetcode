class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections, math

def construct(root):
    if not root:
        return root
    allCount = 0
    countPerLevel = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        size = len(queue)
        countPerLevel.append(size)
        allCount += size
        for i in range(size):
            cur = queue.popleft()
            if cur.left != None:
                queue.append(cur.left)
            if cur.right != None:
                queue.append(cur.right)
    needAdd = 0
    needDelete = allCount - 1
    minOperations = needDelete
    idealHeight = 0
    for i in range(1, len(countPerLevel)):
        needDelete -= countPerLevel[i]
        needAdd += math.pow(2, i - 1) - countPerLevel[i-1]
        operations = needAdd + needDelete
        if operations < minOperations:
            minOperations = operations
            idealHeight = i
    
    newRoot = TreeNode()
    queue.append(newRoot)
    curHeight = 0
    while curHeight < idealHeight - 1:
        size = len(queue)
        for i in range(size):
            cur = queue.popleft()
            cur.left = TreeNode()
            cur.right = TreeNode()
            queue.append(cur.left)
            queue.append(cur.right)
        curHeight += 1
    lastLevelCount = countPerLevel[idealHeight]
    i = 0
    while i < lastLevelCount:
        cur = queue.popleft()
        cur.left = TreeNode()
        i += 1
        if i == lastLevelCount:
            break
        cur.right = TreeNode()
        i += 1
    return newRoot
