def solution(A):
    moves = 0
    current_moves = 0
    for x in A:
        if current_moves < x:
            moves += x - current_moves
        current_moves = x
    return moves

print(solution([3, 2, 9, 1, 10]))