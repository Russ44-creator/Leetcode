class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                curIdx = stack.pop()
                while stack and height[stack[-1]] == height[curIdx]:
                    stack.pop()
                if stack:
                    stackTop = stack[-1]
                    ans += (min(height[stackTop], height[i]) - height[curIdx]) * (i - stackTop - 1)
            stack.append(i)
        return ans