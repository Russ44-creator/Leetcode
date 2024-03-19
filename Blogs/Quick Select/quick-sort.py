def quicksort(alist, start, end):
    if start >= end:
        return
    mid = alist[start]
    low, high = start, end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid
    quicksort(alist, start, low - 1)
    quicksort(alist, low + 1, end)

alist = [54,26,93,17,77,31,44,55,20]
quicksort(alist,0,len(alist)-1)
print(alist)
