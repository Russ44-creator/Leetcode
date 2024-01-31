short_s = "AB"
long_s = "ABBACABABA"

def repe(word, sequence):
   
    n = len(sequence)
    wn = len(word)
    maxrepeat = 0
    i = 0
    while i <= n - maxrepeat * wn:
        j = 0
        while i + j < n and sequence[i + j] == word[j % wn]:
            j += 1
        maxrepeat = max(maxrepeat, j // wn)
        i += 1
    return maxrepeat
    

print (repe(short_s, long_s))