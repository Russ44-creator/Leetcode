def countMatches(grid1, grid2):
    count= 0
    m, n = len(grid1), len(grid1[0])
    g1 = [[0 for i in range(n)] for j in range(m)]
    g2 = [[0 for i in range(n)] for j in range(m)]
    ormap = [[0 for i in range(n)] for j in range(m)]
    
    for i in range(m):
        for j in range(n):
            g1[i][j] = grid1[i][j] 
            g2[i][j] = grid2[i][j]
    
    for i in range(m):
        for j in range(n):
            ormap[i][j] = grid1[i][j] or grid2[i][j]
            

    for i in range(m):
        for j in range(n):
            if ormap[i][j] == 1 and dfs(g1, g2, ormap, i, j):
                count += 1

            ormap[i][j] = grid1[i][j] or grid2[i][j]
            

    return count

def dfs(g1, g2, ormap, i, j):
    m, n = len(ormap), len(ormap[0])
    ormap[i][j] = 0
    # boolean up = true, down = true, left = true, right = true;
    up, down, left, right = True, True, True, True
    if i > 0 and ormap[i-1][j] ==1:
        up = dfs(g1, g2, ormap, i-1, j)
    if i < m - 1 and ormap[i + 1][j] == 1:
        down = dfs(g1, g2, ormap, i+1, j)
    if j > 0 and ormap[i][j - 1] == 1:
        left = dfs(g1, g2, ormap, i, j-1)
    if j < n - 1 and ormap[i][j + 1] == 1:
        right = dfs(g1, g2, ormap, i, j+1)
    return g1[i][j]==1 and g2[i][j]==1 and up and down and left and right;

m1 = [[1, 0, 1],[1, 1, 1], [1, 0, 0]]
m2 = [[1, 0, 1],[1, 0, 1], [1, 0, 1]]
print(countMatches(m1, m2))