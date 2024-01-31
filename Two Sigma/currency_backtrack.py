def get_currency_exchange_rate(source, target, graph):

    def backtrack(current, seen, k):
        if current == target:
            return 1
    
        product = 0
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    product = max(product, graph[current][neighbor] * backtrack(neighbor, seen))
                    seen.remove(neighbor)

        return product

    return backtrack(source, {source})


g = {
    "A": {"B": 6, "D": 1},
    "B": {"A": 6, "D": 2, "E": 2, "C": 5},
    "D": {"A": 1, "B": 2, "E": 1},
    "E": {"B": 2, "D": 1, "C": 5},
    "C": {"B": 5, "E": 5}
}
curr1 = "A"
curr2 = "C"
print(get_currency_exchange_rate(curr1, curr2, g))