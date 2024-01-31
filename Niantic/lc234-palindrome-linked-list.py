# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        prev = None
        while mid:
            next_node = mid.next
            mid.next = prev
            prev = mid
            mid = next_node
        tail = prev
        
        while head and tail and tail != head:
            if tail.val != head.val:
                return False
            head = head.next
            tail = tail.next
        return True