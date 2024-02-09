class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        cnts = [0] * 26
        for c in tasks:
            cnts[ord(c) - ord('A')] += 1
        maxv, tot = 0, 0
        for i in range(26):
            maxv = max(maxv, cnts[i])
        for i in range(26):
            tot += 1 if maxv == cnts[i] else 0
        return max(len(tasks), (n + 1) * (maxv - 1) + tot)