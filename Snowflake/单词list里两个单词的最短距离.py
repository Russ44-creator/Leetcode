X = ["are", "they", "where", "are"]
a = "are"
b = "where"
# Follow up:  A不一定要出现在B之前, 就是也可以是B先出现, 然后再出现A.
hashMap = {}
ans = float('inf')
for i, word in enumerate(X):
    if word == a:
        if b in hashMap:
            ans = min(ans, abs(i - hashMap[b]) + 1)
        hashMap[a] = i
    if word == b:
        if a in hashMap:
            ans = min(ans, abs(i - hashMap[a]) + 1)
        hashMap[b] = i

print(ans)