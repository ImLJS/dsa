# Breadth First Search Algorithm

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V) where V is the number of vertices

# Directed Graph

from collections import deque


# For Acyclic Graphs
def bfs_acyclic(graph, source):
    queue = deque([source])  # Initialize the queue with the source node

    while queue:
        node = queue.popleft()  # Pop the first element from the queue
        print(node)
        for neighbour in graph[node]:  # Iterate over the neighbours of the node
            queue.append(neighbour)  # Add the neighbour to the queue


# For Cyclic Graphs


def bfs_cyclic(graph, source):
    queue = deque([source])  # Initialize the queue with the source node
    visited = set([source])  # Initialize the visited set with the source node

    while queue:
        node = queue.popleft()  # Pop the first element from the queue
        print(node)
        for neighbour in graph[node]:  # Iterate over the neighbours of the node
            if neighbour not in visited:  # If the neighbour is not visited
                queue.append(neighbour)  # Add the neighbour to the queue
                visited.add(neighbour)  # Add the neighbour to the visited set


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": ["a"],
    "f": [],
}

source = "a"

bfs_acyclic(graph, source)  # a b c d e f