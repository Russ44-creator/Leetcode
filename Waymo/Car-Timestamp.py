'''
Given an integer N representing the number of timestamps, 
a list of tickets showing the entry time and exit time of each car. 
Return a list of numbers showing the number of cars in the garage of each time stamp. 
(total number of cars won't change at any exit time, but it will change at the next 
timestamp)
Example:
input:
N = 5
tickets = [(1, 3), (2, 4)]
output:
[0, 1, 2, 2, 1]
'''

tickets = [(1, 3), (2, 4)]
n = 5

'''
假dp ----> O(N):
用一个dictionary(用array/list也行)记录每个时间点的动态，key = timestamp, 
value = delta number of cars in the garage.
eg:
N = 5, tickets = [(1, 3), (2, 4)]
dict = {1: 1, 2: 1, 3: -1, 4: -1}
timestamp[i] = timestamp[i - 1] + dict[i] if i in dict and dict[i] > 0 
else timestamp[i - 1]
'''