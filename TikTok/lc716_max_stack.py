class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        currMax = x
        if len(self.stack) > 0: currMax = max(x, self.peekMax())
        self.stack.append([x, currMax])

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        stack = self.stack
        buffer, currMax = [], stack[-1][1]
        for i in reversed(range(len(stack))):
            if stack[i][0] == currMax: break
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return currMax