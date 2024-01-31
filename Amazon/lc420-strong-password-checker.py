class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        m = 0
        if any(chrs.isupper() for chrs in password)==True:
            m+=1
        if any(chrs.islower() for chrs in password)==True:
            m+=1
        if any(chrs.isdigit() for chrs in password)==True:
            m+=1
        if n < 6:
            return max(6-n,3-m)
        def isContinue(stra):
            n = len(stra)
            k = 1
            allc = []
            for i in range(n-1):
                if stra[i]==stra[i+1]:
                    k+=1
                else:
                    if k>=3:
                        allc.append(k)
                    k = 1
            if k>=3:
                allc.append(k)
            return allc
        allc = isContinue(password)
        if n >= 6 and n <= 20:
            g = 0
            for item in allc:
                g += int(item/3)
            return max(g, 3-m)
        elif n > 20:
            tot = 0
            cnts = [0] * 3
            for item in allc:
                tot += int(item/3)
                cnts[item % 3] += 1
            base = n - 20
            cur = base
            for i in range(3):
                if i == 2:
                    cnts[i] = tot
                if cnts[i] != 0 and cur != 0:
                    t = min(cnts[i] * (i + 1), cur)
                    cur -= t
                    tot -= int(t / (i + 1))
            return base+max(tot,3-m)