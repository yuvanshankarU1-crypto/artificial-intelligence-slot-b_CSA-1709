def dfs(graph, current, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []
        
    visited.add(current)
    traversal_order.append(current)
    
    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal_order)
            
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
    
    print("DFS Traversal starting from 'A':", dfs(graph, 'A'))
