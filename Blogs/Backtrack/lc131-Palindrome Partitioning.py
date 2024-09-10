from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        isPalindrome = [[False] * len(s) for _ in range(len(s))]  # 初始化isPalindrome矩阵
        self.computePalindrome(s, isPalindrome)
        self.backtracking(s, 0, [], result, isPalindrome)
        return result

    def backtracking(self, s, startIndex, path, result, isPalindrome):
        if startIndex == len(s):
            result.append(path[:])
            return

        for i in range(startIndex, len(s)):
            if isPalindrome[startIndex][i]:   # 是回文子串
                substring = s[startIndex:i + 1]
                path.append(substring)
                self.backtracking(s, i + 1, path, result, isPalindrome)  # 寻找i+1为起始位置的子串
                path.pop()           # 回溯过程，弹出本次已经添加的子串

    def computePalindrome(self, s, isPalindrome):
        for i in range(len(s) - 1, -1, -1):  # 需要倒序计算，保证在i行时，i+1行已经计算好了
            for j in range(i, len(s)):
                if j == i:
                    isPalindrome[i][j] = True
                elif j - i == 1:
                    isPalindrome[i][j] = (s[i] == s[j])
                else:
                    isPalindrome[i][j] = (s[i] == s[j] and isPalindrome[i+1][j-1])