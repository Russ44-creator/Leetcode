import heapq
from typing import List
from heapq import heapify, heappop, heappush, heappushpop

def klargestelements(arr1,k):
    q = heapq.nlargest(k,arr1)
    return q

k = 3
arr1 = [1,2,4,5,6,7]
m = klargestelements(arr1, k)
print(m)

# 使用tuple作为heap的元素
list = [('a', 2), ('b', 1), ('c', 0), ('d', 1)]
heap_elts = [(item[1], item) for item in list]
heapq.heapify(heap_elts)  # you specifically asked about heapify, here it is!
while len(heap_elts) > 0:
    print(heapq.heappop(heap_elts)[1])    # element 1 is the original tuple

# top k frequent
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq_table = {}
    for i in nums:
        freq_table[i] = freq_table.get(i, 0) + 1
    heap = []
    for i in freq_table.keys():
        if len(heap) == k:
            heappushpop(heap, (freq_table[i], i))
        else:
            heappush(heap, (freq_table[i], i))
    ans = []
    while k > 0:
        k -=1
        ans.append(heappop(heap)[1])
    return ans

# heapreplace 先pop后push

from queue import Queue   # 队列，FIFO
from queue import PriorityQueue  #优先级队列，优先级高的先输出

q = PriorityQueue()
q.put((2, "Lisa"))
q.put((3, "dada"))
i = 0
# while i < q.qsize():
#     print(q.get())
while q.empty() == False:
    break

for item in q.queue:
    print(item)
    if item[1] == "Lisa":
        print(2)

while i < q.qsize():
    print(q.get())

def contains_in_pq(pq, node):
    for item in pq.queue:
        if item[1] == node:
            return True
    return False

size1 = q.qsize()

class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return
 
    def __lt__(self, other):
        return self.priority < other.priority
 	  
        # 或者使用__cmp__函数
        # def __cmp__(self, other):
        #     if self.priority < other.priority:
        #         return -1
        #     elif self.priority == other.priority:
        #         return 0
        #     else:
        #         return 1

q2 = PriorityQueue()
 
q2.put(Job(5, 'Mid-level job'))
q2.put(Job(10, 'Low-level job'))
# q2.pop(Job(10, 'Low-level job'))