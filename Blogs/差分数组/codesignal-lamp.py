import collections

def solution(lamps):
    illuminate = collections.defaultdict(lambda: 0)
    for x, y in lamps:
        illuminate[x - y] += 1
        illuminate[x + y] -= 1
    sorted_positions = sorted(illuminate.keys())
    current_illumination = 0
    count = 0
    for i in range(len(sorted_positions)):
        position = sorted_positions[i]
        current_illumination += illuminate[position]
        if current_illumination == 1:
            if i + 1 < len(sorted_positions):
                next_position = sorted_positions[i + 1]
                count += next_position - position - 1
                if illuminate[position] == 1:
                    count += 1
                if illuminate[next_position] == -1:
                    count += 1

    return count

if __name__ == "__main__":
    print(solution([[-2, 3], [2, 3], [2, 1]]))
    print(solution([[-2, 1], [2, 1]]))
    print(solution([[0, 2], [1, 1]]))
    print(solution([[1, 1]]))