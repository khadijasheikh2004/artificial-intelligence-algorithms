import heapq

def ucs(graph, start, goal):
    # Priority queue to store (cost, node, path) tuples
    priority_queue = [(0, start, [start])]  # (cost, node, path) - Start node with cost 0 and path as [start]
    visited = set()  # Set to keep track of visited nodes
    cost_so_far = {start: 0}  # Store the minimum cost to reach each node

    while priority_queue:
        # Pop the node with the lowest cost from the priority queue
        current_cost, current_node, path = heapq.heappop(priority_queue)

        # If the goal node is reached, return the total cost and path
        if current_node == goal:
            return current_cost, path

        # Skip this node if it has been visited
        if current_node in visited:
            continue

        # Mark the current node as visited
        visited.add(current_node)

        # Explore all the neighbors of the current node
        for neighbor, cost in graph[current_node]:
            new_cost = current_cost + cost

            # If the new cost to reach the neighbor is lower than the previously known cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

    # If the goal node cannot be reached, return infinity and an empty path
    return float('inf'), []

# Defining a graph as an adjacency list where each neighbor has a cost
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Find the least cost path from 'A' to 'G'
start = 'A'
goal = 'G'
result_cost, result_path = ucs(graph, start, goal)
print(f"Path: {' -> '.join(result_path)}")
print(f"Least cost from {start} to {goal}: {result_cost}")