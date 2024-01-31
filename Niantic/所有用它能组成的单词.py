'''
举例: 给了['t', 'e', 'a'], 返回所有这三个字符能组成的合理单词题目给的非常开放，没有任何限制，
需要跟面试官讨论assumption。比如，后来问出来
1）可‍‌‍‍‍‌‌‍‌‌‍‌‍‍‌‍‌‍‍‍以假设字符串没有重复字符
2）你有另外一个input，它包含了所牛津英汉大字典的词，可以用来verify是否是合理单词。
3）再聊发现，你可以预处理这个字典
'''

word_list = ['t', 'e', 'a']
word_set = set(word_list)
def recursion(word, used_set):
    ans_list = []
    for w in word_set - used_set:
        # print(used_set)
        new_word = word + w
        ans_list.append(new_word)
        used_set.add(w) 
        ans_list += recursion(new_word, used_set)
        used_set.remove(w)
    return ans_list

print(recursion("", set()))

