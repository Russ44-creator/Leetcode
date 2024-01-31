def leader(edges):
    graph = {}
    values = set()
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        values.add(v)
    
    count = {}
    def dfs(node):
        if node not in graph:
            count[node] = 0
            return 0
        if node in count:
            return count[node]
        if node not in count:
            count[node] = 0
        
        for nei in graph[node]:
            count[node] += 1 + dfs(nei)
        return count[node]
    
    start = graph.keys() - values
    for node in start:
        dfs(node)
    return count


input = [ ["A","B"] , ["B", "C"] ]
print(leader(input))