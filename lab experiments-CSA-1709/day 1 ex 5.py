from collections import deque

def is_valid(m, c):
    # m: missionaries, c: cannibals on a bank
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    # Missionaries cannot be outnumbered by cannibals if any are present on either bank
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def missionaries_cannibals_bfs():
    # State format: (Missionaries_left, Cannibals_left, Boat_position)
    # Boat position: 1 for left bank, 0 for right bank
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    
    # Possible boat moves: (m_move, c_move)
    boat_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    while queue:
        (m, c, boat), path = queue.popleft()
        
        if (m, c, boat) == goal_state:
            return path + [(m, c, boat)]
            
        multiplier = -1 if boat == 1 else 1
        
        for dm, dc in boat_moves:
            next_m = m + multiplier * dm
            next_c = c + multiplier * dc
            next_boat = 1 - boat
            
            if is_valid(next_m, next_c):
                next_state = (next_m, next_c, next_boat)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [(m, c, boat)]))
                    
    return None

if __name__ == "__main__":
    print("Missionaries and Cannibals Solution Path:")
    solution = missionaries_cannibals_bfs()
    if solution:
        for idx, step in enumerate(solution):
            print(f"Step {idx}: Left Bank -> M:{step[0]}, C:{step[1]} | Boat:{'Left' if step[2]==1 else 'Right'}")
    else:
        print("No solution found.")
