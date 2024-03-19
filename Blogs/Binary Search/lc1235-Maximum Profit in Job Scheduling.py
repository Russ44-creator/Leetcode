from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        f = [0] * (len(jobs) + 1)
        for i, (_, st, p) in enumerate(jobs):
            j = bisect_right(jobs, (st, inf), hi = i)
            f[i + 1] = max(f[i], f[j] + p)
        return f[-1]