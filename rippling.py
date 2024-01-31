import math

def beacon_signal(x1, y1, x2, y2, xl, yl, R):
    
    # Initialize count
    count = 0
                
    for y in range(y1, y2+1):
        d = abs(y - yl)
        if d > R:
            continue
        h = math.sqrt(R ** 2 - d ** 2)
        count += (min(math.floor(h + xl), x2) - max(math.ceil(xl - h), x1)) + 1
    return count 

print(beacon_signal(0, 0, 1, 2, 0, 0, 1))