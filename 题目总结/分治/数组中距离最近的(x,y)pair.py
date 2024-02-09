import sys
import math

def distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def divide_algo(points):
    n = len(points)
    if n < 2:
        return sys.maxsize, None, None
    elif n == 2:
        return distance(points[0], points[1]), points[0], points[1]
    points = sorted(points)
    half = (n - 1) // 2
    d1, a1, b1 = divide_algo(points[:half])
    d2, a2, b2 = divide_algo(points[half:])
    d, a, b = (d1, a1, b1) if d1 < d2 else (d2, a2, b2)
    calibration = points[half][0]
    left, right = [], []
    for u in points:
        if calibration - d < u[0] < calibration:
            left.append(u)
        elif calibration <= u[0] < calibration + d:
            right.append(u)
    right = sorted(right, key=lambda x: (x[1], x[0]))
    res = d
    for u in left:
        l, r = -1, len(right) - 1
        while r - l > 1:
            m = (l + r) // 2
            if right[m][1] <= u[1] - d:
                l = m
            else:
                r = m
        idx = r
        for j in range(7):
            if j + idx >= len(right):
                break
            if distance(u, right[idx + j]) < res:
                res = distance(u, right[idx + j])
                a, b = u, right[idx + j]
    return res, a, b