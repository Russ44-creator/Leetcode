import heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        freq_table = {}
        for i in nums:
            freq_table[i] = freq_table.get(i, 0) + 1
        heap = []
        for i in freq_table.keys():
            if len(heap) == k:
                heapq.heappushpop(heap, (freq_table[i], i))
            else:
                heapq.heappush(heap, (freq_table[i], i))
        ans = []
        while k > 0:
            k -= 1
            ans.append(heapq.heappop(heap)[1])
        return ans