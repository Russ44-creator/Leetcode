class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        sign = 1
        num = 0
        pre_op = '+'
        s += '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == " ":
                pass
            else:
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    operant = stack.pop()
                    stack.append(operant * num)
                elif pre_op == "/":
                    operant = stack.pop()
                    stack.append(int(operant / num))
                num = 0
                pre_op = c

        return sum(stack)
    