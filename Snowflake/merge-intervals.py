# https://www.1point3acres.com/bbs/thread-981138-1-1.html

'''
第二题: Given an array of time intervals, merge two time slots if they are overlapping.
* [[1, 3], [2, 5], [11, 13]] => [[1, 5], [11, 13]]
具体input output格式可以商量
'''

class Solution:
    def merge(self, intervals):
        # intervals sort
        intervals.sort()
        if not intervals:
            return []
        interval = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > interval[1]:
                ans.append(interval)
                interval = intervals[i]
            else:
                if intervals[i][1] > interval[1]:
                    interval[1] = intervals[i][1]
        ans.append(interval)
        return ans  