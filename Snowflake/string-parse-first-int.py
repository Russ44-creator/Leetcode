'''
第二题就是 从string里parsetInt，给一个由digit和english letter组成的string，
从找到一个interger后，返回这个int，后面的substring就可以不看了。
e.g. input (string) “AUUadd-42dartg78”, output(int): -42，
'''

string = "AUUadd-42dartg78"
ans = ""
start = 0
i = 0
while i < len(string):
    if "0" <= string[i] <= "9":
        start = i
        while i < len(string) and "0" <= string[i] <= "9":
            ans += string[i]
            i += 1
        break
    i += 1
res = int(ans)
if start - 1 >= 0 and string[start - 1] == "-":
    print(-res)
else:
    print(res)
        
