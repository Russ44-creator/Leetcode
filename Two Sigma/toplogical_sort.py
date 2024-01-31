from collections import defaultdict
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        def getTime(x):
            return time[x-1]
        
        # build adjaceny list representation
        graph = defaultdict(list)
        for (prereq, course) in relations:
            graph[course].append(prereq)
        
        visited = dict()
        def rec(course):
            if course in visited:
                return visited[course]

            visited[course] = float('inf')
            maxTime = 0
            for preReq in graph[course]:
                maxTime = max(maxTime, rec(preReq))

            visited[course] = maxTime + getTime(course)
            return visited[course]

        maxVal = 0
        for i in range(n+1):
            maxVal = max(maxVal, rec(i))
        
        if maxVal == float('inf'):
            return 0
        
        return maxVal