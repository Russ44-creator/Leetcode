class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove_from_list(node)
            self.insert_to_list(node)
            return self.dic[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.remove_from_list(node)
            new_node = ListNode(key, value)
            self.insert_to_list(new_node)
            self.dic[key] = new_node
        else:
            if len(self.dic) >= self.capacity:
                self.remove_from_tail()
            new_node = ListNode(key, value)
            self.insert_to_list(new_node)
            self.dic[key] = new_node
    
    def remove_from_tail(self):
        last_node = self.tail.prev
        self.remove_from_list(last_node)
        key = last_node.key
        del self.dic[key]
    
    def insert_to_list(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node
    
    def remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)