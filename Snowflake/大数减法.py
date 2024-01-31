def subtract(num1, num2):
    result = ""
    borrow = 0
    len1, len2 = len(num1), len(num2)
    if len1 < len2:
        num1, num2 = num2, num1
        len1, len2 = len2, len1
        result = "-"
    elif len1 == len2 and num1 < num2:
        num1, num2 = num2, num1
        len1, len2 = len2, len1
        result = "-"
    for i in range(len1):
        digit1 = int(num1[len1-1-i])
        digit2 = int(num2[len2-1-i]) if i < len2 else 0
        digit = digit1 - digit2 - borrow
        borrow = 0
        if digit < 0:
            digit += 10
            borrow = 1
        result = str(digit) + result
    result = result.lstrip("0")
    if not result:
        result = "0"
    return result