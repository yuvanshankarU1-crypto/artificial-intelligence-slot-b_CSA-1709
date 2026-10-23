from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal_order = []
    
    visited.add(start_node)
    
    while queue:
        current = queue.popleft()
        traversal_order.append(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print("BFS Traversal starting from 'A':", bfs(graph, 'A'))
