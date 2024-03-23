import heapq

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort()
        heap = []
        for interval in intervals:
            
            if not heap or heap[0] > interval[0]:
                # print(interval[0])
                heapq.heappush(heap, interval[1])
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, interval[1])
        return len(heap)