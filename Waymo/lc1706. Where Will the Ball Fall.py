class Solution:
    def fall(self, grid, row, col, x, y):
        if y == row:
            return x
        if x == 0 and grid[y][x] == -1:
            return -1
        if x == col - 1 and grid[y][x] == 1:
            return -1
        if grid[y][x] == 1 and grid[y][x + 1] == -1:
            return -1
        if grid[y][x] == -1 and grid[y][x - 1] == 1:
            return -1
        return self.fall(grid, row, col, x + grid[y][x], y + 1)

    def findBall(self, grid):
        row, col = len(grid), len(grid[0])
        ans = [0] * col
        for i in range(col):
            ans[i] = self.fall(grid, row, col, i, 0)
        return ans