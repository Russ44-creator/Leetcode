high = [(1, 3), (5, 7), (11, 16)]
low = [(0, 1), (2, 3), (3, 4), (3, 5), (3, 6), (4, 5), (5, 8), (6, 9), (7, 10), (7, 11), 
       (8, 15), (13, 18), (17, 20)]

high.sort()
low.sort()

ans = high.copy()
i, j = 0, 0
while j < len(low):
    if i == len(high):
        ans.append(low[j])
        j += 1
        continue
    if low[j][1] <= high[i][0]:
        ans.append(low[j])
        j += 1
    else:
        while i < len(high) and low[j][1] > high[i][0]:
            if low[j][0] >= high[i][1]:
                i += 1
            else:
                j += 1
                break
        if i < len(high) and low[j][1] <= high[i][0]:
            ans.append(low[j])
            j += 1
ans.sort()
print(ans)