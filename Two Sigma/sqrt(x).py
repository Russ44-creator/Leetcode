class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last

        # res = 1
        # for i in range(20):
        #     temp = res
        #     res = temp - (temp ** 2 - x) / (2 *temp)
        # return math.floor(res)
        # x^2 - a = 0.