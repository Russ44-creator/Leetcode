# https://www.1point3acres.com/bbs/thread-690899-1-1.html
'''
给一个很长的text和一个keyword array, 求每个keyword在这个text里的frequency。
我是建trie, split空格之后一个一个查的, 然而有个坑是不是所有的单词都是用空格split的 
（这个还在整句话偏后面的位置, 他们用的text editor不是自动换行的, 我特么还没有滚动鼠标把整个example
看到最后), 大E了, 没有闪。。。
最后说了一下怎么处理这种情况，以及如何用 one-pass 的方法来做。
follow-up 是假设 keyword 太多，一个 server 放不下该怎么办。
'''
