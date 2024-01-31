intervals = [[0,30],[5,10],[15,20]]
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of conference rooms required.
import heapq

def minMeetingRooms(intervals):
    intervals.sort()
    heap = []  # stores the end time of intervals
    for i in intervals:
        if heap and i[0] >= heap[0]: 
            # means two intervals can use the same room
            heapq.heapreplace(heap, i[1])
        else:
            # a new room is allocated
            heapq.heappush(heap, i[1])
    return len(heap)

print(minMeetingRooms(intervals))