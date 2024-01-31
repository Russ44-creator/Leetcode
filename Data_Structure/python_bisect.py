from bisect import bisect_left 
import bisect

arr = [1, 2, 3, 5]
arr_1 = [1, 2, 3, 4, 4, 4, 5]
print(bisect.bisect(arr, 4))            # 无重复值列表数组 #3
print(bisect.bisect(arr_1, 4))          # 插入点索引 在所有已存在值的 右侧 #6
print(bisect.bisect_right(arr, 4))    # 插入点索引 在所有已存在值的 右侧 #3

arr = [1, 2, 3, 5]
arr_1 = [1, 2, 3, 4, 4, 4, 5]
print(bisect.bisect(arr, 4))            # 无重复值列表数组
print(bisect.bisect(arr_1, 4))          # 插入点索引 在所有已存在值的 右侧
print(bisect.bisect_right(arr_1, 4))    # 插入点索引 在所有已存在值的 右侧 # 6
print(bisect.bisect_left(arr_1, 4))     # 插入点索引 在所有已存在值的 左侧 # 3
