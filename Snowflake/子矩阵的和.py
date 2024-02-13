# 前序和 二维
class NumMatrix:
    def __init__(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        # 前缀和数组的行列数各自加1, 这样下标0就代表空矩阵的情况, 对应前缀和也是初始值0
        self.sums = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                # 当前格子值+左侧子矩阵+上侧子矩阵-左上侧子矩阵
                self.sums[r + 1][c + 1] = matrix[r][c] + self.sums[r][c + 1] + self.sums[r + 1][c] - self.sums[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 右下侧子矩阵-左侧子矩阵-上侧子矩阵+左上侧子矩阵
        return self.sums[row2 + 1][col2 + 1] - self.sums[row1][col2 + 1] - self.sums[row2 + 1][col1] + self.sums[row1][col1]