# Depth First Search Algorithm

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V) where V is the number of vertices

# Directed Graph

from collections import deque


# For Acyclic Graphs
def dfs_acyclic(graph, start):
    stack = deque([start])

    while stack:
        node = stack.pop()
        print(node)
        for neighbour in graph[node]:
            stack.append(neighbour)


def dfs_acyclic_recursive(graph, node):
    print(node)
    for neighbour in graph[node]:
        dfs_acyclic_recursive(graph, neighbour)


# For Cyclic Graphs


def dfs_cyclic(graph, start):
    stack = deque([start])
    visited = set([start])

    while stack:
        node = stack.pop()
        print(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)


def dfs_cyclic_recursive(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs_cyclic_recursive(graph, neighbour, visited)


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
graph_cyclic = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": ["a"],
    "f": [],
}

source = "a"
dfs_acyclic(graph, source)  # a c e b d f
dfs_acyclic_recursive(graph, source)  # a b d f c e
dfs_cyclic(graph_cyclic, source)  # a c e b d f
dfs_cyclic_recursive(graph_cyclic, source, set())  # a b d f c e