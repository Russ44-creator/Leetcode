from collections import Counter
from typing import List

class Solution:
  def twoSum(self, n: int, task: List[int]) -> int:
    ts = sorted(list(Counter(task).values()), reverse=True)

    def check(v):
      remain = 0
      for t in ts:
        remain = remain + (t-v) if t >= v else remain - (v-t)//2
      return remain <= (n-len(ts))*(v//2)
    
    l, r = 0, max(ts)
    while l <= r:
      mid = (l+r) >> 1
      if check(mid):
        r = mid-1
      else:
        l = mid+1
    return r+1
  

if __name__ == "__main__":
  print(Solution().twoSum(2, [1,1,2,1]))
  print(Solution().twoSum(3, [1, 2, 3, 1, 2, 3]))