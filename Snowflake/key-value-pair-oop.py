'''
write a data structure (key-String, value-Integer pair; unique keys, 
might have duplicate values)
Ex: ("a", 1), ("b", 2), ("c", 1)
实现以下方法
1. insert a new key, value pair
2. Given a key, return the value
3. Given a value, return a String[] of keys
4. Return the key with the smallest value (can be any key，
   比如例子里最小的为1，return a/c都行），delete the corresponding key, value pair
'''

hashmap = {}
valueList = {} # maintain a list
# or a heap
heap = [] # maintain the value, delete the key, value pair
