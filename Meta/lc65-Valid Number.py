class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        #print(s)
        dot_seen = False
        e_seen = False
        num_seen = False
        for i, a in enumerate(s):
            if a.isdigit():
                num_seen = True
            elif a == ".":
                if e_seen or dot_seen:
                    return False
                dot_seen = True
            elif a == "e" or a == "E":
                if e_seen or not num_seen:
                    return False
                num_seen = False
                e_seen = True
            elif a in "+-":
                if i > 0 and (s[i - 1] != "e" and s[i - 1] != "E"):
                    return False
            else:
                return False
        return num_seen