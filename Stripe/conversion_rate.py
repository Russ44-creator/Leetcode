'''
String: "AUD:USD:0.7,AUD:JPY:100,USD:CAD:1.2"
Part 1
给定conversion rates input, 写一个可以通过fromCurrency和toCurrency调出'直接'汇率的函数，
暂时不需要考虑多次转换，不过为了提高印象分可以跟面试官确认
需要先parse给定的input之后存储数据。我用的是一个简单的hashmap, key是“fromCurrency/toCurrency”,
Part 2
允许通过一次转换获得想要的货币, 例子(AUD->USD->CAD)
这个可以不用写那么麻烦, 我是直接hard code了一个intermediate step, 
好处是写起来很快并且不容易出问题. 你也可以直接按照bfs的思路来做, 但是如果失误的话会影响part 3, 
所以我建议到part 4再考虑bfs, 反正bfs写起来也挺快的
Part 3
当计算汇率是计算最佳汇率, 就比如你可以通过AUD->GBP->CAD 和 AUD->USD->CAD两种方法获得CAD, 那你就要找最好的汇率
因为挺简单的不知道该跟面试官说啥, 然后又想提升一下印象分, 我就算变讨论了下什么是最好汇率, min还是max, 
然后瞎bb了一点
Part 4
允许不止一次转换, 就是bfs直到找到target currency或者发现没有path, 用dfs应该也可以
总的来说挺简单的, 写快一点不用在performance上过多纠结, 能做出来更多的part比较重要, 然后我的面试官比较passive, 
每次问问题都会问我怎么想然后按我想的来, 建议就是多想想能怎么bb提升印象分
'''
from collections import defaultdict

string = "AUD:USD:0.7,AUD:JPY:100,USD:CAD:1.2"

def simple_convert(string, from_country, to_country):
    rate_map = defaultdict(dict)
    rate_list = string.split(",")
    for rate in rate_list:
        fromCurrency, toCurrency, r = rate.split(":")
        rate_map[fromCurrency][toCurrency] = float(r)
        rate_map[toCurrency][fromCurrency] = 1 / float(r)
    return rate_map[from_country][to_country]

print(simple_convert(string, "AUD", "USD"))

def one_middle_convert(string, from_country, to_country):
    rate_map = defaultdict(dict)
    rate_list = string.split(",")
    for rate in rate_list:
        fromCurrency, toCurrency, r = rate.split(":")
        rate_map[fromCurrency][toCurrency] = float(r)
        rate_map[toCurrency][fromCurrency] = 1 / float(r)
    res = 0
    if to_country in rate_map[from_country]:
        res = rate_map[from_country][to_country]
    for middle in rate_map[from_country]:
        if to_country in rate_map[middle]:
            res = max(res, rate_map[from_country][middle] * rate_map[middle][to_country])
    return res

print(one_middle_convert(string, "AUD", "CAD"))

import heapq, math
def best_conversion(string, from_country, to_country):
    graph = {}
    rate_list = string.split(",")
    for rate in rate_list:
        fromCurrency, toCurrency, r = rate.split(":")
        if fromCurrency not in graph:
            graph[fromCurrency] = []
        graph[fromCurrency].append((toCurrency, -math.log(rate)))

    heap = [(0, from_country)]
    visited = {}
    while heap:
        accumulated_weight, currency = heapq.heappop(heap)
        if currency == to_country:
            return accumulated_weight
        if currency in visited:
            continue
        visited[currency] = accumulated_weight
        for neighbor, weight in graph.get(currency, []):
            if neighbor not in visited:
                heapq.heappush(heap, (accumulated_weight + weight, neighbor))
    return -1

