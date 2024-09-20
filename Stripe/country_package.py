# https://www.1point3acres.com/bbs/thread-1072844-1-1.html
input = "US:UK:UPS:4,US:UK:DHL:5,UK:CA:FedEx:10,AU:JP:DHL:20"
'''
第一问，和汇率题一样
写一个方法, 输入是 (成本定义字符串, sourceCountry, targetCountry, method), 输出cost
不难, 犹豫了一下是马上就用nested map还是用string拼接, 最后用了拼接+单层map秒了, 但是感觉选错了。。
考官还问了一些edge case的处理, 比如如果国家没找到返回什么,定义是空字符串你的代码可以处理么之类的
'''

'''
第二问，也和汇率题一样
如果最多允许有一个中间的 country,输出一个结构。比如输入的US, CA, 你需要输出这么个玩意
{
    route: "US -> UK -> CA",
    method: "UPS -> FedEx",
    cost: 14
}
题里没用明确说到底是个string还是json obj还是个什么, 我没有和考官确认, 疏忽了, 按照obj写的。
这点还是要和考官确认下为好。
不需要计算最低‍‌‍‍‍‌‌‍‌‌‍‌‍‍‌‍‌‍‍‍成本, 任何中间country和method都行, cost是两个method的cost之和。
看到这个有点懵了, 我用了三层map做的, 多层嵌套给自己整成SB了。写了一段巨丑无比的n层的if/for。不过最后竟然一次跑通, 感觉出现了奇迹。。
做完第二问就没时间了, 没说有没有第三问。我觉得如果有也是和汇率题一样, 要么求最低成本的路径, 要么允许多个中间country写DFS解。
'''

def backtrack(currentNode, endNode, graph, temp, visited, results):
    if currentNode == endNode:
        results.add(temp)
        return
    neighbors = graph.get(currentNode)
    if neighbors:
        for neighNode, conversionRate in neighbors.items():
            if neighNode not in visited:
                visited.add(neighNode)
                backtrack(neighNode, endNode, graph, temp * conversionRate, visited, results)
                visited.remove(neighNode)

def build_graph(currencies_list):
    graph = {}
    for currency in currencies_list:
        splitCurr = currency.split(',')
        from_currency = splitCurr[0]
        to_currency = splitCurr[1]
        value = float(splitCurr[2])
        
        if from_currency not in graph:
            graph[from_currency] = {}
        graph[from_currency][to_currency] = value
    return graph

def find_max_conversion_rate(currencies_input, currencyFrom, currencyTo):
    currencies = currencies_input.split(';')
    graph = build_graph(currencies)
    visited = set()
    results = set()
    backtrack(currencyFrom, currencyTo, graph, 1.0, visited, results)
    if results:
        return max(results)
    else:
        return -1.0

currencies_input = 'USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155'
currencyFrom = 'USD'
currencyTo = 'JPY'
maxRate = find_max_conversion_rate(currencies_input, currencyFrom, currencyTo)
print(maxRate)  # 输出: 110.05


import heapq, math
def max_conversion_rate(rates, query):
    # Build the graph with negative log weights
    graph = {}
    for from_currency, to_currency, rate in rates:
        if from_currency not in graph:
            graph[from_currency] = []
        graph[from_currency].append((to_currency, -math.log(rate)))
    
    source, target = query
    if source not in graph:
        return -1.0  # Source currency not in graph

    # Dijkstra's algorithm initialization
    heap = [(0, source)]  # (accumulated_weight, currency)
    visited = {}
    
    while heap:
        accumulated_weight, currency = heapq.heappop(heap)
        if currency == target:
            # Exponentiate the negative accumulated weight to get the rate
            return math.exp(-accumulated_weight)
        if currency in visited:
            continue
        visited[currency] = accumulated_weight
        for neighbor, weight in graph.get(currency, []):
            if neighbor not in visited:
                heapq.heappush(heap, (accumulated_weight + weight, neighbor))
    
    return -1.0  # Target currency not reachable