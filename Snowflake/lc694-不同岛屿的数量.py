class Solution:
    def numDistinctIslands(self, grid) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        def dfs(r, c):
            if visited[r][c]:
                return
            visited[r][c] = 1
            nxt = [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]
            for i in range(4):
                nr, nc = nxt[i]
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    self.path += str(i + 1)
                    dfs(nr, nc)
        
        rec = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and visited[r][c] == False:
                    self.path = "0"
                    dfs(r, c)
                    print(self.path)
                    rec.add(self.path)
        return len(rec)