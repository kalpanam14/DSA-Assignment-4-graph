#Detect Cycle in a Directed Graph
def has_cycle(graph):
    visited = set()
    recursion_stack = set()

    def dfs(node):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph[node]:
            if neighbor in recursion_stack:
                return True  # Cycle detected
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        recursion_stack.remove(node)
        return False

    # Perform DFS on each unvisited node
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True  # Cycle detected

    return False  # No cycle found

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['A'],
    'E': []
}

if has_cycle(graph):
    print("Cycle detected in the graph")
else:
    print("No cycle detected in the graph")
