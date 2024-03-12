import collections

class Solution:
    def topKFrequent(self, nums, k: int):
        # 使用快排
        count = collections.Counter(nums)
        reverse_k = len(count) - k
        num_cnt = list(count.items())
        topKs = self.findTopK(num_cnt, k, 0, len(num_cnt) - 1)
        return [item[0] for item in topKs]
    
    def findTopK(self, num_cnt, k, low, high):
        print(low)
        pivot = num_cnt[low]
        i = low
        j = high
        while i < j:
            while i < j and num_cnt[j][1] <= pivot[1]:
                j -= 1
            num_cnt[i] = num_cnt[j]
            while i < j and num_cnt[i][1] >= pivot[1]:
                i += 1
            num_cnt[j] = num_cnt[i]
        num_cnt[i] = pivot
        if i == k - 1:
            return num_cnt[:k]
        elif i > k-1:
            return self.findTopK(num_cnt, k, low, i - 1)
        else:
            return self.findTopK(num_cnt, k, i + 1, high)
        
