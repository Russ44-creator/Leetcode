'''
一个csv格式的string,csv里面有一些account receivable transaction history。
 然后要求你把里面的相同向合并。 然后格式也要稍微转换一下。
比如说:
merchant A, 2024-01-01, Visa, 100
merchant A, 2024-01-01, Visa, 200
Output:
merchant A, 2024-01-01, Visa, 300

Part 2, Part 3 就是可以添加一个contract, 一个contract可以由多个 account receivable 组成。
merchant A, 2024-01-01, Visa, 100
merchant A, 2024-01-01, Visa, 200
contract1, merchant A, 2024-01-01, Visa, 200

Output:
merchant A, 2024-01-01, Visa, 100
contract, 2024-01-01, Visa, 200
具体格式不太记得了。 题目不是很难，但是要读的东西特别多。
'''