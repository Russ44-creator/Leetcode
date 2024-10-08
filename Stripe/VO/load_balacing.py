'''
有一个 class loadBalancer，假如有a,b,c server，实现一个route方法
让 lb.route(weight = 2) 返回a，
lb.route(weight = 1) 返回b，
lb.route(weight = 1) 返回c，
lb.rounte(weight = 1) 返回b
最后一次返回b是因为b跟c此时都有weight 为1的request，这个时候我们找server字母排列最小的

要求return给user在available server中，符合constraints的最小weight server。
（1）第一问：直接return 最小weight server。weight相同return 字符最小的
（2）第二问：加上ttl-time to live。用语言自带的time package，然后每个server记录每个task结束的时间，
然后在结束相应的task就行。
（3）第三问：server有了可接受的最大load。没啥可说的。
'''