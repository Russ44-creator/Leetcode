from collections import defaultdict

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 8]

def find_doubles(l):
    l.sort()
    ans = defaultdict(lambda: 0)
    ele = set()
    for i in l:
        if i % 2 == 0 and i / 2 in ele:
            ans[int(i / 2)] += 1
        if i == 0:
            ans[int(i / 2)] += 1
        ele.add(i)
    l1 = []
    for key, value in ans.items():
        if value == 1:
            l1.append(key)
    return sorted(l1)

print(find_doubles(l))