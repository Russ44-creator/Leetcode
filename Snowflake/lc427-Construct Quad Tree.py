# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def isQuadTree(self, grid):
        len_ = len(grid)
        sum_ = 0
        for i in range(len_):
            sum_ += sum(grid[i])
        if sum_ == len_ ** 2:
            return True
        elif sum_ == 0:
            return False
        else:
            return None

    def construct(self, grid) -> 'Node':
        isLeaf = self.isQuadTree(grid)
        _len = len(grid)
        if isLeaf == None:
            mid = _len // 2
            topLeftGrid = [[grid[i][j] for j in range(mid)] for i in range(mid)]
            topRightGrid = [[grid[i][j] for j in range(mid, _len)] for i in range(mid)]
            bottomLeftGrid = [[grid[i][j] for j in range(mid)] for i in range(mid, _len)]
            bottomRightGrid = [[grid[i][j] for j in range(mid, _len)] for i in range(mid, _len)]
            node = Node(True, False, self.construct(topLeftGrid), self.construct(topRightGrid), 
                        self.construct(bottomLeftGrid), self.construct(bottomRightGrid))
            return node
        elif isLeaf == False:
            return Node(False, True, None, None, None, None)
        else:
            return Node(True, True, None, None, None, None)