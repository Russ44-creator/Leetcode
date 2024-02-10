"""
Dropbox

Id Allocator / Number / Phone Number

Write a class for an id allocator that can allocate and release ids
"""
import collections

class Allocator:
    def __init__(self, max_val) -> None:
        self.queue = collections.deque()
        self.first_pass_idx = 0
        self.allocated = set()
        self.max_val = max_val
    
    def allocate(self):
        result = None
        if self.first_pass_idx <= self.max_val:
            self.first_pass_idx += 1
            result = self.first_pass_idx - 1
        elif len(self.queue) > 0:
            result = self.queue.pop()
        if result is not None:
            self.allocated.add(result)
            return result
        else:
            return False
    
    def release(self, id):
        if (not 0 <= id < self.max_val) or (id not in self.allocated):
            return False
        self.allocated.remove(id)
        self.queue.appendleft(id)