from collections import defaultdict, List, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        edges = defaultdict(lambda: 0)
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                edges[ingredient] += 0
                edges[recipes[i]] += 1
        dq = deque()
        ans = []
        supplies_set = set(supplies)
        for supply in supplies:
            edges[supply] += 0
            dq.append(supply)
        while dq:
            ingredient = dq.popleft()
            for next_food in graph[ingredient]:
                edges[next_food] -= 1
                if edges[next_food] == 0:
                    dq.append(next_food)
                    ans.append(next_food)
        return ans
