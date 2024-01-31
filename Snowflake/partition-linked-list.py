# https://www.1point3acres.com/bbs/thread-981138-1-1.html
# https://www.1point3acres.com/bbs/thread-932877-1-1.html
'''
第三题： Given a link‍‌‍‍‍‌‌‍‌‌‍‌‍‍‌‍‌ed list and a value x, partition it such that all nodes 
less than or equal to x come first, followed by all nodes with a value greater than x
E.g 1 -> 3 -> 6 -> 4, x = 5
Output: 1 -> 3 -> 4 -> 6
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head, x: int):
        little, large = ListNode(), ListNode()
        little_dummy, large_dummy = little, large
        while head:
            if head.val >= x:
                large.next = ListNode(head.val)
                large = large.next
            else:
                little.next = ListNode(head.val)
                little = little.next
            head = head.next
        little.next = large_dummy.next
        return little_dummy.next
            