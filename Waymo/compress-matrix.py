import collections

def compress_2D_array(A):
    m, n = len(A), len(A[0])
    aux = sorted(
        ((r, c) for r in range(m) for c in range(n)),
        key=lambda p: A[p[0]][p[1]]
    )
    for v, (r, c) in enumerate(aux, 1): A[r][c] = v
    return A

def compress_2D_array_followup(A):
    m, n = len(A), len(A[0])
    # Adjacency list of the directed graph
    G = collections.defaultdict(set)
    # For each node count the number of parent nodes
    cnt = {(r, c): 0 for r in range(m) for c in range(n)}
    # Sort each row, build graph and update counter
    for r, row in enumerate(A):
        order = sorted(range(n), key=lambda c: row[c])
        for c1, c2 in zip(order, order[1:]):
            G[(r, c1)].add((r, c2))
            cnt[(r, c2)] += 1
    print(G, cnt)
    # Sort each column, build graph and update counter
    for c, col in enumerate(zip(*A)):
        order = sorted(range(m), key=lambda r: col[r])
        for r1, r2 in zip(order, order[1:]):
            G[(r1, c)].add((r2, c))
            cnt[(r2, c)] += 1
    # Compress the matrix
    val = 1
    # Find nodes that have no parent in the graph
    peel = {k for k, v in cnt.items() if v == 0}
    while cnt:
        # Use to store node to peel in next round
        temp = set()
        # Modify matrix value at these nodes
        # Update the counter of their children
        # Peel children in next round if its counter becomes 0
        # Then peel these nodes from the graph
        for r, c in peel:
            for ch in G[(r, c)]: 
                cnt[ch] -= 1
                if cnt[ch] == 0: 
                    temp.add(ch)
            A[r][c] = val
            cnt.pop((r, c))
        val += 1
        peel = temp
    return A

A = [[7, 6], [4, 9]]
print(compress_2D_array_followup(A))