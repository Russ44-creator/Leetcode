class Solution:
    def maximalRectangle(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        pre_sum = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    pre_sum[i][j] = pre_sum[i - 1][j] + 1
        ans = 0
        for i in range(m):
            stack = []
            l = [0] + pre_sum[i] + [0]
            # print(l)
            for j in range(n + 2):
                print(j)
                # print(l)
                # print(stack)
                while stack and l[stack[-1]] > l[j]:
                    height = l[stack[-1]]
                    stack.pop()
                    ans = max(ans, (j - stack[-1] - 1) * height)
                    # print(stack)
                stack.append(j)
        return ans
