# https://www.1point3acres.com/bbs/thread-951795-1-1.html

import collections

input = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 9, 12, 12, 12, 12,
        13, 14, 15, 16]
curTime = -1
reqCount = 0
dropped = []
queueRequests10s = collections.deque()
for i in range(len(input)):
    reqTime = input[i]
    if reqTime != curTime:
        curTime = reqTime
        reqCount = 0
    if reqCount >= 3:
        dropped.append(reqTime)
    else:
        while queueRequests10s and queueRequests10s[0] <= curTime - 10:
            queueRequests10s.popleft()
        if len(queueRequests10s) >= 20:
            dropped.append(reqTime)
        else:
            queueRequests10s.append(reqTime)
            reqCount += 1
print(dropped)