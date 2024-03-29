class Solution:
    def fullJustify(self, words, maxWidth: int):
        # 一个list存当前所有word，一个变量存当前word有多少位
        result = []
        cur = []
        num_of_letters = 0
        for word in words:
            if num_of_letters + len(word) + len(cur) - 1 >= maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                result.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur.append(word)
            num_of_letters += len(word)
        return result + [' '.join(cur).ljust(maxWidth)]