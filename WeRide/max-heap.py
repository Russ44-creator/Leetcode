class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        # Add the new value to the end of the list
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("pop from empty heap")
        # Swap the root with the last item and remove the last item
        self._swap(0, len(self.heap) - 1)
        value = self.heap.pop()
        # Restore the heap property by sifting down the new root element
        self._sift_down(0)
        return value

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        # Keep going up until we reach the root or the max heap property is satisfied
        while index > 0 and self.heap[parent_index] < self.heap[index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self, index):
        child_index = 2 * index + 1  # Left child index
        while child_index < len(self.heap):
            # Find the largest child
            right_child_index = child_index + 1
            if right_child_index < len(self.heap) and self.heap[child_index] < self.heap[right_child_index]:
                child_index = right_child_index
            
            # If the parent is larger than both children, the heap property is satisfied
            if self.heap[index] >= self.heap[child_index]:
                break

            # Otherwise, swap the parent with the larger child
            self._swap(index, child_index)
            index = child_index
            child_index = 2 * index + 1

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Example usage:
max_heap = MaxHeap()
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

for num in data:
    max_heap.push(num)

# Pop elements from the max heap
while len(max_heap.heap) > 0:
    print(max_heap.pop(), end=' ')
