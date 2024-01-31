class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        pre_op = "+"
        s += "+"
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            elif s[i] == " ":
                i += 1
            elif s[i] == "(":
                i_start = i+1
                # 用于记录左括号-右括号数目 当num_brackts=0时进行递归 而不是第一次见到右括号！
                num_brackets=1
                for i in range(i_start,len(s)):
                    if s[i]=='(':
                        num_brackets+=1
                    elif s[i]==')':
                        num_brackets-=1
                    if num_brackets==0: break
                num = self.calculate(s[i_start:i])
               
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
                pre_op = s[i]
                i += 1
        return sum(stack)