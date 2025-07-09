graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': [],
    '8': []
}

visited = []  # List for visited nodes
stack = []    # Initializing Stack

# Function for DFS
def dfs(visited, graph, node):
    visited.append(node)
    stack.append(node)

    # Creating loop to visit each node
    while stack:
        m = stack.pop()  # Pop from the stack (LIFO)
        print(m, end=" ")

        # Reversed so that leftmost child is explored first
        for neighbour in reversed(graph[m]):
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

print("Following is the Depth-First Search:")
# Function Call
dfs(visited, graph, '5')