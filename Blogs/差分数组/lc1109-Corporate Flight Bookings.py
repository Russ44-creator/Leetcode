from collections import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        c = [0] * (n + 1)
        for bo in bookings:
            l = bo[0] - 1
            r = bo[1] - 1
            v = bo[2]
            c[l] += v
            c[r + 1] -= v
        ans = [0] * n
        ans[0] = c[0]
        for i in range(1, n):
            ans[i] = ans[i - 1] + c[i]
        return ans