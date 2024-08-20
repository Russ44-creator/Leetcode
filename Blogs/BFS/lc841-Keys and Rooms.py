from collections import defaultdict, deque, List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for i, room in enumerate(rooms):
            for key in room:
                graph[i].add(key)
        dq = deque([0])
        visited = set()
        while dq:
            room = dq.popleft()
            visited.add(room)
            for key in graph[room]:
                if key in visited:
                    continue
                else:
                    dq.append(key)
        return len(visited) == len(rooms)