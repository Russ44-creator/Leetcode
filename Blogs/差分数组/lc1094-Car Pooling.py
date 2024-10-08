from collections import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort the trips
        # compare the cap with the number of passengers
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True