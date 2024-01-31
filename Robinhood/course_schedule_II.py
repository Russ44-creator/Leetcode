# lc 210

class Solution:
    def findOrder(self, numVertices, edges):
        visited = set()
        sortedList = []
        depsDict = {vertex: set() for vertex in range(numVertices)}
        for node, dep in edges:
            depsDict[node].add(dep)
            
        noDeps = [vertex for vertex, deps in depsDict.items() if len(deps) == 0 and vertex not in visited]
        while noDeps:
            vertex = noDeps.pop()
            visited.add(vertex)
            sortedList.append(vertex)
            
            for node, dep in depsDict.items():
                if vertex in depsDict[node]:
                    depsDict[node].remove(vertex)
            
            noDeps = [vertex for vertex, deps in depsDict.items() if len(deps) == 0 and vertex not in visited]
            
        return sortedList if len(sortedList) == numVertices else []
		