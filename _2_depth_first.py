def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited vertices

    print(start_vertex)
    visited.add(start_vertex)

    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')