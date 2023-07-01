from collections import deque

def bfs(graph, start_vertex):
    visited = set()  # Set to keep track of visited vertices
    queue = deque([start_vertex])  # Queue for BFS traversal

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            neighbors = graph[vertex]
            queue.extend(neighbors)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')