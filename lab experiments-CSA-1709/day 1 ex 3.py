from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0, [])]) # (jug1, jug2, path)
    
    while queue:
        j1, j2, path = queue.popleft()
        
        if j1 == target or j2 == target:
            return path + [(j1, j2)]
            
        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))
        
        # Possible states
        transitions = [
            (jug1_capacity, j2, "Fill Jug 1"),
            (j1, jug2_capacity, "Fill Jug 2"),
            (0, j2, "Empty Jug 1"),
            (j1, 0, "Empty Jug 2"),
            (j1 - min(j1, jug2_capacity - j2), j2 + min(j1, jug2_capacity - j2), "Pour Jug 1 -> Jug 2"),
            (j1 + min(j2, jug1_capacity - j1), j2 - min(j2, jug1_capacity - j1), "Pour Jug 2 -> Jug 1")
        ]
        
        for next_j1, next_j2, action in transitions:
            if (next_j1, next_j2) not in visited:
                queue.append((next_j1, next_j2, path + [(j1, j2, action)]))
                
    return None

if __name__ == "__main__":
    jug1, jug2, target = 4, 3, 2
    print(f"Solving for Jugs of capacity {jug1}L and {jug2}L to measure {target}L:")
    solution = water_jug_bfs(jug1, jug2, target)
    if solution:
        for step in solution:
            print(step)
    else:
        print("No solution found.")
