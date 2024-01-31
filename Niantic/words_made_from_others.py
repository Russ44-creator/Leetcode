'''
Niantic 电面
chars = ['g', 't', 's', 'a', 'b', 'i', 'e', 'g', 't', 'g']
words = ["abs", "table", "bags", "tab", "bib", "egg", "gab"]
write a function which filters the words into only ones that can be made from chars.
Each character in chars can only be used once (but each word is evaluated independentl‍‌‍‍‍‌‌‍‌‌‍‌‍y)
# >>> print wordFilter(words, chars)
["abs", "bags", "tab", "egg", "gab"]
'''
import collections

chars = ['g', 't', 's', 'a', 'b', 'i', 'e', 'g', 't', 'g']
words = ["abs", "table", "bags", "tab", "bib", "egg", "gab"]

c = collections.Counter(chars)
ans = []
for word in words:
    add = 1
    temp_c = c.copy()
    for w in word:
        if w not in temp_c:
            add = 0
            break
        else:
            if temp_c[w] == 0:
                add = 0
                break
            else:
                temp_c[w] -= 1
    if add == 1:
        ans.append(word)
print(ans)





