import heapq

# Goal state
GOAL_STATE = (1, 2, 3, 
              4, 5, 6, 
              7, 8, 0) # 0 represents the blank tile

# Possible moves: (row_change, col_change)
MOVES = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]

def calculate_manhattan(state):
    """Calculates Manhattan distance heuristic."""
    distance = 0
    for i, val in enumerate(state):
        if val != 0:
            target_x, target_y = (val - 1) // 3, (val - 1) % 3
            curr_x, curr_y = i // 3, i % 3
            distance += abs(curr_x - target_x) + abs(curr_y - target_y)
    return distance

def get_neighbors(state):
    """Generates valid neighboring states."""
    neighbors = []
    zero_idx = state.index(0)
    x, y = zero_idx // 3, zero_idx % 3
    
    for dx, dy, move in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            n_idx = nx * 3 + ny
            new_state = list(state)
            new_state[zero_idx], new_state[n_idx] = new_state[n_idx], new_state[zero_idx]
            neighbors.append((tuple(new_state), move))
    return neighbors

def solve_8_puzzle(start_state):
    """Solves the 8-puzzle using A* search."""
    # Priority queue stores: (f_score, g_score, current_state, path)
    pq = [(calculate_manhattan(start_state), 0, start_state, [])]
    visited = set()
    
    while pq:
        f, g, current, path = heapq.heappop(pq)
        
        if current == GOAL_STATE:
            return path
            
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, move in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + calculate_manhattan(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [move]))
    return None

# Example usage:
if __name__ == "__main__":
    initial_state = (1, 2, 3, 
                     4, 0, 5, 
                     6, 7, 8)
    print("Initial State:", initial_state)
    solution = solve_8_puzzle(initial_state)
    print("Solution path:", solution)
