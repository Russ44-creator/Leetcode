from collections import defaultdict

box = [["cm", "mc"],
       ["ccm", "mc"],
       ["pm", "mc"],
       ["c", "mc"],
        ["mc", "mc"]]


def check_quality(box):
    ans = 0
    for b in box:
        dic = defaultdict(lambda: 0)
        first = b[0]
        temp = 0
        if len(b[0]) != len(b[1]):
            ans += 1
            continue
        for i in first:
            dic[i] += 1
        second = b[1]
        for i in second:
            if i not in dic:
                ans += 1
                temp = 1
                break
            if i in dic:
                dic[i] -= 1
                if dic[i] == 0:
                    del dic[i]
        if temp == 0 and bool(dic):
            ans += 1
    return ans

print(check_quality(box))