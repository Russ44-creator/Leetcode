'''
实现一个Queue, 操作有:
1. add: insert an element, Integer, to the end of Queue
2. poll: retrieve and remove the first element from the Queue
两个操作的时间都是O(1).
用list, 保存head和tail.
follow up 1: 给每个element加个weight的attribute, 每次poll的时候先输出权重比较大的, 
weights只有5个: 1,2,3,4,5. (用5个list保存)
follow up 2: weights的数字可以很大, 但是总的权重数量是少数的. (用map)
'''

class ListNode:
    def __init__(self) -> None:
        pass
# 可以用map来存listnode，也可以用5个list
# map来存listnode，所以得用heap来排序
        
