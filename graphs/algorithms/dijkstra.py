# Dijkstra algorithm implementation

# It is an algorithm for finding the shortest paths between nodes in a graph.
# The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes,
# but a more common variant fixes a single node as the "source" node and finds shortest paths from the source
# to all other nodes in the graph, producing a shortest-path tree.

# The algorithm is often used in routing and as a subroutine in other graph algorithms.

# Time complexity: O(V^2) where V is the number of vertices in the graph.
# Space complexity: O(V) where V is the number of vertices in the graph.

from heapq import heappop, heappush
from collections import defaultdict


def convert_edges_to_graph(edges):
    graph = defaultdict(list)  # Store the graph as a dictionary of dictionaries

    for start, end, weight in edges:  # Iterate over the edges
        graph[start].append(
            (end, weight)
        )  # Add the end node and the weight to the start node
    return graph  # Return the graph


def dijkstra(graph, start):
    min_times = {}  # Store the minimum time to reach each node from the start node
    min_heap = [(0, start)]  # Store the distance and the node

    while min_heap:
        distance, node = heappop(min_heap)  # Get the node with the minimum distance
        if node in min_times:  # If the node is already visited, continue
            continue

        min_times[node] = distance  # Store the minimum distance to reach the node

        for neighbour, weight in graph[node]:  # Iterate over the neighbours of the node
            if (
                neighbour not in min_times
            ):  # If the neighbour is not visited, add it to the heap
                heappush(
                    min_heap, (distance + weight, neighbour)
                )  # Add the distance and the neighbour to the heap

    return min_times  # Return the minimum time to reach each node from the start node


edge = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]

graph = convert_edges_to_graph(edge)
print(dijkstra(graph, 2))  # Output: {2: 0, 1: 1, 3: 1, 4: 2}