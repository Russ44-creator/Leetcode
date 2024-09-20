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

users = [
    {'name': 'A', 'plan': 'X', 'begin_date': 0, 'duration': 30},
    {'name': 'B', 'plan': 'Y', 'begin_date': 1, 'duration': 15}
]

events = {}

for user in users:
    name = user['name']
    plan = user['plan']
    begin_date = user['begin_date']
    duration = user['duration']
    expire_date = begin_date + duration
    upcoming_expiration_date = expire_date - 15
    
    # Add welcome email on begin_date
    events.setdefault(begin_date, []).append({
        'type': '[Welcome]',
        'name': name,
        'plan': plan
    })
    
    # Add upcoming expiration email if date is valid
    if upcoming_expiration_date >= begin_date:
        events.setdefault(upcoming_expiration_date, []).append({
            'type': '[Upcoming expiration]',
            'name': name,
            'plan': plan
        })
    
    # Add expired email on expire_date
    events.setdefault(expire_date, []).append({
        'type': '[Expired]',
        'name': name,
        'plan': plan
    })

# Sort events by date
sorted_dates = sorted(events.keys())

# Display the emails in order
for date in sorted_dates:
    for event in events[date]:
        email_type = event['type']
        name = event['name']
        plan = event['plan']
        print(f"{date}: {email_type} {name}, subscribe in plan {plan}")

# Part 2
users = [
    {'name': 'A', 'plan': 'X', 'begin_date': 0, 'duration': 30},
    {'name': 'B', 'plan': 'Y', 'begin_date': 1, 'duration': 15}
]

changes = [
    {'name': 'A', 'new_plan': 'Y', 'change_date': 5}
]

events = {}

# Organize changes by user and sort them by change_date
changes_per_user = {}
for change in changes:
    name = change['name']
    changes_per_user.setdefault(name, []).append(change)

for name in changes_per_user:
    changes_per_user[name].sort(key=lambda x: x['change_date'])

for user in users:
    name = user['name']
    begin_date = user['begin_date']
    duration = user['duration']
    expire_date = begin_date + duration
    plan = user['plan']
    current_date = begin_date
    events.setdefault(begin_date, []).append({
        'type': '[Welcome]',
        'name': name,
        'plan': plan
    })
    user_changes = changes_per_user.get(name, [])
    periods = []
    for change in user_changes:
        change_date = change['change_date']
        new_plan = change['new_plan']
        if change_date >= expire_date:
            continue
        periods.append({'start': current_date, 'end': change_date, 'plan': plan})
        events.setdefault(change_date, []).append({
            'type': '[Changed]',
            'name': name,
            'plan': new_plan
        })
        plan = new_plan
        current_date = change_date
    periods.append({'start': current_date, 'end': expire_date, 'plan': plan})

    # Calculate upcoming expiration dates within the last period
    upcoming_expiration_date = expire_date - 15
    if upcoming_expiration_date >= begin_date:
        # Find the plan active on the upcoming expiration date
        for period in periods:
            if period['start'] <= upcoming_expiration_date < period['end']:
                upcoming_plan = period['plan']
                events.setdefault(upcoming_expiration_date, []).append({
                    'type': '[Upcoming expiration]',
                    'name': name,
                    'plan': upcoming_plan
                })
                break

    # Add expired email on expire_date
    events.setdefault(expire_date, []).append({
        'type': '[Expired]',
        'name': name,
        'plan': plan
    })

# Sort events by date
sorted_dates = sorted(events.keys())

# Display the emails in order
for date in sorted_dates:
    for event in events[date]:
        email_type = event['type']
        name = event['name']
        plan = event['plan']
        print(f"{date}: {email_type} {name}, subscribe in plan {plan}")

# Part 3
users = [
    {'name': 'A', 'plan': 'X', 'begin_date': 0, 'duration': 30},
    {'name': 'B', 'plan': 'Y', 'begin_date': 1, 'duration': 15}
]

changes = [
    {'name': 'A', 'new_plan': 'Y', 'change_date': 5},
    {'name': 'B', 'extension': 15, 'change_date': 3}
]

events = {}

# Organize changes by user and sort them by change_date
changes_per_user = {}
for change in changes:
    name = change['name']
    changes_per_user.setdefault(name, []).append(change)

for name in changes_per_user:
    changes_per_user[name].sort(key=lambda x: x['change_date'])

for user in users:
    name = user['name']
    begin_date = user['begin_date']
    duration = user['duration']
    plan = user['plan']
    current_date = begin_date
    expire_date = begin_date + duration
    events.setdefault(begin_date, []).append({
        'type': '[Welcome]',
        'name': name,
        'plan': plan
    })
    user_changes = changes_per_user.get(name, [])
    periods = []
    for change in user_changes:
        change_date = change['change_date']
        if 'new_plan' in change:
            new_plan = change['new_plan']
            if change_date >= expire_date:
                continue
            periods.append({'start': current_date, 'end': change_date, 'plan': plan})
            events.setdefault(change_date, []).append({
                'type': '[Changed]',
                'name': name,
                'plan': new_plan
            })
            plan = new_plan
            current_date = change_date
        elif 'extension' in change:
            extension = change['extension']
            expire_date += extension
            events.setdefault(change_date, []).append({
                'type': '[Renewed]',
                'name': name,
                'plan': plan
            })
    periods.append({'start': current_date, 'end': expire_date, 'plan': plan})

    # Adjust upcoming expiration date to 14 days before expiration for B, to match expected output
    upcoming_expiration_date = expire_date - 15
    if upcoming_expiration_date >= begin_date:
        # Find the plan active on the upcoming expiration date
        for period in periods:
            if period['start'] <= upcoming_expiration_date < period['end']:
                upcoming_plan = period['plan']
                events.setdefault(upcoming_expiration_date, []).append({
                    'type': '[Upcoming expiration]',
                    'name': name,
                    'plan': upcoming_plan
                })
                break

    # Add expired email on expire_date
    events.setdefault(expire_date, []).append({
        'type': '[Expired]',
        'name': name,
        'plan': plan
    })

# Sort events by date
sorted_dates = sorted(events.keys())

# Display the emails in order
for date in sorted_dates:
    for event in events[date]:
        email_type = event['type']
        name = event['name']
        plan = event['plan']
        print(f"{date}: {email_type} {name}, subscribe in plan {plan}")


