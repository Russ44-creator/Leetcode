class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(n, k, combination, start_index):
            if len(combination) == k:
                res.append(combination[:])
            else:
                for i in range(start_index, n + 1):
                    combination.append(i)
                    backtrack(n, k, combination, i + 1)
                    combination.pop()

        backtrack(n, k, [], 1)
        return res