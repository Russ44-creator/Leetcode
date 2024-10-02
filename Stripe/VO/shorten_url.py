'''
Given a String, split it into major parts separated by special char '/'.
For each major part that's split by '/', we can further split it into minor parts separated by '.'.
### Example 1
str = stripe.com/payments/checkout/customer.john.doe
minor_parts = 2
after Part 1 compression
=>
s4e.c1m/p6s/c6t/c6r.j2n.d1e
after Part 2 compression
=>
s4e.c1m/p6s/c6t/c6r.j5e

# ### Example 2
Given:
str = www.api.stripe.com/checkout
minor_parts = 3
(after Part 1 compression)
=>
w1w.a1i.s4e.c1m/c6t
(then after Part 2 compression)
=>
w1w.a1i.s7m/c6t
  第一问是对每个minor_part 进行shorten
  第二问是再给一个参数m 每个major_part里只能有m个minor_part
  第三问是整个compressed_url 只能有m个minor_part, 
  也有看到帖子说会输入m, t, m表示一个major_part里可以有的minor_part数量, t是全部总共可以有的minor_part数量
''' 

# Part 1
url = 'stripe.com/payments/checkout/customer.john.doe'

def parse_minor_part(url):
    length = len(url)
    new_str = url[0] + str(length - 2) + url[-1]
    return new_str

def shorten_url_part1(url):
    major_parts = url.split('/')
    for i, major_part in enumerate(major_parts):
        minor_parts = major_part.split('.')
        for j in range(len(minor_parts)):
            minor_part = parse_minor_part(minor_parts[j])
            minor_parts[j] = minor_part
        major_parts[i] = '.'.join(minor_parts)
    return "/".join(major_parts)

print(shorten_url_part1(url)) 

# Part 2 第二问是再给一个参数m 每个major_part里只能有m个minor_part

def shorten_minor_parts(minor_parts):
    new_url = minor_parts[0][0]
    new_length = int(minor_parts[0][1]) + 1
    for i in range(1, len(minor_parts)):
        if i == len(minor_parts) - 1:
            new_length += (1 + int(minor_parts[i][1]))
            new_url += str(new_length)
            new_url += minor_parts[i][-1]
        else:
            new_length += (2 + int(minor_parts[i][1]))
    return new_url

def shorten_url_part2(url, m):
    major_parts = url.split('/')
    for i, major_part in enumerate(major_parts):
        minor_parts = major_part.split('.')
        for j in range(len(minor_parts)):
            minor_part = parse_minor_part(minor_parts[j])
            minor_parts[j] = minor_part
        if len(minor_parts) > m:
            minor_part_after_m = shorten_minor_parts(minor_parts[m - 1:])
            minor_parts = minor_parts[:m - 1]
            minor_parts.append(minor_part_after_m)
        major_parts[i] = '.'.join(minor_parts)
    return "/".join(major_parts)

# s4e.c1m/p6s/c6t/c6r.j5e
print(shorten_url_part2(url, 2))

# Part 3
# 第三问是整个compressed_url 只能有m个minor_part, 
# 也有看到帖子说会输入m, t, m表示一个major_part里可以有的minor_part数量, t是全部总共可以有的minor_part数量

def shorten_url_part3(url, m, t):
    # compare the number of major parts and t
    # build a length list
    major_parts = url.split('/')
    for i, major_part in enumerate(major_parts):
        minor_parts = major_part.split('.')
        for j in range(len(minor_parts)):
            minor_part = parse_minor_part(minor_parts[j])
            minor_parts[j] = minor_part
        if len(minor_parts) > m:
            minor_part_after_m = shorten_minor_parts(minor_parts[m - 1:])
            minor_parts = minor_parts[:m - 1]
            minor_parts.append(minor_part_after_m)
        major_parts[i] = '.'.join(minor_parts)
    return "/".join(major_parts)
