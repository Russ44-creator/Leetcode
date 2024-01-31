import random
import bisect

class Solution:

    def __init__(self, w):
        self.prefix_sum = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        random_num = random.randint(1, self.total_sum)
        index = bisect.bisect_left(self.prefix_sum, random_num)
        return index