
# GRAPH - GARCIA

graph = {
    "G": ["A1", "R"],
    "A1": ["G", "C", "R"],
    "R": ["G", "A1", "I", "A2"],
    "C": ["A1", "I"],
    "I": ["C", "R"],
    "A2": ["R"]
}


# BFS - Breadth-First Search
def bfs(graph, start):
    queue = [start]
    visited = [start]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return result


# DFS - Depth-First Search
def dfs(graph, current, visited=None):
    if visited is None:
        visited = []

    visited.append(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# Convert internal names to letters
def display(result):
    return ["A" if node in ("A1", "A2") else node for node in result]


# Display results
print("GRAPH - GARCIA")
print("BFS:", " - ".join(display(bfs(graph, "G"))))
print("DFS:", " - ".join(display(dfs(graph, "G"))))
