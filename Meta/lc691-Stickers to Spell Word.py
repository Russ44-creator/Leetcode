from collections import defaultdict
from typing import List
from collections import Counter, deque

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        availables = []
        for sticker in stickers:
            cnts = defaultdict(int)
            for s in sticker:
                cnts[s] += 1
            availables.append(cnts)
        queue = deque([(target, 0)])
        visited = {target}
        while queue:
            cur, step = queue.popleft()
            if not cur:
                return step
            for avl in availables:
                if cur[0] in avl:
                    nxt = cur
                    current_count = Counter(cur)
                    for char, num in avl.items():
                        if char in current_count:
                            current_count[char] -= num
                            if current_count[char] <= 0:
                                del current_count[char]
                    nxt = ''.join(char * current_count[char] for char in current_count)
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, step + 1))
        return -1