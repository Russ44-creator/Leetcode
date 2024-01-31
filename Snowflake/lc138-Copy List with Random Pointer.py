class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        d = {}
        p = head
        while p:
            new_node = Node(p.val, None, None)
            d[p] = new_node
            p = p.next
        p = head
        while p:
            if p.next:
                d[p].next = d[p.next]
            if p.random:
                d[p].random = d[p.random]
            p = p.next
        return d[head]