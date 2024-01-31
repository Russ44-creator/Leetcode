class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        list_ = []
        for i in strs:
            list_.append('{:4}'.format(len(i)) + i)
        return ''.join(list_)
        

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """
        index = 0
        list_ = []
        while index < len(s):
            char_long = int(s[index:index + 4])
            list_.append(s[index + 4:index + char_long + 4])
            index += 4 + char_long
        return list_
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))