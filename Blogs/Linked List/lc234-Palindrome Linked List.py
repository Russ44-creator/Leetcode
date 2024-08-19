from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list=[]
        while head: 
            list.append(head.val)
            head=head.next
        l,r=0, len(list)-1
        while l<=r: 
            if list[l]!=list[r]:
                return False
            l+=1
            r-=1
        return True   