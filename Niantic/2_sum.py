from collections import defaultdict
nums = [2,7,11,15, 7, 2]
target = 9

hset = defaultdict(lambda: 0)
for i, num in enumerate(nums):
    hset[num] += 1

ans = 0
for key, value in hset.items():
    if target - key in hset:
        ans += hset[target - key] * hset[key]

print(int(ans / 2))