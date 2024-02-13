'''
def divide_algorithm(points):
    n = len(points)
    # 特判只有一个点或者是两个点的情况
    if n < 2:
        return sys.maxsize, None, None
    elif n == 2:
        return distance(points[0], points[1]), points[0], points[1]

    # 对所有点按照横坐标进行排序
    points = sorted(points)
    half = (n - 1) // 2
    # 递归，这里有一个问题，为什么要先排序再递归？
    d1, a1, b1 = divide_algorithm(points[:half])
    d2, a2, b2 = divide_algorithm(points[half:])
    d, a, b = (d1, a1, b1) if d1 < d2 else (d2, a2, b2)

    calibration = points[half][0]
 
    # 根据中间的位置将点集分成两个部分
    left, right = [], []
    for u in points:
        if calibration - d < u[0] < calibration:
            left.append(u)
        elif calibration <= u[0] < calibration + d:
            right.append(u)

    # 右侧点集按照纵坐标排序
    right = sorted(right, key=lambda x: (x[1], x[0]))

    res = d

    for u in left:
        # 左开右闭的二分
        l, r = -1, len(right)-1
        while r - l > 1:
            m = (l + r) >> 1
            if right[m][1] <= u[1] - d:
                l = m
            else:
                r = m

        idx = r
  
        # 在范围内最多只有6个点能够构成最近点对
        for j in range(7):
            if j + idx >= len(right):
                break
            if distance(u, right[idx + j]) < res:
                res = distance(u, right[idx + j])
                a, b = u, right[idx + j]

    return res, a, b

'''