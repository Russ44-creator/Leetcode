from collections import defaultdict
from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        ans = inf
        hashMap = defaultdict(lambda: 0)
        for i in range(n):
            hashMap[t[i]] += 1
        i, j = 0, 0
        start, end = 0, 0
        count = len(hashMap)
        while j < len(s):
            hashMap[s[j]] = hashMap.get(s[j], 0) - 1
            if hashMap[s[j]] == 0:
                count -= 1
            if count == 0:
                while count == 0:
                    if ans > j - i + 1:
                        start, end = i, j
                        ans = j - i + 1
                    hashMap[s[i]] += 1
                    if hashMap[s[i]] > 0:
                        count += 1
                    i += 1
            j += 1
        if ans == inf:
            return ""
        return s[start: end + 1]