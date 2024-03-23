class Solution:
    def shortestDistance(self, grid) -> int:
        Row, Col = len(grid), len(grid[0])
        canget_from_1 = [[0 for _ in range(Col)] for _ in range(Row)]  #空地，有多少个建筑物可以到达
        dist_sum_from_1 = [[0 for _ in range(Col)] for _ in range(Row)]    #空地， 可以到达的建筑物们的距离和
        cnt_1 = 0           #建筑物1的数量
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 1:
                    cnt_1 += 1
                    Q = []
                    Q.append((r, c, 0))
                    visited = [[False for _ in range(Col)] for _ in range(Row)]
                    while Q:
                        i, j, d = Q.pop(0)
                        for ni, nj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                            if (0 <= ni < Row) and (0 <= nj < Col) and (grid[ni][nj] == 0) and (visited[ni][nj] == False):
                                canget_from_1[ni][nj] += 1
                                dist_sum_from_1[ni][nj] += (d + 1)
                                Q.append((ni, nj, d + 1))
                                visited[ni][nj] = True
        res = float('inf')
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 0:
                    if canget_from_1[r][c] == cnt_1:
                        res = min(res, dist_sum_from_1[r][c])
        return res if res != float('inf') else -1