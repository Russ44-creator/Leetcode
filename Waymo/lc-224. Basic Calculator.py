class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        num = 0
        pre_op = '+'
        s += '+'
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == ' ':
                pass
            elif c == '(':
                start = i + 1
                num_brackets = 1
                i += 1
                while i < len(s):
                    if s[i] == '(':
                        num_brackets += 1
                    elif s[i] == ')':
                        num_brackets -= 1
                    if num_brackets == 0:
                        break
                    i += 1
                
                num = self.calculate(s[start: i])
                print(i, num)
            else:
                if pre_op == '+':
                    stack.append(num)
                else:
                    stack.append(-num)
                num = 0
                pre_op = c
            i += 1
        return sum(stack)