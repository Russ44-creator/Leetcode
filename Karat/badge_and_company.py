exit = -1
enter = 1
badge_records = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"]
]

import collections
def find_mismatched_entries(records):
    status = collections.defaultdict(list)
    for r in records:
        if status[r[0]] == [] or r[1] == "enter":
            status[r[0]] += [r[1]]
        elif r[1] == "exit" and status[r[0]][-1] == "enter":
            status[r[0]].pop()
    exitNoBadge, enterNoBadge = [], []
    for e in status:
        if "enter" in status[e]:
            exitNoBadge += [e]
        if "exit" in status[e]:
            enterNoBadge += [e]
    return exitNoBadge, enterNoBadge

print(find_mismatched_entries(badge_records))

 
badge_records = [
  ["Paul", 1315],
  ["Jennifer", 1910],
  ["John", 835],
  ["Paul", 1355],
  ["John", 830],
  ["Paul", 1405],
  ["Paul", 1630],
  ["John", 855],
  ["John", 915],
  ["John", 930],
  ["Jennifer", 1335],
  ["Jennifer", 730],
  ["John", 1630],
]

def find_unusual_entries(records):
    # Build a mapping from each employee to their badge usages.
    entries = collections.defaultdict(list)
    for r in records:
        entries[r[0]] += [r[1]]
    unusual = {}
    for e, t in entries.items():
        if len(t) < 3: continue
        for i in range(len(t)-2):
            j=i+2
# Stop until the period is more than 1 hour. 
            while 0 <= t[j] - t[i] <= 100 and j < len(t):
                j += 1
                unusual[e] = t[i:j]
            # Return the first 1-hour period.
            if e in unusual:
                break
    return unusual

print(find_unusual_entries(badge_records))