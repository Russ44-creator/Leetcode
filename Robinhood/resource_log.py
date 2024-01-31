# Suppose we have an unsorted log file of accesses to web resources. 
# Each log entry consists of an access time, 
# the ID of the user making the access, and the resource ID.
# The access time is represented as seconds since 00:00:00, 
# and all times are assumed to be in the same day.
# For example:
import collections
from collections import defaultdict

logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]

length = len(logs1)
dic = defaultdict(list)
for log in logs1:
    dic[log[2]].append(int(log[0]))
ans = ""
max_f = 0
for key, value in dic.items():
    value.sort()
    maxFreq = 0
    l = 0
    for r in range(len(value)):
        while l < r and value[l] + 300 < value[r]:
            l += 1
        maxFreq = max(maxFreq, r - l + 1)
    if maxFreq > max_f:
        max_f = maxFreq
        ans = key
        
print(ans, max_f)
    
