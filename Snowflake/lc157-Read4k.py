class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        bi = 0
        for _ in range(0, n, 4):
            tmp = [None] * 4
            cur_len = read4(tmp)
            for j in range(cur_len):
                buf[bi] = tmp[j]
                bi += 1
        return min(bi, n)