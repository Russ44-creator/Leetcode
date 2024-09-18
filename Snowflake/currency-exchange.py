# https://www.1point3acres.com/bbs/thread-947030-1-1.html
'''
第二题汇率转换，给一个list of triplets (currency_1, currency_2, 
exchange_rate), 一个currency_a，一个currency_b，一个amount，求换算出来的cure‍‌‍‍‍‌‌‍‌‌‍‌‍‍‌‍‌‍‍‍ncy_b的数量
问了不少followup，比如第二题有没有O(1)解（建个dict），这个dict怎么存，怎么improve之类的

'''
'''
Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
To/From currency ['GBP', 'AUD']
'''

from collections import defaultdict
from typing import List

def create_graph(currencies):
    graph = defaultdict(list)
    for source, target, rate in currencies:
        graph[source].append((target, rate ))
        # reverse edge
        graph[target].append((source, 1/rate))

    return graph

def find_rate_converion(source: str, target: str) -> int:        
    def dfs(source:str, target:str, visited : set) -> int:
        if source == target:
            return 1

        visited.add(source)
        edges = graph.get(source, None)
        final_rate = -1
        for edge in edges:
            nbr, rate = edge
            if nbr not in visited:
                # visited.add(nbr)
                rate_to_nbr = rate * dfs(nbr, target, visited)
                if rate_to_nbr > 0: # valid path
                    final_rate = rate_to_nbr
                    break

        return final_rate

    graph = create_graph(curr)
    return dfs(source, target, set())        

curr = [ ("GBP", "JPY", 1.5),  ("USD", "CNY", 0.5), ("USD", "AUD", 0.5), ("JPY", "AUD", 0.1), ("JPY", "RPY", 20), ("RPY", "RUS", 11),  ("RPY", "NER", 11), ("RUS", "TED", 1),  ("RUS", "ROM", 2), ("RUS", "PINK", 2), ("RUS", "YELLOW", 2),("RPY", "ABC", 3000), ("ABC", "BCD", 3000), ("BCD", "ROM", 3000)]
# USD -> AUD -> JPY -> RPY -> RUS ->  ROM
# USD -> AUD -> JPY -> RPY -> ABC -> BCD ->  ROM
print("rate",find_rate_converion("USD", "ROM"))   