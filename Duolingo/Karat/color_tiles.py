'''
Suppose you have a one-dimensional board of two colors of tiles. Red tiles can only move to the right, 
black tiles can only move to the left. A tile can move 1 space at a time. Either they move to an adjacent 
empty space, or they can jump over a single tile of the other color to an empty space.
Eg:
red = R
black = B
empty = _
R _ B _ => _ R B _ or
R B _ _
R B _ _ => _ B R _

Given a start and end configuration represented as a list of strings, return a list of valid moves to 
get from start to end (doesn't need to be shortest), or None if none exist. 
Include the start and end states in the list of moves.

Example #1:
start_1 = ['R', '_', 'B', 'B']
end_1 = ['B', '_', 'B', 'R']
-> [
['R', '_', 'B', 'B']
['_', 'R', 'B', 'B']
['B', 'R', '_', 'B']
['B', 'R', 'B', '_']
['B', '_', 'B', 'R']

Example #2:
start_2 = ['R', 'R', '_']
end_2 = ['_', 'R', 'R']
-> [
['R', 'R', '_']
['R', '_', 'R']
['_', 'R', 'R']
]
All Test Cases:
validMoves(start_1, end_1)
validMoves(start_2, end_2)
n: number of spaces in the board
'''

def validMoves(start, end):
    # Helper function to get all valid next states from the current state
    def get_next_states(current):
        next_states = []
        n = len(current)
        for i in range(n):
            if current[i] == 'R':
                if i + 1 < n and current[i + 1] == '_':  # Move right
                    new_state = current[:]
                    new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                    next_states.append(new_state)
                if i + 2 < n and current[i + 2] == '_' and current[i + 1] in ['B']:  # Jump over B
                    new_state = current[:]
                    new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                    next_states.append(new_state)
            elif current[i] == 'B':
                if i - 1 >= 0 and current[i - 1] == '_':  # Move left
                    new_state = current[:]
                    new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                    next_states.append(new_state)
                if i - 2 >= 0 and current[i - 2] == '_' and current[i - 1] in ['R']:  # Jump over R
                    new_state = current[:]
                    new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                    next_states.append(new_state)
        return next_states

    # DFS function to explore all paths
    def dfs(current, path):
        if current == end:
            return path[:]
        if tuple(current) in visited:
            return None
        visited.add(tuple(current))
        for next_state in get_next_states(current):
            result = dfs(next_state, path + [next_state])
            if result:
                return result
        visited.remove(tuple(current))
        return None

    visited = set()
    path = dfs(start, [start])
    return path

# Testing the function with the provided examples
start_1 = ['R', '_', 'B', 'B']
end_1 = ['B', '_', 'B', 'R']
print(validMoves(start_1, end_1))

start_2 = ['R', 'R', '_']
end_2 = ['_', 'R', 'R']
print(validMoves(start_2, end_2))
