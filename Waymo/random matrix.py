import random
class Solution:
    def randomArray(self, l, M, N):
        res = [[0 for i in range(N)] for j in range(M)]
        idxs = list(range(M * N))
        random.shuffle(idxs)
        if M * N % len(l) != 0:
            return []
        n = M * N / len(l)
        for i in range(M * N):
            idxL = int(idxs[i] // n)
            r = i // M
            c = i % M
            res[r][c] = l[idxL]
        return res
l = [1, 2, 3, 4]
M = 4
N = 4
s = Solution()
for i in range(3):
    print(s.randomArray(l, M, N))
