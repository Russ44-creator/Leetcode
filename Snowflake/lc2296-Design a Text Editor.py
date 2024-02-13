class TextEditor:

    def __init__(self):
        self.left, self.right = [], []

    def addText(self, text: str) -> None:
        self.left += list(text)

    def deleteText(self, k: int) -> int:
        k0 = k
        while k and self.left:
            self.left.pop()
            k -= 1
        return k0 - k

    def text(self):
        return ''.join(self.left[-10:])

    def cursorLeft(self, k: int) -> str:
        while k and self.left:
            self.right.append(self.left.pop())
            k -= 1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.right:
            self.left.append(self.right.pop())
            k -= 1
        return self.text()
        

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)