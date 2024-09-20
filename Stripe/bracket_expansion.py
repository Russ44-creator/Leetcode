# https://www.1point3acres.com/bbs/thread-1083166-1-1.html
# https://www.1point3acres.com/bbs/thread-1073812-1-1.html
# https://www.1point3acres.com/bbs/thread-1071491-1-1.html
'''
Question - Bracket Expansion
You are given a string expression which consists of several comma separated tokens
enclosed within opening ('{') and closing ('}') curly braces.
The string expression might or might not have a prefix before opening curly brace('{') and
a suffix after closing curly brace ('}').
You have to return a list of strings as output for each comma separated item as shown below in the examples
Example 1:
Input = "/2022/{jan,feb,march}/report"
List<String> Output = "/2022/jan/report"
"/2022/feb/report"
"/2022/march/report"
Example 2:
Input = "over{crowd,eager,bold,fond}ness"
Output = "overcrowdness"
"overeagerness"
"overboldness"
"overfondness"
Example 3:
Input = "read.txt{,.bak}"
Output = "read.txt"
"read.txt.bak"

part2:
If there are less than 2 tokens enclosed within curly braces or incorrect expression
(eg. opening and close braces not present, only opening brace present,
closing brace present before opening brace etc) return the output same as input
these patterns do not have enough tokens, so they are not expanded:
Example 1:
Input: pre{mid}suf
Output: pre{mid}suf
Example 2:
Input: pre{}suf
Output: pre{}suf
these pattrens have invalid braces:

part3:
expand multiple braces lc1087
'''