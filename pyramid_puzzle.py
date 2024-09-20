import sys

def find_path(pyramid, target, row, index, current_product, path):
    if index < 0 or index >= len(pyramid[row]):
        return None
    current_number = pyramid[row][index]
    new_product = current_product * current_number
    if row == len(pyramid) - 1:
        if new_product == target:
            return path
        else:
            return None
    left = find_path(pyramid, target, row + 1, index, new_product, path + 'L')
    if left is not None:
        return left
    right = find_path(pyramid, target, row + 1, index + 1, new_product, path + 'R')
    if right is not None:
        return right
    return None

def main():
    lines = sys.stdin.read().splitlines()
    lines = [line.strip() for line in lines if line.strip()]

    target_line = lines[0]
    target_str = target_line[len('Target:'):].strip()
    target = int(target_str)

    pyramid = []
    for line in lines[1:]:
        row = [int(s.strip()) for s in line.strip().split(',')]
        pyramid.append(row)

    result = find_path(pyramid, target, row=0, index=0, current_product=1, path='')

    if result is not None:
        print(result)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
