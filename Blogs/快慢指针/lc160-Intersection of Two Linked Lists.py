# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        one = headA
        two = headB
        while one != two:
            one = headA if one is None else one.next
            two = headB if two is None else two.next
        return one