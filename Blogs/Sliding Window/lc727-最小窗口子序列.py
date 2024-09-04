class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # 先计算包含 T 的前缀子串的窗口，再根据前缀子串窗口不断拓展，找到包含整个字符串的窗口。
        cur = [-1] * len(S)
        for i, m_char in enumerate(S):
            # 用cur数组标记所有T[0]在S中出现的位置。
            if m_char == T[0]:
                cur[i] = i
        
        # 遍历T中所有的字符，不断找到T中所有字符在S中出现的所有位置。
        for j in range(1, len(T)):
            # last 用来标记T上一个字符最后出现的位置。
            last = -1
            # new 用来标记上一个字符T[j - 1]在S中出现的所有位置。
            new = [-1] * len(S)
            for i, m_char in enumerate(S):
                # 由于我们需要保证T字符的顺序，因此只有在上一个字符出现过，然后当前字符出现的情况下，才会记录上一个字符字符的位置。这样能够保证所有T字符都在S中，以正确的顺序出现。
                if last != -1 and m_char == T[j]:
                    new[i] = last
                if cur[i] != -1:
                    last = cur[i]
            cur = new
        
        # 到这里时，cur[i]中存储的元素（在!=-1时）代表：以S[i]为终点的最小窗口子序列的起点坐标。
        start, end = 0, len(S)
        for end_index, start_index in enumerate(cur):
            if start_index >= 0 and end_index - start_index < end - start:
                start, end = start_index, end_index
        return S[start: end + 1] if end < len(S) else ""