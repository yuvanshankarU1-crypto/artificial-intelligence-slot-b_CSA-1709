import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority queue stores: (f_score, g_score, current_node, path)
    pq = [(heuristics[start], 0, start, [start])]
    visited = set()
    
    while pq:
        f, g, current, path = heapq.heappop(pq)
        
        if current == goal:
            return path, g
            
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_g = g + weight
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
                
    return None, float('inf')

if __name__ == "__main__":
    # Graph structure: Node -> list of (neighbor, weight)
    graph = {
        'S': [('A', 1), ('G', 10)],
        'A': [('B', 2), ('C', 1)],
        'B': [('D', 5)],
        'C': [('D', 3), ('G', 4)],
        'D': [('G', 2)],
        'G': []
    }
    
    # Heuristic values from each node to Goal 'G'
    heuristics = {
        'S': 5,
        'A': 3,
        'B': 4,
        'C': 2,
        'D': 1,
        'G': 0
    }
    
    path, cost = a_star_search(graph, heuristics, 'S', 'G')
    print("A* Path:", path)
    print("Total Cost:", cost)
