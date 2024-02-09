'''
自我介绍3分钟之后开始做题。题目是unsorted array找median。开始比较了quick sort的时间复杂度，
问怎么算出来o(n)的复杂度的，写的时候在quick sort 的exchange pivot那里卡了很长时间，最后好歹
是debug出来了。
'''

def find_median(nums):
    k = (len(nums) - 1) // 2
    return quicksort(nums, k, 0, len(nums) - 1)

def quicksort(nums, k, lo, hi):
    i = lo
    j = hi
    pivot = nums[lo]
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]
    nums[i] = pivot
    print(i)
    if i > k:
        return quicksort(nums, k, lo, i - 1)
    if i < k:
        return quicksort(nums, k, i + 1, hi)
    return nums[i]

nums = [5, 1, 6, 7, 4, 3, 8, 9]
print(find_median(nums))

