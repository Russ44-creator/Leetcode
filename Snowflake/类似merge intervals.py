# https://www.1point3acres.com/bbs/thread-1029886-1-1.html

'''
path permutations, 给个字符串，让你切割成指定大小的多种路径:
(abcd, 2) = {a.b.cd, a.bc.d, ab.c.d}
类似于Merge Intervals, 带score的
'''

string = "abcd"
path = 2
res = []
def dfs(word, remain, temp):
    if word == "":
        return
    if remain == 0:
        temp.append(word)
        res.append(".".join(temp))
        temp.pop()
        return
    for i in range(1, len(word) + 1):
        temp.append(word[:i])
        # print(word[:i])
        dfs(word[i:], remain - 1, temp)
        temp.pop()

dfs(string, 2, [])
print(res)