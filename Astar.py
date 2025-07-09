from queue import PriorityQueue

def a_star_search(graph, heuristics, start, goal):
    # Initialize open and closed lists
    open_list = PriorityQueue()  # stores (f_cost, node, path)
    open_list.put((0 + heuristics[start], start, 0, [start]))  # (f_cost, node, g_cost, path)
    closed_list = set()  

    # Dictionary to track the best g-cost for each node
    g_costs = {start: 0}

    while not open_list.empty():
        # Find the node with the least f on the open list (q) and pop q off the open list 
        f_cost, current_node, current_g_cost, path = open_list.get()
        
        # Generate neighbors of q
        if current_node == goal:
            return path, current_g_cost  

        # Push q onto the closed list
        closed_list.add(current_node)

        # Process each neighbor 
        for neighbor, cost in graph[current_node]:
            if neighbor in closed_list:
                continue  # Skip if the neighbor is in the closed list
            
            # Calculate g_cost for the neighbor
            new_g_cost = current_g_cost + cost
            
            # Calculate heuristic value for the neighbor
            h_cost = heuristics[neighbor]
            
            # Calculate neighbor.f = neighbor.g + neighbor.h
            f_cost = new_g_cost + h_cost

            # Check if this path to the neighbor is better than any previously found
            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost  # Update g-cost for the neighbor
                open_list.put((f_cost, neighbor, new_g_cost, path + [neighbor]))  # Add to the open list with updated f-cost

    return None, float('inf')  # No path found

graph = {
    'S': [('A', 8), ('H', 4), ('I', 9)],
    'A': [('B', 5), ('H', 3), ('S', 8)],
    'B': [('D', 6), ('C', 6), ('H', 9), ('A', 5)],
    'C': [('H', 1), ('I', 5), ('D', 2), ('F', 7), ('B', 6)],
    'D': [('C', 2), ('E', 5), ('F', 2), ('B', 6)],
    'E': [('G', 4), ('F', 1), ('D', 5)],
    'F': [('G', 8), ('C', 7), ('D', 2), ('E', 1)],
    'G': [],
    'H': [('A', 3), ('S', 4), ('B', 9), ('C', 1), ('I', 2)],
    'I': [('H', 2), ('S', 9), ('C', 5)]
}

heuristics = {
    'S': 10, 'A': 9, 'B': 7, 'C': 4, 'D': 3, 'E': 2, 
    'F': 4, 'G': 0, 'H': 6, 'I': 7
}

start_node = 'S'
goal_node = 'G'

# Find shortest path using A* algorithm
path, total_cost = a_star_search(graph, heuristics, start_node, goal_node)

print(f"Shortest path: {' -> '.join(path)}")
print("Total cost:", total_cost)