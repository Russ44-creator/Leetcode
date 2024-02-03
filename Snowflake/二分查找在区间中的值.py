list_ = [1, 2, 2, 4, 5, 6, 7, 7, 8, 8]
a = 2
b = 7
left, right = 0, len(list_)
left_index, right_index = 0, 0
while left < right:
    mid = (left + right) // 2
    if list_[mid] == a:
        right = mid
    elif list_[mid] < a:
        left = mid + 1
    else:
        right = mid 
left_index = right

left, right = 0, len(list_)
while left < right:
    mid = (left + right) // 2
    if list_[mid] == b:
        left = mid + 1
    elif list_[mid] < b:
        left = mid + 1
    else:
        right = mid
right_index = left
print(right_index)
print(list_[left_index:right_index])