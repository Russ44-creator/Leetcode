'''
subscription: list of users {name, plan, begin_date, duration}, 
要求按顺序发email (plan当天发welcome, -15 days发upcoming expiration, expire当天发expire)
第二问: 基础上增加一个change in plans, list of changes {name, new_plan, change_date}
第三问是bonus, 第二问的基础上再加一个renew, change list中entry为 {name, extension, change_date}
例如：
users = [{name: A, plan: X, begin_date = 0, duration = 30}, {name: B, plan: Y, 
begin_date = 1, duration = 15}],
输出
0: [Welcome] A, subscribe in plan X
1: [Welcome] B, subscribe in plan Y
1: [Upcoming expiration] B, subscribe in plan Y
15: [Upcoming expiration] A, subscribe in plan X
16: [Expired] B, subcribe in plan Y
30: [Expired] A, subscribe in plan X
'''
users = [
    {'name': 'A', 'plan': 'X', 'begin_date': 0, 'duration': 30},
    {'name': 'B', 'plan': 'Y', 'begin_date': 1, 'duration': 15}
]

from collections import defaultdict
def print_user_subscription(users):
    res = defaultdict(list)
    for user in users:
        name, plan, begin_date, duration = user['name'], user['plan'], int(user['begin_date']), int(user['duration'])
        timeList = {"Welcome": begin_date, 
                    "Upcoming expiration": duration + begin_date - 15, "Expired": duration + begin_date}
        for action, time in timeList.items():
            res[time].append(f"{time}, [{action}] {name}, subscribe in plan {plan}")
    for key, value in res.items():
        value.sort(reverse=True)
    res = dict(sorted(res.items(), key=lambda x: x[0]))
    ans = []
    for time, actions in res.items():
        for action in actions:
            ans.append(action)
    return ans

print(print_user_subscription(users))

'''
第二问例如：
users = [{name: A, plan: X, begin_date = 0, duration = 30}, {name: B, plan: Y, begin_date = 1, duration = 15}]
changes = [{name: A, new_plan: Y, change_date = 5}]
输出
0: [Welcome] A, subscribe in plan X
1: [Welcome] B, subscribe in plan Y
1: [Upcoming expiration] B, subscribe in plan Y
5: [Changed] A, subscribe in plan Y
15: [Upcoming expiration] A, subscribe in plan Y
16: [Expired] B, subcribe in plan Y
30: [Expired] A, subscribe in plan Y
'''
users = [
    {'name': 'A', 'plan': 'X', 'begin_date': 0, 'duration': 30},
    {'name': 'B', 'plan': 'Y', 'begin_date': 1, 'duration': 15}
]
changes = [{'name': 'A', 'new_plan': 'Y', 'change_date': 5}]

from collections import defaultdict
def print_user_subscription_part2(users, changes):
    res = defaultdict(list)
    for user in users:
        name, plan, begin_date, duration = user['name'], user['plan'], int(user['begin_date']), int(user['duration'])
        timeList = {"Welcome": begin_date, 
                    "Upcoming expiration": duration + begin_date - 15, "Expired": duration + begin_date}
        userChanges = {}
        for change in changes:
            if change['name'] == name:
                userChanges[change['change_date']] = change['new_plan']
                timeList["Changed"] = change['change_date']
        timeList = dict(sorted(timeList.items(), key=lambda x: x[1]))
        for action, time in timeList.items():
            if action == "Changed":
                plan = userChanges[time]
                res[time].append(f"{time}, [{action}] {name}, subscribe in plan {plan}")
            else:
                res[time].append(f"{time}, [{action}] {name}, subscribe in plan {plan}")
    for key, value in res.items():
        value.sort(reverse=True)
    res = dict(sorted(res.items(), key=lambda x: x[0]))
    ans = []
    for time, actions in res.items():
        for action in actions:
            ans.append(action)
    return ans

print(print_user_subscription_part2(users, changes))
'''
第三问例如：
users = [{name: A, plan: X, begin_date = 0, duration = 30},
{name: B, plan: Y, begin_date = 1, duration = 15}]
changes = [{name: A, new_plan: Y, change_date: 5}, {name: B, extension: 15, change_date: 3}]
输出
0: [Welcome] A, subscribe in plan X
1: [Welcome] B, subscribe in plan Y
1: [Upcoming expiration] B, subscribe in plan Y
3: [Renewed] B, subscribe in plan Y
5: [Changed] A, subscribe in plan Y
15: [Upcoming expiration] A, subscribe in plan Y
16: [Upcoming expiration] B, subcribe in plan Y
30: [Expired] A, subscribe in plan Y
30: Expired] B, subscribe in plan Y
'''