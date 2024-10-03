import random

class Solution:
    def findKthLargest(self, nums, k):
        return self.quick_select(nums, len(nums) - k)

    def quick_select(self, nums, k_smallest): # k_smallest (zero-based index)
        pivot = random.choice(nums)
        left, mid, right = [], [], []

        for num in nums:
            if num == pivot:
                mid.append(num)
            elif num < pivot:
                left.append(num)
            else:
                right.append(num)
        
        if k_smallest < len(left):  # k_smallest is on the left side
            return self.quick_select(left, k_smallest)

        if k_smallest < len(left) + len(mid):  # k_smallest is on the middle
            return pivot

        return self.quick_select(right, k_smallest - len(left) - len(mid))