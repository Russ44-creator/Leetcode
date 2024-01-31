from collections import defaultdict

class Solution:
    def loadFactorsTopologicalSorting(self, service_list, entrypoint):
        # adjacency list
        adj = {}
        for sl in service_list:
            service, dependencies_str = sl.split("=")
            dependencies = dependencies_str.split(",")
            # non-existent dependency references should be ignored
            if dependencies[0] == "":
                adj[service] = []
            else:
                for dependency in dependencies:
                    if service in adj:
                        adj[service].append(dependency)
                    else:
                        adj[service] = [dependency]

        counter = defaultdict(int)
        visit = defaultdict(bool)  # False=visited, True=current path

        def dfs(service):
            if visit[service]:  # if it returns True it's a cycle
                return

            if visit[service] == False:
                counter[service] += 1

            visit[service] = True
            for nn in adj[service]:
                if nn in adj:
                    dfs(nn)
            visit[service] = False

        dfs(entrypoint)

        res = []
        for service, load_factor in counter.items():
            res.append(f"{service}*{str(load_factor)}")

        return sorted(res)

service_list = ["logging=",
"user=logging",
"orders=user,foobar",
"recommendations=user,orders",
"dashboard=user,orders,recommendations"]
entrypoint = "dashboard"

sol = Solution()
print(sol.loadFactorsTopologicalSorting(service_list, entrypoint))