class Solution:
    def minAddToMakeValid(self, string: str) -> int:
        stack = []
        for s in string:
            if s == "(":
                stack.append(s)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    stack.append(s)
        return len(stack)