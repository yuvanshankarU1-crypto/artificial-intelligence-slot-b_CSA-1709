import itertools

def calculate_total_distance(route, distance_matrix):
    distance = 0
    for i in range(len(route) - 1):
        distance += distance_matrix[route[i]][route[i+1]]
    # Return to starting city
    distance += distance_matrix[route[-1]][route[0]]
    return distance

def tsp_brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    
    min_distance = float('inf')
    best_route = None
    
    # Fix the starting city as 0 to avoid duplicate permutations of the same cycle
    for perm in itertools.permutations(cities[1:]):
        route = [0] + list(perm)
        current_distance = calculate_total_distance(route, distance_matrix)
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
            
    return best_route, min_distance

if __name__ == "__main__":
    # Distance matrix between 4 cities
    # Row/Col 0, 1, 2, 3
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    route, min_dist = tsp_brute_force(dist_matrix)
    print("Best Route:", route)
    print("Minimum Distance:", min_dist)
