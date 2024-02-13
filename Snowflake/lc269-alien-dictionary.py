from collections import defaultdict
import collections

class Solution:
    def alienOrder(self, words) -> str:
        if len(words) == 1:
            all_chars = set()
            ans = ""
            for w in words[0]:
                if w in all_chars:
                    continue
                ans += w
                all_chars.add(w)
            return ans
        graph = defaultdict(set)
        all_chars = set()
        for word in words:
            for w in word:
                all_chars.add(w)
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            ptr1, ptr2 = 0, 0
            while ptr1 < len(word1) and ptr2 < len(word2) and word1[ptr1] == word2[ptr2]:
                ptr1 += 1
                ptr2 += 1
            if ptr1 < len(word1) and ptr2 < len(word2):
                graph[word1[ptr1]].add(word2[ptr2])
            if ptr1 < len(word1) and not ptr2 < len(word2):
                return ""
        
        in_degree = defaultdict(lambda: 0)
        for key, value in graph.items():
            for v in value:
                in_degree[v] += 1
            in_degree[key] += 0

        dq = collections.deque()

        for key, value in in_degree.items():
            if value == 0: 
                dq.append(key)
        ans = ""
        visited = set()
        while dq:
            node = dq.popleft()
            all_chars.remove(node)
            ans += node
            
            for nxt in graph[node]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    dq.append(nxt)
            del graph[node]
        if len(graph) != 0:
            return ""
        for char in all_chars:
            ans += char
        return ans
