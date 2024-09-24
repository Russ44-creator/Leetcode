'''
Given logs and removed_time calculate the total penalty score
logs consist of 0 and 1 in one string
ex) "0 0 0 1 0 0"
0 means the server was up and running
1 means the server was down and not functioning
if the server is taken down too early you get a +1 penalty for reach the running server after removed_time
if the server is taken down too late, you get a +1 penalty for reach a server that was down before removed_time
Example 1
"0 0 1 0" remove_time = 2
| when the server is shut down, there is a penalty of 1 since during time 3-4 log4 
indicated it was on when it should have been off.
penalty = 1
Example 2
"0 0 1 0" remove_time = 0
penalty = 3
log 1, 2, 4 was on when it should have been off
Example 3
"1 1 1 0" remove_time = 0
penalty = 1
only log 4 was on when it should have been off
'''

'''
问题二 （在问题一的基础上）
write another function to give logs find when is the best time to take the server down
Example
log "1 1 1 0"
best_time = 0
because for time 1 2 3 4 penalties will be 2 3 4 3
at time 1 penalty is 1 which is the lowest
'''

'''
问题三 （在问题二的基础上）
write another function which can take in logs this time with 'BEGIN' 'END' '0' '1' '\n' they can be out of order
There are no nested loops,
ex) 'BEGIN END BEGIN BEGIN 1 0 0 END END 0 0 1'
The only valid sequence is BEGIN 1 0 0 END
It must start with BEGIN and end with END
There can be multiple valid sequences, return a list of ‍‌‍‍‍‌‌‍‌‌‍‌‍‍‌‍‌‍‍‍the best times to take the server down
Example 1
"BEGIN BEGIN 1 0 0 END"
return [3]
because the valid sequence is "1 0 0" now use the function we wrote in part 2 and return it in a list.
Example 2
"BEGIN BEGIN 1 0 0 END 0 0 0 1 BEGIN 1 1 1 0 END"
return [3, 0]
valid sequence is "1 0 0" and "1 1 1 0"
'''