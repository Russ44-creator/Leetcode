# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf = []

    def read(self, buf: List[str], n: int) -> int:
        buf_len = len(self.buf)
        # 检查上一次多余的字符够不够
        if len(self.buf) >= n:
            buf[:n] = self.buf[:n]
            self.buf = self.buf[n:]
            return n
        # 如果不够
        cur = buf_len
        while cur < n:
            cache = [None] * 4
            num = read4(cache)
            self.buf += cache[:num]
            cur += num
            if num < 4 or n <= 4:
                break
        res = min(cur, n)
        buf[:res] = self.buf[:res]
        self.buf = self.buf[res:]
        return res