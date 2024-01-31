class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 防止bug:s的第一个元素即为t的第一个元素的情况
        t = ' ' + t
        # dp = [[0] * 26] * len(t) 这种方式初始化的二维列表不可取
        # dp表示每个位置上26个字符下一次出现在t中的位置, 不再出现用-1表示
        dp = [[0 for i in range(26)] for i in range(len(t))]
        for j in range(0, 26):
            nextPos = -1
            for i in range(len(t)-1, -1, -1):
                dp[i][j] = nextPos
                if(t[i] == chr(ord('a') + j)):
                    nextPos = i

        index = 0
        for x in s:
            index = dp[index][ord(x) - ord('a')]
            if(index == -1):
                return False
        return True